import random
#criar um try para input de numero ou mais de uma letra
# criar os desenhos
def apresentacao():

    print(32 * "*")
    print("** Bemvindo ao jogo da forca! **")
    print(32 * "*")

def escolher_palavra_secreta():

    arquivo = open("palavras.txt")
    palavras = []

    for linha in arquivo:
        linha = linha.strip()
        palavras.append(linha)

    arquivo.close()

    numero = random.randrange(0, len(palavras))
    palavra_secreta = palavras[numero].upper()
    return palavra_secreta

def jogar():

    apresentacao()

    palavra_secreta = escolher_palavra_secreta()

    letras_acertadas = ["_" for letra in palavra_secreta]
    print(letras_acertadas)

    enforcou = False
    acertou = False
    tentativa = 0

    # os valores acima precisam ser falsos pois o jogo ainda não começou, quando um dos valores for True o jogo termina.
    while not enforcou and not acertou: # enquanto o user NÃO 'enforcar' e NÃO 'acertar', o loop continua
    # a lógica do loop 'while not' é que ele só vai ser interrompido quando a condição se tornar verdadeira
        chute = input("Qual letra? ")
        chute = chute.strip().upper() #limpar o input e deixar em maiusculo

        if chute in palavra_secreta:
            index = 0
            for letra in palavra_secreta:
                if chute == letra: #vai verificar se o chute é uma letra da palavra secreta
                    letras_acertadas[index] = letra #quando acertar a letra irá atualizar a posição na lista
                index += 1 #index+1 serve para iterar por todas as letras da lista e posicionar corretamente as letras

        else:
            tentativa += 1 # i = i +1
            print(f"Você errou a letra, ainda tem {6 - tentativa} tentativas")
        enforcou = tentativa == 6 # controle da saída do loop
        acertou = ("_") not in letras_acertadas # enquanto nao for true nao sai
        print(letras_acertadas)

    if acertou:
        print("Parabéns, você ganhou o jogo!")
    else:
        print("Você perdeu!")

if __name__ == "__main__":
    jogar()
