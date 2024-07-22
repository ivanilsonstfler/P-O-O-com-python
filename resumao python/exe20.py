# Faça um algoritmo/programa para ler um número que é um código de usuário. Caso
# este código seja diferente de um código armazenado internamente no algoritmo
# (igual a 1234) deve ser apresentada a mensagem ‘Usuário inválido!’. Caso o Código
# seja correto, deve ser apresentado outro valor que é a senha. Se esta senha esƟver
# incorreta (a certa é 9999) deve ser mostrada a mensagem ‘senha incorreta’. Caso a
# senha esteja correta, deve ser mostrada a mensagem ‘Acesso permiƟdo’.

codigoUsuario = int(input("Digite o codigo do usuario: "))

if codigoUsuario != 1234:
    print("Usuario Invalido!")
else:
    senha = int(input("Digite a senha: "))

if senha != 9999:
        print("Senha Incorreta")
else:
        print("Acesso Permitido")
