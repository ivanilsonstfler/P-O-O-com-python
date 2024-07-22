from ast import If


n1 = float(input("Digite a primeira nota: "))
n2 = float(input("Digite a segumda nota: "))
n3 = float(input("Digite a terceira nota: "))
media_exer = float(input("Digite a média dos exercicios: "))

media_aproveitamento = (n1 + n2 * 2 + n3 * 3 + media_exer) / 6

if media_aproveitamento >= 9.0:
    conceito = "A"
elif media_aproveitamento >= 7.5:
    conceito = "B"
elif media_aproveitamento >= 6.0:
    conceito = "C"
else:
    conceito = "D"

print("Média de aproveitamento: ", media_aproveitamento)
print("Conceito: ", conceito)

