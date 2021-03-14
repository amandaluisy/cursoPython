import random
def jogar():


    print(30*"*")
    print("     Jogo de Adivinhação")
    print(30*"*")
    numero_secreto = random.randint(1,50)

    tentativa = 0

    pontos = 1000

    print("O jogo é composto por três níveis (1) - Fácil, (2) - Médio e  (3) - Difícil")
    print("No nível 1 você terá 10 tentativas\nNo nível 2 você terá 5 tentativas\nNo nível 3 você terá 3 tentativas\n")
    nivel = int(input("Digite um nivel para o seu jogo:\n"))
    if nivel == 1:
        tentativa = 10
    elif nivel == 2:
        tentativa = 5
    elif nivel == 3:
        tentativa = 3

    print ("Voce escolheu o nível {} e terá {} tentativas" .format(nivel,tentativa))

    for rodada in range(1,tentativa+1):
        print("Rodada {} de {}".format(rodada,tentativa))
        chute = int(input("Digite um numero entre 1 e 50:\n"))
        acertou = chute == numero_secreto
        errou = chute != numero_secreto
        maior = chute > numero_secreto
        menor = chute < numero_secreto
        pontos_perdidos = abs(numero_secreto - chute)
        pontos = pontos - pontos_perdidos
        if acertou:
            print("Parabéns! Você acertou o numero secreto: {}" .format(numero_secreto))
            print("A sua pontuação foi de : {}" .format(pontos))
            break

        elif errou:
            print("Você errou, tente Novamente")
            if maior:
                print("O seu chute : {} é maior que o número secreto".format(chute))
            elif menor:
                print("O seu chute : {} é menor que o número secreto".format(chute))
        if (rodada == tentativa):
            print("Você perdeu! O número secreto era {} .".format(numero_secreto))
    print("Fim do jogo")
if (__name__ == "__main__"):
    jogar()