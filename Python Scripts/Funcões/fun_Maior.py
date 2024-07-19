from asyncio.windows_events import NULL


def escreva(msg):
    print('-' * (len(msg) + 4))
    print(f'  {msg}')
    print('-' * (len(msg) + 4))

def maior(*num):
    tam = len(num)
    escreva(f'Analisando os valores passados...')
    if tam == 0:
        print('Nenhum valor foi informado.')
    else:
        print(num)
        escreva(f'Recebi {tam} valores.')
        print(f'O maior valor: {max(num)}')
        print(f'O menor valor: {min(num)}')
        print('-' * 20)
    
    
# Programa Principal
maior(2, 3, 7, 19, 20, 50, 92, 0)
maior(4, 7, 9)
maior(1, 2, 3, 4, 5, 6, 7, 8, 9, 10)
maior(0)
maior()