import advinhacao
import forca

print()
print(32 * "*")
print("*******Escolha seu jogo!********")
print(32 * "*")
print()

print("(1) Advinhação (2) Forca")
escolha = int(input("Escolha seu jogo: "))


if escolha == 1:
    print("Você escolheu Advinhação!")
    advinhacao.jogar()
elif escolha == 2:
    print("Você escolheu Forca!")
    forca.jogar()


