from http.server import BaseHTTPRequestHandler, HTTPServer

class SimpleHTTPRequestHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        # Imprime os cabeçalhos da requisição no console
        print(f"Requisição recebida com os cabeçalhos:\n{self.headers}\n")

        # Enviar resposta ao cliente
        self.send_response(200)
        self.send_header('Content-type', 'text/plain')
        self.end_headers()

        # Enviar corpo da resposta
        self.wfile.write(response.encode('utf-8'))


    def do_POST(self):
        # Lê o corpo da requisição POST
        content_length = int(self.headers['Content-Length'])
        post_data = self.rfile.read(content_length)
        
        # Imprime os cabeçalhos e o corpo da requisição no console
        print(f"Requisição POST recebida com os cabeçalhos:\n{self.headers}\n")
        print(f"Corpo da requisição: {post_data.decode('utf-8')}\n")
        
        # Enviar resposta ao cliente
        self.send_response(200)
        self.send_header('Content-type', 'text/html')
        self.end_headers()
        
        # Enviar corpo da resposta
        self.wfile.write(b"POST recebido! Veja os logs do servidor para os detalhes do pacote HTTP.")

def run(server_class=HTTPServer, handler_class=SimpleHTTPRequestHandler, port=8080):
    server_address = ('', port)
    httpd = server_class(server_address, handler_class)
    print(f"Servidor rodando na porta {port}...")
    httpd.serve_forever()

if __name__ == '__main__':
    run()
