#!/usr/bin/env python3
#coding:'utf-8'

import socket as sc

class Server:
    
    '''Servidor de tranferencia de Arquivo.'''

    def __init__(self, HOST, PORT): # Inicializador da classe. 
        self.host = HOST # IP do Servidor. 
        self.port = PORT # Porta de conexão do servidor.


    def _run_server(self):
        """Subir o servidor."""
        server = sc.socket(sc.AF_INET, sc.SOCK_STREAM) # Criando o objeto Socket
        server.bind((self.host, self.port)) # Abrindo a conexão
        server.listen() # Numero de conexoes
        print('CONECTADO!')
        connection, addres = server.accept()

        return connection, addres


    def transfer_file(self):
         """Tranferir arquivos para o clinte."""
         connection, addres = self._run_server()
         name_file = connection.recv(1024).decode() # Receber o nome do arquivo desejado. 

         with open(name_file, 'rb') as file:
             for data in file.readlines(): # Ler o arquivo e enviar para o cliente. 
                 connection.send(data) # Enviando o dado para o clinte
             print('Arquivo enviado!')



server = Server('127.0.0.1', 4040)
server.transfer_file()