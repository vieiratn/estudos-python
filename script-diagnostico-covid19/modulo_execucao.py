
import string
# Importação da Biblioteca de Mensagens
import modulo_mensagens
from conexao_db import Gravar_dados

# Dicionário e Listas (Informações dos Pacientes)
dados = dict()
doenças = list()


# Coleta de Dados e Inserção em Dicionário e Lista
def dadospessoais():

    while True:
        try:
            nome = input('Informe seu Nome: ').upper()
            if not any(chr.isdigit() for chr in nome) and not any(chr in string.punctuation for chr in nome):
                dados['nome']=nome
            else:                
                continue
            idade = int(input(f"{nome}, informe a sua idade: "))
            if idade >0 and idade < 120:
                dados['idade']=idade
            else:                
                continue
            fumante = input(f'{nome}, você é fumante? [s/n]: ').upper()
            if fumante in 'SN' and fumante != '':
                dados['fumante']=fumante
                break
            else:
                continue
        except Exception as e:
            print(e)

 

def dadosdoenças():
    while True:
        dados['hipertensão'] = str(input(f'A) Você é hipertenso(a) [s/n]: ')).strip().upper()[0]
        if dados['hipertensão'] in 'SN':
            break
        else:
            modulo_mensagens.errodado()
    while True:
        dados['asma'] = str(input(f'B) Você é asmático(a) [s/n]: ')).strip().upper()[0]
        if dados['asma'] in 'SN':
            break
        else:
            modulo_mensagens.errodado()
    while True:
        dados['diabetes'] = str(input(f'C) Você é diabético(a) [s/n]: ')).strip().upper()[0]
        if dados['diabetes'] in 'SN':
            break
        else:
            modulo_mensagens.errodado()


def dadossintomas():
    while True:
        dados['tosse'] = str(input(f'A) Você está com tosse seca? [s/n]: ')).strip().upper()[0]
        if dados['tosse'] in 'SN':
            break
        else:
            modulo_mensagens.errodado()
    while True:
        dados['cansaço'] = str(input(f'B) Você está com cansaço excessivo? [s/n]: ')).strip().upper()[0]
        if dados['cansaço'] in 'SN':
            break
        else:
            modulo_mensagens.errodado()
    while True:
        dados['febre'] = str(input(f'C) Você está com febre persistente? [s/n]: ')).strip().upper()[0]
        if dados['febre'] in 'SN':
            break
        else:
            modulo_mensagens.errodado()
    while True:
        dados['respiração'] = str(input(f'D) Você está com dificuldade de respirar? [s/n]: ')).strip().upper()[0]
        if dados['respiração'] in 'SN':
            break
        else:
            modulo_mensagens.errodado()


# Análise de Dados para Relatório
def análise1():
    if dados['idade'] >= 60:
        modulo_mensagens.grim60()
        if dados['fumante'] == 'S':
            print(modulo_mensagens.msgfumantes())
        else:
            print(modulo_mensagens.msgfumanten())
    else:
        modulo_mensagens.gri()
        if dados['fumante'] == 'S':
            print(modulo_mensagens.msgfumantes())
        else:
            print(modulo_mensagens.msgfumanten())


def análise2():
    if dados['hipertensão'] == 'S':
        doenças.append(str('HIPERTENSÃO'))
    if dados['asma'] == 'S':
        doenças.append(str('ASMA'))
    if dados['diabetes'] == 'S':
        doenças.append(str('DIABETES'))
    if doenças == []:
        print(modulo_mensagens.msgdoencasn())
    else:
        print(modulo_mensagens.msgdoencass())


def análise3():
    sintomasgraves = 0
    if dados['febre'] == 'S':
        sintomasgraves += 1
    if dados['respiração'] == 'S':
        sintomasgraves += 1
    if sintomasgraves == 1 or sintomasgraves == 2:
        msg = modulo_mensagens.msgsintomasgraves()
        print(msg)
        Gravar_dados(dados['nome'], dados['idade'], dados['fumante'], msg)

    if dados['febre'] == 'N' and dados['respiração'] == 'N':
        sintomasleves = 0
        if dados['tosse'] == 'S':
            sintomasleves += 1
        if dados['cansaço'] == 'S':
            sintomasleves += 1
        if sintomasleves == 0:
            msg = modulo_mensagens.msgsemsintomas()
            print(msg)
            Gravar_dados(dados['nome'], dados['idade'], dados['fumante'], msg)
                
        if sintomasleves == 1 or sintomasleves == 2:
            msg = modulo_mensagens.msgsintomasleves()
            print(msg)
            Gravar_dados(dados['nome'], dados['idade'], dados['fumante'], msg)
         


def log_erro(msg):
    with open('log_erro.txt', 'a+') as file:
        file.write(f'{msg}\n')
