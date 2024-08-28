# Snakechat
Este é um simples projeto de chat implementado em Python, que utiliza sockets e threading para permitir a comunicação em tempo real entre clientes conectados a um servidor. O projeto é composto por dois scripts principais: server.py e client.py.

## Funcionalidades

  - server.py: Configura e executa o servidor de chat que aceita conexões de vários clientes, gerencia os clientes conectados e retransmite as mensagens enviadas por qualquer cliente para todos os outros conectados.
  - client.py: Configura o cliente de chat que se conecta ao servidor, permitindo que um usuário envie e receba mensagens em tempo real.

## Requisitos

  - Python 3.x

## Execução

  1. **Clonar o Repositório**
     
     git clone https://github.com/oHenryy/Snakechat.git
    
  3. **Executar o Servidor**

     Inicie o servidor em uma janela de terminal:
     ```
     python server.py
     ```

  4. **Executar o Cliente**

     Em uma nova janela de terminal, execute o cliente:
     ```
     python client.py
     ```
     O cliente solicitará um nickname e, em seguida, permitirá que o usuário envie mensagens que serão transmitidas para todos os outros clientes conectados.

## Conceituando

`server.py`:

    - **Host e Porta:** O servidor é configurado para escutar em 127.0.0.1 na porta 12345.
    - **Gerenciamento de Conexões:** O servidor aceita conexões de clientes e mantém uma lista dos clientes e seus respectivos nicknames.
    - **Broadcast de Mensagens:** As mensagens recebidas de um cliente são retransmitidas para todos os outros clientes conectados.
    - **Gerenciamento de Erros:** Caso ocorra um erro durante a comunicação com um cliente, ele é removido da lista de clientes, e uma mensagem é enviada aos demais informando sua saída.

`client.py`:

    - **Conexão ao Servidor:** O cliente se conecta ao servidor utilizando o endereço IP 127.0.0.1 e a porta 12345.
    - **Envio e Recebimento de Mensagens:** O cliente tem duas threads: uma para receber mensagens do servidor e outra para enviar mensagens.
    - **Nickname:** Cada cliente escolhe um nickname ao conectar-se ao servidor, que é exibido junto às mensagens enviadas.
