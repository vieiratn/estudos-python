#!/usr/bin/python3

# Importação do Módulo
import modulo_execucao
import modulo_mensagens

# Programa Principal
try:
    modulo_mensagens.títulos('SISTEMA DE AJUDA NO DIAGNÓSTICO DA COVID-19')
    modulo_execucao.dadospessoais()
    modulo_mensagens.títulos(f'DOENÇAS PRÉ-EXISTENTES')
    modulo_execucao.dadosdoenças()
    modulo_mensagens.títulos(f'SINTOMAS APRESENTADOS')
    modulo_execucao.dadossintomas()

except Exception as erro:
    modulo_mensagens.errogenerico()
    modulo_execucao.log_erro(erro)

else:
    modulo_mensagens.títulos(f'RELATÓRIO DOS DADOS INFORMADOS')
    modulo_mensagens.cabeçalhorel()
    modulo_execucao.análise1()
    modulo_execucao.análise2()
    modulo_execucao.análise3()

# Mensagens Personalizadas ao Final do Script
finally:
    modulo_mensagens.títulos('FIQUE EM CASA, NÓS VAMOS SUPERAR!')
    modulo_mensagens.títulos('LAVE AS MÃOS, USE MÁSCARA E EVITE SAIR DE CASA!')
    modulo_mensagens.títulos('OBRIGADO POR UTILIZAR O SISTEMA!')
