def fatorial(num, show=False):
    """
    Calcula o fatorial de um número

    Args:
        num (int): Param para o fatorial
        show (bool, optional): Param para mostrar o calculo. Defaults to False.

    Returns:
        Retorna o fatorial de um número para f
    """
    f = 1
    for c in range(num, 0, -1):
        if show:
            print(c, end='')
            if c > 1:
                print(' x ', end='')
            else:
                print(' = ', end='')
        f *= c
    return f

# Programa Principal
n = int(input('Digite um número para fatorar: '))
i = str(input('Deseja mostrar o calculo do fatorial? [S/N] ')).strip().upper()[0]
if i == 'S':
    print(f'{n}! = {fatorial(n, show=True)}')
else:
    print(f'{n}! = {fatorial(n)}')
help(fatorial)
