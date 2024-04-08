# . Uma empresa quer verificar se um empregado está qualificado para a aposentadoria
# ou não. Para estar em condições, um dos seguintes requisitos deve ser saƟsfeito:
# - Ter no mínimo 65 anos de idade.
# - Ter trabalhado no mínimo 30 anos.
# - Ter no mínimo 60 anos e ter trabalhado no mínimo 25 anos. 
idade = int(input("Digite sua idade: "))

anos_trabalho = int(input("Digite anos de Trabalho: "))

if idade >= 65 or anos_trabalho >= 30:
    print("Você está apto a se aposentar")

elif idade >= 60 or anos_trabalho >= 25:
    print("Você está apto a se aposentar")

else:
    print("Não se encaixa nos requisitos, não pode se aposentar.")