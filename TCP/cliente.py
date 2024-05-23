import socket

# Configuración del servidor
SERVER_HOST = '127.0.0.1'
SERVER_PORT = 12346

# Crear un socket TCP
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Conectar al servidor
client_socket.connect((SERVER_HOST, SERVER_PORT))

# Enviar datos al servidor
message = "Hola, servidor!"
client_socket.sendall(message.encode())

# Recibir respuesta del servidor
response = client_socket.recv(1024).decode()
print("Respuesta del servidor:", response)

# Cerrar el socket
client_socket.close()