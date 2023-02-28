import random


def jogar():
    print(32 * "*")
    print("Bem-vindo ao jogo de advinhação!")
    print(32 * "*")

    numero_secreto = round(random.randrange(1, 101))
    i = 0
    rodada = 1

    # print(numero_secreto)
    while True:
        try:  # para evitar que o codigo quebre se o user não escrever um numero inteiro
            print("\nQual nível de dificuldade?")
            print("(1) Fácil (2) Médio (3) Díficil")
            nivel = int(input("Defina um nível de dificuldade: "))
            if nivel in [1, 2,
                         3]:  # caso digite um numero que nao esta nessa lista, exibirá msg de erro e retorna pro inicio
                if nivel == 1:
                    i = 20
                elif nivel == 2:
                    i = 10
                elif nivel == 3:
                    i = 5
                break  # caso o numero esteja na lista [1,2,3], break quebrará o loop e seguirá pro proximo bloco
            print("\nVocê precisa escolher o número 1, 2 ou 3 para selecionar a dificuldade!")
        except ValueError:
            print("\nPor favor, escreva um número válido!\n")

    while rodada <= i:  # (1 <= i) o loop termina quando o numero de rodadas for igual a tentativas (ignorando o break)
        try:
            print(f"Tentativa {rodada} de {i}")
            chute = int(input("Digite um número entre 1 e 100: "))
            print("Você digitou ", chute)

            acertou = chute == numero_secreto
            maior = chute > numero_secreto
            menor = chute < numero_secreto

            if chute < 1 or chute > 100:
                print("\nVocê deve digitar um número entre 1 a 100!\n")
                continue  # if True, quebra a continuidade e volta pro inicio do loop, sem incremento da rodada

            if (acertou):
                print("Você acertou!\n")
                break  # esse break quebra o loop e termina o jogo
            else:
                if (maior):
                    print("\nVocê errou, seu chute foi maior que o numero secreto!\n")
                elif (menor):
                    print("\nVocê errou, seu chute foi menor que o numero secreto!\n")
                rodada +=1  # incremento no loop (rodada = rodada +1)
        except ValueError:
            print("\nPor favor, digite um número inteiro entre 1 e 100!\n")

    print(f"FIM DO JOGO!!, o número secreto era {numero_secreto}!!")


if __name__ == "__main__":  # verificar se o arquivo atual está sendo executado como principal ou importado
    jogar()  # nesse caso, se for principal poderá ser executado normalmente
