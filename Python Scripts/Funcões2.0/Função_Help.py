# Manual do Interactive Python
from time import sleep
c = ('\033[0;41m', '\033[0;44m', # 0 - vermelho, 1 - azul
     '\033[0;42m', '\033[0;45m', # 2 - verde, 3 - roxo
     '\033[0;43m', '\033[7;40m', # 4 - amarelo, 5 - branco
     '\033[m')                   # 6 - sem cor
def ajuda(com):
    titulo(f'Acessando o manual do comando \'{com}\'', 4)
    print(c[6], end='')
    print(c[5], end='')
    help(com)
    print(c[6], end='')
    sleep(2)
    
def titulo(msg, cor=6):
    tam = len(msg) + 4
    print(c[cor], end='')
    print('-' * tam)
    print(f'  {msg}  ')
    print('-' * tam)
    print(c[6], end='')
    sleep(1)

# Programa Principal
comando = ''
while True:
    titulo('SISTEMA DE AJUDA PyHELP', 2)
    comando = str(input('Função ou Biblioteca > '))
    if comando.upper() == 'FIM':
        break
    else:
        ajuda(comando)
titulo('ATÉ LOGO!', 1)
