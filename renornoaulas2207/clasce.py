# class Pessoa:
    
#         nome = "Ivanilson"
#         idade = "35"
    

# pessoa1 = Pessoa()
# print(pessoa1.nome)

# pessoa1.nome = 'Maria'
# print(pessoa1.nome)
class Pessoa:
    def __init__(self,nome, idade, ):
        self.nome = nome
        self.idade = idade
        self.altura = 2
        

    def falar(self, mensagem):
        print(f'{self.nome} diz {mensagem}')
        
    
    
    
    
pessoa1 = Pessoa("joao", 30)
print(pessoa1.nome)
print(pessoa1.idade)
print(pessoa1.altura)