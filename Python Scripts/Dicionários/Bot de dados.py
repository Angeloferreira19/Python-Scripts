# Bot de rolagem de dados
from random import randint
from time import sleep
from operator import itemgetter
Player = int(input('Digite o número de players: '))
dado = int(input('Qual o dado que devo rolar: D'))
jogo = dict()
ranking = list()
print('--' * 20)
print('Vamos Jogar!')
for c in range(0, Player):
    jogo[f'Jogador {c + 1}'] = randint(1, dado)
    sleep(1)
print('--' * 20)
print('Valores sorteados:')
for k, v in jogo.items():
    print(f'{k} tirou {v} no dado.')
    sleep(1)
print('--' * 20)
ranking = sorted(jogo.items(), key=itemgetter(1), reverse=True)
print('Ranking dos jogadores:')
for i, v in enumerate(ranking):
    print(f'{i + 1}º lugar: {v[0]} com {v[1]}')
    sleep(1)
print('--' * 20)
print(f'Parabéns {ranking[0][0]}!\n Você Venceu!')
print('FIM!!')
