class Pessoa:
    def __init__(self, nome: str, idade: int, sexo: str):
        self.nome = nome
        self.idade = idade
        self.sexo = sexo
    
    
    def dizerOlá(self):
        self.escrever(f'Olá meu nome é {self.nome} e tenho {self.idade} anos.')
        if self.sexo == 'M':
            self.escrever(f'Sou do sexo masculino.')
        else:
            self.escrever(f'Sou do sexo feminino.')
    
    
    def cozinhar(self, receita: str):
        self.escrever(f'Estou cozinhando {receita}!')
    
    
    def andar(self, distancia: float):
        self.escrever(f'Saí, só volto quando andar {distancia} metros.')
    
    
    def escrever(self, msg: str):
        print('-' * (len(msg) + 4))
        print(f'  {msg}')
        print('-' * (len(msg) + 4))
        