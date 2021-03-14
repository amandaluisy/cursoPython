def jogar():
    print(25*"*")
    print("Bem vindo ao jogo da forca")
    print(25*"*")
    print("O jogo tem 3 niveis\n 1 - Facil, 2 - Médio, 3 - Dificil")
    nivel = int(input("Selecione um nível:"))
    if nivel == 1:
        print("nivel 1")

if (__name__ == "__main__"):
    jogar()