# importacao das bibliotecas
from socket import * # sockets
import subprocess

# definicao das variaveis
serverName = '' # ip do servidor (em branco)
serverPort = 61000 # porta a se conectar
serverSocket = socket(AF_INET,SOCK_STREAM) # criacao do socket TCP
serverSocket.bind((serverName,serverPort)) # bind do ip do servidor com a porta
serverSocket.listen(1) # socket pronto para 'ouvir' conexoes
print ('Servidor TCP esperando conexoes na porta %d ...' % (serverPort))
while 1:
  connectionSocket, addr = serverSocket.accept() # aceita as conexoes dos clientes
  mensagem = connectionSocket.recv(1024) # Recebe o comando do cliente
  mensagem = mensagem.decode('utf-8')
  print('Recebeu comando: ', mensagem)
  resposta = subprocess.check_output(mensagem, shell=True, universal_newlines=True,stderr=subprocess.STDOUT) # Executa o comando
  connectionSocket.send(resposta.encode('utf-8')) # Retorna uma resposta para o cliente se necessario
  connectionSocket.close() # encerra o socket com o cliente

serverSocket.close() # encerra o socket do servidor