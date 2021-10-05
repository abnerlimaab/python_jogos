print("===============================")
print("Bem-vindo ao jogo da advinhação")
print("===============================")

numero_secreto = 42
total_de_tentativas = 3
rodada = 1

while(rodada <= total_de_tentativas):
    print("Tentativa {} de {}".format(rodada, total_de_tentativas))
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

    rodada = rodada + 1

print("Fim do jogo!")