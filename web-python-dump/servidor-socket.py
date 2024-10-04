import socket

def start_server(host='localhost', port=8080):
    # Cria o socket
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    
    # Associa o socket ao endereço e porta
    server_socket.bind((host, port))
    
    # Coloca o socket em modo de escuta
    server_socket.listen(1)
    print(f"Servidor rodando em {host}:{port}...")

    while True:
        # Aceita uma nova conexão
        client_socket, client_address = server_socket.accept()
        print(f"Conexão recebida de {client_address}")

        # Lê a requisição do cliente
        request_data = client_socket.recv(1024).decode('utf-8')
        print(f"Requisição recebida:\n{request_data}")

        # Monta a resposta HTTP (retornando a própria requisição em texto puro)
        http_response = f"HTTP/1.1 200 OK\r\n"
        http_response += "Content-Type: text/plain\r\n"
        http_response += f"Content-Length: {len(request_data)}\r\n"
        http_response += "Connection: close\r\n"
        http_response += "\r\n"
        http_response += request_data

        # Envia a resposta para o cliente
        client_socket.sendall(http_response.encode('utf-8'))
        
        # Fecha a conexão com o cliente
        client_socket.close()

if __name__ == "__main__":
    start_server()
