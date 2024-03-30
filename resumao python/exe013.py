# Ler 3 valores (A, B e C) representando as medidas dos lados de um triângulo e
# escrever se formam ou não um triângulo. OBS: para formar um triângulo, o valor de
# cada lado deve ser menor que a soma dos outros 2 lados. 
valor_A = float(input("Digite o valor A: "))
valor_B = float(input("Diggite o valor B: "))
vallor_C = float(input("Digite o valor C: "))
if valor_A < valor_B + vallor_C and valor_B <valor_A + vallor_C and  valor_A + valor_B:
 
    print("Os valores formam um triangulo.")
else:
    print("Os valores não formam um triangulo.")