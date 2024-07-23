class Viagem:
    def __init__(self, destino):
        self.destino = destino
        
    def exibir_info(self):
        return f"Destino: {self.destino}"
        
Viagem0 = Viagem("Bonito/MS")
Viagem1 = Viagem("Foz do Iguaçu")
Viagem2 = Viagem("Santa Catarina/SC")
Viagem3 = Viagem("Belo Horizonte/MG")
Viagem4 = Viagem("Pantanal")

print("BEM-VINDO")

viajante = input("Digite seu nome para começar: ")
print(f"{viajante}, temos 5 destinos que combinam com você:")
print("[0] Bonito")
print("[1] Foz do Iguaçu")
print("[2] Santa Catarina")
print("[3] Belo Horizonte")
print("[4] Pantanal")

opcao_selecionada = int(input("Selecione o número da viagem desejada: "))
lista_viagem = [Viagem0, Viagem1, Viagem2, Viagem3, Viagem4]

if 0 <= opcao_selecionada < 5:
    print(f"{viajante}, sua viagem será para {lista_viagem[opcao_selecionada].exibir_info()}.")
else:
    print("Essa opção não está inclusa nos nossos destinos!")
