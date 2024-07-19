def escreva(msg):
    print('-' * (len(msg) + 4))
    print(f'  {msg}')
    print('-' * (len(msg) + 4))

def sorteio(lista):
    from random import randint
    from time import sleep
    escreva('SORTEANDO VALORES...')
    for c in range(0, 5):
        n = randint(0, 10)
        lista.append(n)
    escreva('Os valores sorteados são:')
    print(f'{lista} ', end='', flush=True)
    sleep(0.3)
    print('PRONTO!')
    

def somaPar(lista):
    soma = 0
    for valor in lista:
        if valor % 2 == 0:
            soma += valor
    escreva(f'A soma dos valores pares de {lista} é {soma}')
    
# Programa Principal
numeros = list()
sorteio(numeros)
somaPar(numeros)
