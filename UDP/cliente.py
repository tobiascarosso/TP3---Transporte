import socket

# Configuración del servidor
SERVER_HOST = '127.0.0.1'
SERVER_PORT = 12346

while True:
    # Crear un socket UDP
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)


    # Obtener el mensaje del usuario
    message = input("Ingrese el mensaje para enviar al servidor: ")

    # Enviar datos al servidor
    client_socket.sendto(message.encode(), (SERVER_HOST, SERVER_PORT))

    # Cerrar el socket
    client_socket.close()