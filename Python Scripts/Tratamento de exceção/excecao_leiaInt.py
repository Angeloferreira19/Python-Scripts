def leiaInt(msg):
    while True:
        try:
            n = int(input(msg).strip())
        except (ValueError, TypeError):
            print(f'\033[0;31m ERRO! Valor inválido. Digite somente um número inteiro válido.\033[m')
            continue
        except KeyboardInterrupt:
            print('\n\033[0;31m Usuário preferiu não digitar esse número.\033[m')
            return 0
        else:
            return n
        

def leiaFloat(msg, forma=False):
    while True:
        try:
            m = float(input(msg).strip())
        except (ValueError, TypeError):
            print(f'\033[0;31m ERRO! Valor inválido. Digite um número real válido.\033[m')
            if forma is True:
                print(f'\033[0;31m ERRO! Forma inválida. Tente novamente.\033[m')
            continue
        except KeyboardInterrupt:
            print('\n\033[0;31m Usuário preferiu não digitar esse número.\033[m')
            return 0
        else:
            return m


# Programa Principal
n = leiaInt('Digite um número inteiro: ')
m = leiaFloat('Digite um número real: ')
print(f'Você acabou de digitar os números {n} e {m}')
