# importacao das bibliotecas
from socket import * # sockets

# definicao das variaveis
serverName = 'localhost' # ip do servidor a se conectar
serverPort = 61020 # porta a se conectar
clientSocket = socket(AF_INET, SOCK_DGRAM) # criacao do socket UDP

message = input('Solicite a data: ')
clientSocket.sendto(message.encode('utf-8'),(serverName, serverPort)) # envia mensagem para o servidor
data, serverAddress = clientSocket.recvfrom(2048) # recebe do servidor a resposta
print ('O servidor (\'%s\', %d) acaba de responder!\n%s' % (serverName, serverPort, data.decode('utf-8'))) # Exibe resposta
clientSocket.close() # encerra o socket do cliente
input('Press ENTER to exit')

