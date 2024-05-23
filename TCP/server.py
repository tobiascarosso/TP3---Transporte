import socket

# Configuración del servidor
SERVER_HOST = '127.0.0.1'
SERVER_PORT = 12345

# Crear un socket TCP
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Enlazar el socket al host y puerto
server_socket.bind((SERVER_HOST, SERVER_PORT))

# Escuchar conexiones entrantes
server_socket.listen(5)

print("Servidor TCP esperando conexiones entrantes en", SERVER_HOST, ":", SERVER_PORT)

while True:
    # Esperar a que un cliente se conecte
    client_socket, client_address = server_socket.accept()

    try:
        # Recibir datos del cliente
        data = client_socket.recv(1024).decode()

        if data:
            print("Mensaje del cliente:", data)

            # Procesar la solicitud (aquí puedes realizar cualquier lógica de procesamiento necesaria)

            # Enviar una respuesta al cliente
            response = "Ok! Recibido desde " + client_address[0] + ":" + str(client_address[1])
            client_socket.send(response.encode())
    except Exception as e:
        print("Error:", e)
    finally:
        # Cerrar el socket del cliente
        client_socket.close()

# Cerrar el socket del servidor
server_socket.close()