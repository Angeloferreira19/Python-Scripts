def leiaInt(msg):
    ok = False
    valor = 0
    while True:
        n = str(input(msg))
        if n.isnumeric():
            valor = int(n)
            ok = True
        else:
            print('\033[0;31m ERRO! Digite somente um número inteiro. \033[m')
        if ok:
            break
    return valor

# Programa Principal
print('-' * 20)
n = leiaInt('Digite um número: ')
print('-' * 20)
print(f'Você acabou de digitar o número {n}')
