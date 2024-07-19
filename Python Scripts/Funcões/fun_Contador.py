from time import sleep

def contador(i, f, p):
    if p < 0:
        p *= -1
    if p == 0:
        p = 1
    print('--' * 20)
    print(f'Contagem de {i} a {f} de {p} em {p}')
    sleep(1.5)
    
    if i < f:
        cont = i
        while cont <= f:
            print(f'{cont} ', end='', flush=True)
            sleep(0.5)
            cont += p
        print('FIM!')
    else:
        cont = i
        while cont >= f:
            print(f'{cont} ', end='', flush=True)
            sleep(0.5)
            cont -= p
        print('FIM!')
        
# Programa Principal
contador(1, 10, 1)
contador(10, 0, -2)
print('--' * 20)
print('Sua vez de personalizar a contagem: ')
ini = int(input('Inicio: '))
fim = int(input('fim: '))
pas = int(input('Passo: '))
contador(ini, fim, pas)