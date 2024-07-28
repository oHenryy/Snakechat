import socket
import threading

# Solicita o nickname do usuário
nickname = input("Escolha seu nickname: ")

# Configurações do cliente
HOST = '127.0.0.1'  # Endereço IP do servidor
PORT = 12345        # Porta do servidor

# Inicializa o socket do cliente
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect((HOST, PORT))

# Função para receber mensagens do servidor
def receive():
    while True:
        try:
            # Recebe a mensagem do servidor
            message = client.recv(1024).decode('utf-8')
            if message == 'NICK':
                client.send(nickname.encode('utf-8'))
            else:
                print(message)
        except:
            # Fecha o cliente em caso de erro
            print("Ocorreu um erro!")
            client.close()
            break

# Função para enviar mensagens para o servidor
def write():
    while True:
        message = f'{nickname}: {input("")}'
        client.send(message.encode('utf-8'))

# Inicia threads para enviar e receber mensagens
receive_thread = threading.Thread(target=receive)
receive_thread.start()

write_thread = threading.Thread(target=write)
write_thread.start()
