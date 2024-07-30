class Viagem:
    def __init__(self, destino):
        
        self.destino = destino
        
Viagem0 = Viagem("Bonito/MS")
Viagem1 = Viagem("foz do iguaçu")
Viagem2 = Viagem("Santa Catarina/SC")
Viagem3 = Viagem("BELO HORIZONTE/ MG")
Viagem4 = Viagem("PANTANAL")


print("bEM-vINDO")
viajante = input("Digite seu nome para começar")
print(f"{viajante} temos 5 destimos que conbina com vc:"
  '''    
[0] bonito
[1] foz do iguaçu
[2] santa catarina
[3] belo horizonte
[4] pantanl
''')

opcao_selecionada = int(input("selecione o numero da viagem desejada"))
lista_viagem =[Viagem0,Viagem1,Viagem2,Viagem3,Viagem4]



    
if opcao_selecionada >= 5:
    print("esta opçao n esta inclusa no nossos destinos")
    
if opcao_selecionada <= 4:
    print(f'{viajante} sua viagem para {lista_viagem[opcao_selecionada].destino}')