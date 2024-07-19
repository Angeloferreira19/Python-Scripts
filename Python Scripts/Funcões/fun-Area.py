# Função que calcula a área de um terreno
def area(larg, comp):
    area = larg * comp
    print(f'A área de um terreno {c}x{l} é de {area:.2f}m2.')
    
# Programa Principal
print('--' * 20)
print('     CONTROLE DE TERRENO')
print('--' * 20)
c = float(input('Digite o comprimento do terreno: (m)'))
l = float(input('Digite a largura do terreno: (m)'))
print('--' * 20)
area(c, l)