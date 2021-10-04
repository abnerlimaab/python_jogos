print("===============================")
print("Bem-vindo ao jogo da advinhação")
print("===============================")

numero_secreto = 42

chute = int(input("Digite seu número: "))

print("Você digitou ", chute)

acertou = numero_secreto == chute
maior = chute > numero_secreto
menor = chute < numero_secreto

if (acertou):
    print("Você acertou!")
else:
    if(maior):
        print("Seu chute foi maior que o número secreto")
    elif(menor):
        print("Seu chute foi menor que o número secreto")