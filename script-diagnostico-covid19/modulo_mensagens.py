# Importação do Módulo
import modulo_execucao


# Mensagens da Aplicação
def títulos(msg):
    print('+=' * 40)
    print(f'\033[1:35m{msg:^80}\033[m')
    print('+=' * 40)


def grim60():
    print(f'=> \033[0:31mVocê está com {modulo_execucao.dados["idade"]} anos, portanto, '
          f'está em grupo de risco pela idade.\033[m')


def gri():
    print(f'=> \033[0:32mVocê está com {modulo_execucao.dados["idade"]} anos, portanto, '
          f'não está em grupo de risco pela idade.\033[m')


def msgfumantes():
    print(f'=> \033[0:31mVocê é fumante, isso agrava o seu quadro respiratório!\033[m')


def msgfumanten():
    print(f'=> \033[0:32mVocê não é fumante. Parabéns! Isso pode não agravar seu quadro '
          f'respiratório!\033[m')


def msgdoencass():
    print(f'=> \033[0:31mSeu quadro de doenças pré-existentes que podem agravar o fator '
          f'de risco: \033[m')
    print(f'    => \033[0:31m{modulo_execucao.doenças}\033[m')


def msgdoencasn():
    print(f'=> \033[0:32mVocê não possui quadro prévio, portanto, não terá o '
          f'risco agravado.\033[m')


def msgsintomasgraves():
    print(f'=> \033[1:31mVocê apresenta sérios sintomas que podem indicar Covid-19. \n'
          f'    Procure imediatamente um ponto de atendimento e relate seus sintomas. \n'
          f'    Cuide-se, pois, o seu quadro pode se agravar rapidamente!\033[m')


def msgsintomasleves():
    print(f'=> \033[0:33mVocê apresenta sintomas leves que podem significar a Covid-19. \n'
          f'    Mantenha o isolamento total por 14 dias. \n'
          f'    Se apresentar quadro de febre ou dores no peito, procure o sistema de \n'
          f'    saúde imediatamente relatando os sintomas apresentados.\033[m')


def msgsemsintomas():
    print(f'=> \033[0:32mVocê não possui nenhum sintoma ou pode ser assintomatico. \n'
          f'    Continue sua quarentena e evite sair de casa sem necessidade.\033[m')


def cabeçalhorel():
    print(f'\033[0:32m{modulo_execucao.dados["nome"]}\033[m, segue o relatório baseado '
          f'em suas respostas:')


# Tratamento de Erros
def errodado():
    print(f'\033[0:31m=> Dado inválido, tente novamente!\033[m')


def errogenerico():
    print(f'\033[0:31m=> Houve um erro geral no Sistema!\033[m')
