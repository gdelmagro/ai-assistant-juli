from http.server import BaseHTTPRequestHandler, ThreadingHTTPServer
from io import BytesIO
from pathlib import Path
import json

from openpyxl import Workbook

ROOT = Path(__file__).resolve().parent
HOST = '127.0.0.1'
PORT = 8765

class Handler(BaseHTTPRequestHandler):
    def do_GET(self):
        if self.path != '/':
            self.send_error(404)
            return
        body = (ROOT / 'index.html').read_bytes()
        self.send_response(200)
        self.send_header('Content-Type', 'text/html; charset=utf-8')
        self.send_header('Content-Length', str(len(body)))
        self.send_header('Cache-Control', 'no-store')
        self.end_headers()
        self.wfile.write(body)

    def do_POST(self):
        if self.path != '/export' or self.headers.get('Origin') != f'http://localhost:{PORT}':
            self.send_error(403)
            return
        try:
            size = int(self.headers.get('Content-Length', '0'))
            if size < 1 or size > 2_000_000:
                raise ValueError('Tamaño inválido')
            data = json.loads(self.rfile.read(size))
            columns = ['Semana', 'Día', 'Hora', 'Médica', 'Protocolo', 'Coordinadora', 'Número de paciente', 'Visita', 'LAB', 'PK', 'ECG', 'NUTRI', 'AUTO', 'FCI']
            rows = data['rows']
            if not isinstance(rows, list) or len(rows) > 5000:
                raise ValueError('Filas inválidas')
            book = Workbook()
            sheet = book.active
            sheet.title = 'Agenda filtrada'
            sheet.append(columns)
            for row in rows:
                if not isinstance(row, list) or len(row) != len(columns):
                    raise ValueError('Fila inválida')
                # Values from Sheets are data, never executable spreadsheet formulas.
                clean = []
                for value in row:
                    value = str(value or '')
                    clean.append("'" + value if value.startswith(('=', '+', '-', '@')) else value)
                sheet.append(clean)
            sheet.freeze_panes = 'A2'
            sheet.auto_filter.ref = sheet.dimensions
            buffer = BytesIO()
            book.save(buffer)
            body = buffer.getvalue()
        except (ValueError, KeyError, TypeError, json.JSONDecodeError):
            self.send_error(400)
            return
        self.send_response(200)
        self.send_header('Content-Type', 'application/vnd.openxmlformats-officedocument.spreadsheetml.sheet')
        self.send_header('Content-Disposition', 'attachment; filename="agenda-filtrada.xlsx"')
        self.send_header('Cache-Control', 'no-store')
        self.send_header('Content-Length', str(len(body)))
        self.end_headers()
        self.wfile.write(body)

    def log_message(self, format, *args):
        pass

if __name__ == '__main__':
    print(f'Tablero disponible en http://localhost:{PORT}', flush=True)
    ThreadingHTTPServer((HOST, PORT), Handler).serve_forever()
