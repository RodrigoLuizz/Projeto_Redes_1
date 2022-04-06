#!/usr/bin/env python3
#coding: 'utf-8'

import socket as sc


class Cliente:
    '''Clinte que se conectara com o servidor.'''
    
    def __init__(self, HOST, PORT):
        self.host = HOST # IP do Servidor que deseja-se se conectar.. 
        self.port = PORT # Porta usada para conectar-se ao servidor.


    def _conncetion(self):
        """Estabelecer a conexão com o Servidor."""
        client = sc.socket(sc.AF_INET, sc.SOCK_STREAM)
        client.connect((self.host, self.port))
        return client 


    def download_file(self):
        """Faz o download de um arquivo especificado no servidor."""
        cliente = self._conncetion()
        name_file = str(input('Arquivo desejado>>'))
        cliente.send(name_file.encode()) # Pegar o arquivo do servidor.
        # Recebendo o arquivo.
        with open(name_file, 'wb') as file:
            while True:
                data = cliente.recv(1000000)
                if not data: # Verificando se ainda existe dados para serem enviados.
                    break
                file.write(data)
        print("Arquivo recebido, cheque a sua pasta!")


clinte = Cliente('127.0.0.1', 4040)
clinte.download_file()