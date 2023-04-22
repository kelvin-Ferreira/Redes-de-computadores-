# importacao das bibliotecas
from socket import * 
import subprocess

# definicao das variaveis
serverName = 'localhost' # ip do servidor
serverPort = 61000 # porta a se conectar
clientSocket = socket(AF_INET,SOCK_STREAM) # criacao do socket TCP
clientSocket.connect((serverName, serverPort)) # conecta o socket ao servidor

sentence = input('Digite o comando desejado: ')
clientSocket.send(sentence.encode('utf-8')) # envia o comando para o servidor
resposta = clientSocket.recv(1024) # recebe do servidor a resposta
resposta = resposta
print('Comando executato!\n', resposta)
clientSocket.close() # encerramento o socket do cliente
input('Press ENTER to exit')
