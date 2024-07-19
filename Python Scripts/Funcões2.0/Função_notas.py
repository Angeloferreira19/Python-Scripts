def notas(*num, sit=False):
    """_summary_
    Função de calculo de notas
    Args:
        sit (bool, optional): Situação da turma. Defaults to False.
        r (dict, optional): Retorna um dicionário. Defaults to {}.
    """
    r = dict()
    r['total'] = len(num)
    r['maior'] = max(num)
    r['menor'] = min(num)
    r['media'] = sum(num) / len(num)
    if sit:
        if r['media'] < 6:
            print('A Situação é RUIM!')
        elif 6 <= r['media'] < 7:
            print('A Situação é RASOÁVEL!')
        else:
            print('A Situação é BOA!')
    return r

# Programa Principal
resp = notas(4.5, 7, 10, 8.5, sit=True)
print(resp)
help(notas)
