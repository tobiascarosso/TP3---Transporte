import socket

# Configuración del servidor
SERVER_HOST = '127.0.0.1'
SERVER_PORT = 12345

# Crear un socket UDP
server_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

# Enlazar el socket al host y puerto
server_socket.bind((SERVER_HOST, SERVER_PORT))

print("Servidor UDP esperando mensajes en", SERVER_HOST, ":", SERVER_PORT)

while True:
    # Recibir datos del cliente
    data, client_address = server_socket.recvfrom(1024)
    print("Mensaje del cliente:", data.decode(), "desde", client_address)

# Cerrar el socket
server_socket.close()