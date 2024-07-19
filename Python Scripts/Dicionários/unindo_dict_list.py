# Unindo dicionarios e listas
pessoa = dict()
galera = list()
soma = 0
while True:
    pessoa['nome'] = str(input('Nome: '))
    while True:
        pessoa['sexo'] = str(input('Sexo [M/F]: ')).upper().strip()[0]
        if pessoa['sexo'] in 'MF':
            break
        print('ERRO! Por favor, digite apenas M ou F.')
    pessoa['idade'] = int(input('Idade: '))
    soma += pessoa['idade']
    galera.append(pessoa.copy())
    while True:
        resp = str(input('Quer continuar? [S/N] ')).upper().strip()[0]
        if resp in 'SN':
            break
        print('ERRO! Por favor, digite apenas S ou N.')
    if resp == 'N':
        break
print('-=-' * 30)
print(f'Ao todo temos {len(galera)} pessoas cadastradas.')
print('--' * 30)
média = soma / len(galera)
print(f'A média de idade é de {média:5.2f} anos.')
print('--' * 30)
print('As mulheres cadastradas foram', end='')
for p in galera:
    if p['sexo'] == 'F':
        print(f'{p['nome']} ', end='')
print()
print('--' * 30)
print('Lista das pessoas que estão acima da média: ')
for p in galera:
    if p['idade'] >= média:
        print('     ', end='')
        for k, v in p.itens():
            print(f'{k} = {v};', end='')
        print()
print('<< ENCERRADO >>')
