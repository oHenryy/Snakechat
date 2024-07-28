import socket
import threading

# Configurações do servidor
HOST = '127.0.0.1'  # Endereço IP do servidor
PORT = 12345        # Porta do servidor

# Inicializa o socket do servidor
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((HOST, PORT))
server.listen()

# Lista para armazenar clientes conectados
clients = []
nicknames = []

# Função para enviar mensagens para todos os clientes
def broadcast(message):
    for client in clients:
        client.send(message)

# Função para lidar com os clientes
def handle_client(client):
    while True:
        try:
            # Recebe a mensagem do cliente
            message = client.recv(1024)
            # Transmite a mensagem para todos os clientes
            broadcast(message)
        except:
            # Remove o cliente e o nickname se houver um erro
            index = clients.index(client)
            clients.remove(client)
            client.close()
            nickname = nicknames[index]
            broadcast(f'{nickname} saiu do chat!'.encode('utf-8'))
            nicknames.remove(nickname)
            break

# Função principal para aceitar clientes
def receive():
    while True:
        # Aceita a conexão do cliente
        client, address = server.accept()
        print(f'Conectado com {str(address)}')

        # Solicita o nickname do cliente
        client.send('NICK'.encode('utf-8'))
        nickname = client.recv(1024).decode('utf-8')
        nicknames.append(nickname)
        clients.append(client)

        # Informa que o cliente entrou no chat
        print(f'Nickname do cliente é {nickname}')
        broadcast(f'{nickname} entrou no chat!'.encode('utf-8'))
        client.send('Conectado ao servidor!'.encode('utf-8'))

        # Inicia uma thread para lidar com o cliente
        thread = threading.Thread(target=handle_client, args=(client,))
        thread.start()

print('Servidor está ouvindo...')
receive()