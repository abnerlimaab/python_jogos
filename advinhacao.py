import random

def jogar():
    print("===============================")
    print("Bem-vindo ao jogo da advinhação")
    print("===============================")

    numero_secreto = random.randrange(1, 101)
    total_de_tentativas = 0
    pontos = 1000

    print("Qual o nível de dificuldade?")
    nivel_dificuldade = int(input("(1) Fácil - (2) Médio - (3) Difícil"))

    if (nivel_dificuldade == 1):
        total_de_tentativas = 5
    elif (nivel_dificuldade == 2):
        total_de_tentativas = 10
    else:
        total_de_tentativas = 20

    for rodada in range(1, total_de_tentativas + 1):
        print("Tentativa {} de {}".format(rodada, total_de_tentativas))
        chute = int(input("Digite um número entre 1 e 100:"))

        print("Você digitou ", chute)

        if (chute < 1 or chute > 100):
            print("Voce deve digitar um número entre 1 e 100")
            continue

        acertou = numero_secreto == chute
        maior = chute > numero_secreto
        menor = chute < numero_secreto

        if (acertou):
            print("Você acertou! Sua pontuação é {}".format(pontos))
            break
        else:
            if(maior):
                print("Seu chute foi maior que o número secreto")
            elif(menor):
                print("Seu chute foi menor que o número secreto")

        pontos = pontos - abs(numero_secreto - chute)

    print("Fim do jogo!")

if (__name__ == "__main__"):
    jogar()