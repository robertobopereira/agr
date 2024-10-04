from http.server import BaseHTTPRequestHandler, HTTPServer

class SimpleHTTPRequestHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        # Captura os cabeçalhos
        headers_text = f"Cabeçalhos da requisição:\n{self.headers}\n"
        
        # Monta a resposta com os cabeçalhos
        response = headers_text
        
        # Retorna a requisição para o cliente
        self.send_response(200)
        self.send_header('Content-type', 'text/plain')
        self.end_headers()
        self.wfile.write(response.encode('utf-8'))

    def do_POST(self):
        # Captura os cabeçalhos
        headers_text = f"Cabeçalhos da requisição:\n{self.headers}\n"
        
        # Lê o corpo da requisição POST
        content_length = int(self.headers['Content-Length']) if 'Content-Length' in self.headers else 0
        post_data = self.rfile.read(content_length) if content_length > 0 else b''
        
        # Converte o corpo da requisição para texto, se houver
        body_text = f"Corpo da requisição:\n{post_data.decode('utf-8') if post_data else 'Nenhum dado enviado'}\n"
        
        # Monta a resposta com cabeçalhos e corpo
        response = headers_text + body_text
        
        # Retorna a requisição para o cliente
        self.send_response(200)
        self.send_header('Content-type', 'text/plain')
        self.end_headers()
        self.wfile.write(response.encode('utf-8'))

def run(server_class=HTTPServer, handler_class=SimpleHTTPRequestHandler, port=8080):
    server_address = ('', port)
    httpd = server_class(server_address, handler_class)
    print(f"Servidor rodando na porta {port}...")
    httpd.serve_forever()

if __name__ == '__main__':
    run()
