def escreva(msg):
    print('-' * (len(msg) + 4))
    print(f'  {msg}')
    print('-' * (len(msg) + 4))

def voto(ano):
    import time
    atual = time.localtime().tm_year
    idade = atual - ano
    if idade < 16:
        return f'Com {idade} anos: \033[0;32m NÃO VOTA \033[0m'
    elif 16 <= idade < 18 or idade > 65:
        return f'Com {idade} anos: \033[0;33m VOTO OPCIONAL \033[0m'
    else:
        return f'Com {idade} anos: \033[0;31m VOTO OBRIGATORIO \033[0m'

# Programa Principal
nasc = int(input('Em que ano vc nasceu? '))
escreva(voto(nasc))
