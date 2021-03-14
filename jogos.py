import Adivinhacao1
import forca
print("Selecione o jogo desejado"),
print("Digite 1 jogo de adivinhação\nDigite 2 jogo da forca")
jogo = int(input("Qual você deseja jogar?\n"))
if jogo == 1:
    Adivinhacao1.jogar()
elif jogo == 2:
    forca.jogar()
