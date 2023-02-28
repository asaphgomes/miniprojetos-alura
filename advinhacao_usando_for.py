import random

numero = 23
rodada = 1
tentativa = 3

for rodada in range(1, rodada +3):
    print(f"Tentativa {rodada} de {tentativa}")
    chute = int(input("Digite um numero: "))
    print("Você digitou ", chute)

    acertou = chute == numero
    menor = chute < numero
    maior = chute > numero

    if acertou:
        print("Parabéns, você acertou!")
        break
    elif menor:
        print("Puts, você errou, é um numero maior que esse!")
    elif maior:
        print("Puts, você errou, é um numero menor que esse!")

print("Fim do jogo!!")