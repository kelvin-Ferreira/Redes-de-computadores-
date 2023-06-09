# UNIVERSIDADE FEDERAL DO RIO GRANDE DO NORTE
# DEPARTAMENTO DE ENGENHARIA DE COMPUTACAO E AUTOMACAO
# DISCIPLINA REDES DE COMPUTADORES (DCA0113)
# AUTOR: PROF. CARLOS M D VIEGAS (viegas 'at' dca.ufrn.br)
#
# SCRIPT: Base de um servidor HTTP (python 3)
#

# importacao das bibliotecas
import socket
import os

# definicao do host e da porta do servidor
HOST = '' # ip do servidor (em branco)
PORT = 8080 # porta do servidor

# cria o socket com IPv4 (AF_INET) usando TCP (SOCK_STREAM)
listen_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# permite que seja possivel reusar o endereco e porta do servidor caso seja encerrado incorretamente
listen_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

# vincula o socket com a porta (faz o "bind" do IP do servidor com a porta)
listen_socket.bind((HOST, PORT))

# "escuta" pedidos na porta do socket do servidor
listen_socket.listen(1)

# imprime que o servidor esta pronto para receber conexoes
print ('Serving HTTP on port %s ...' % PORT)

while True:
    # aguarda por novas conexoes
    client_connection, client_address = listen_socket.accept()
    # o metodo .recv recebe os dados enviados por um cliente atraves do socket
    request = client_connection.recv(1024)
    # imprime na tela o que o cliente enviou ao servidor
    print (request.decode('utf-8'))
    str = request.decode('utf-8').split()
    caminho = os.path.dirname(os.path.abspath(__file__))
 
    if str[0] == 'GET':
        if str[1] == '/' :
            resp = open(caminho + "/index.html","r")
            http_response = "HTTP/1.1 200 OK\r\n\r\n" + resp.read()
        else:

            if os.path.isfile(caminho + str[1]) == True: 
                resp = open(caminho + str[1],"r")
                http_response = "HTTP/1.1 200 OK\r\n\r\n" + resp.read()
            else:
                resp = open(caminho + "/Error404.html","r")
                http_response = "HTTP/1.1 404 Not Found\r\n\r\n" + resp.read()
    else:
        resp = open(caminho + "/Error400.html","r")
        http_response = "HTTP/1.1 400 Bad Request\r\n\r\n" + resp.read()

    client_connection.send(http_response.encode('utf-8'))
    # encerra a conexao
    client_connection.close()

# encerra o socket do servidor
listen_socket.close()
