#!/bin/python3
import sys
from time import sleep

try:
	import mysql.connector
except:
	print('''Você precisa do modulo mysql_connector instalado, no README.md tem todos os passos necessários para
		a instalação deste modulo.''')
	print('='*30)
	pritn("O script irá encerrar em 3 segundos. Bye!!")
	sleep(3)
	sys.exit(1)



def Conection():

	try:
		mydb = mysql.connector.connect(
		  host="sql10.freesqldatabase.com",
		  database='sql10424407',
		  user="sql10424407",
		  password="xCmgJsLGDP"
		)		
	
	except Exception as e:
            print(f'Erro ao conectar ao banco de dados -> {e}')
            return False
	else:
		return True, mydb


def Criar_tabelas():
	if Conection():
		try:
			response, mysql = Conection()
			cursor = mysql.cursor()
			cursor.execute('''CREATE TABLE dados (id INT(11) NOT NULL AUTO_INCREMENT PRIMARY KEY,nome VARCHAR(255), idade VARCHAR(255), fumante CHAR(1), resultado VARCHAR(255));''')
			print('Tabela Criada com Sucesso!')
		except Exception as e:
			print(f'Error -> {e}')
		finally:
			cursor.close()
	else:
		print("Error ao conectar")



def Gravar_dados(nome,idade,fumante,resultado):

	query = '''INSERT INTO dados (nome, idade,fumante,resultado) VALUES (%s, %s, %s, %s)'''
	values = (nome, idade, fumante, resultado)
	if Conection():
		response,mysql = Conection()
		cursor = mysql.cursor()
		try:
			cursor.execute(query, values)
			mysql.commit()
			print("Dados gravados com sucesso!!")
		except Exception as e:
			print(f"Erro ao gravar dados -> {e}")
		finally:
			cursor.close()


