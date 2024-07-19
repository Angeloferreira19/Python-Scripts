# Cadastro de Trabalhador CLT
import time
clt = dict()
nome = str(input('Nome: '))
ano = int(input('Ano de Nascimento: '))
ctps = int(input('Carteira de Trabalho (0 não tem): '))
clt['nome'] = nome
clt['ano'] = ano
clt['ctps'] = ctps
if ctps != 0:
    clt['contratacao'] = int(input('Ano de Contratação: '))
    clt['salario'] = float(input('Salário: R$'))
    clt['aposentadoria'] = (clt['contratacao'] + 35) - (time.localtime().tm_year - clt['ano'])
print('--' * 20)
for k, v in clt.items():
    print(f'{k} = {v}')
print('--' * 20)
