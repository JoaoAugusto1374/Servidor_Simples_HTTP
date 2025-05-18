from http.server import HTTPServer, BaseHTTPRequestHandler

class MeuServidor(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.send_header("Content-type", "text/plain; charset=utf-8")
        self.end_headers()
        self.wfile.write("Olá mundo!".encode("utf-8"))
servidor = HTTPServer(('localhost', 8000), MeuServidor)
print("Servidor rodando em localhost http://localhost:8000")
servidor.serve_forever()