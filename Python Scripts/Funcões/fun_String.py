def escreva(msg):
    print('-' * (len(msg) + 4))
    print(f'  {msg}')
    print('-' * (len(msg) + 4))
    
# Programa Principal
usuario = str(input('Digite sua mensagem: '))
escreva(f'  {usuario}')
