from socket import * # sockets
import time

# definicao das variaveis
serverName = '' # ip do servidor (em branco)
serverPort = 61020 # porta a se conectar
serverSocket = socket(AF_INET, SOCK_DGRAM) # criacao do socket UDP
serverSocket.bind((serverName, serverPort)) # bind do ip do servidor com a porta
print ('Servidor UDP esperando conexoes na porta %d ...' % (serverPort))
while 1:
    message, clientAddress = serverSocket.recvfrom(2048) # recebe do cliente
    message = message.decode('utf-8')
    if message=="data":# Reconhece a validade do comando
        print('Comando data!')
        data = "Data e hora: "+str(time.ctime())
        serverSocket.sendto((data).encode('utf-8'), clientAddress) # Envia resposta
    if message != "data":# Reconhece a validade do comando
        print('Comando invalido!')
        serverSocket.sendto('Comando invalido!'.encode('utf-8'), clientAddress) # Informa caso o comando seja invalido
serverSocket.close() # encerra o socket do servidor
