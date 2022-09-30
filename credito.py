from math import floor


def main():

    cartao = int(input("Qual o número do cartão de crédito? "))

    #Master Card
    if cartao > 5100000000000000 and cartao < 5600000000000000:

        if algoritmoDeLuhn(cartao) == True:
            print("MASTERCARD")
        else:
            print("INVALID")

    #Visa
    elif cartao < 5000000000000000 and cartao > 4000000000000000 or cartao < 4999999999999 and cartao > 4000000000000:

        if algoritmoDeLuhn(cartao) == True:
            print("VISA")
        else:
            print("INVALID")

    #American Express
    elif cartao > 340000000000000 and cartao < 349999999999999 or cartao > 370000000000000 and cartao < 379999999999999:

        if algoritmoDeLuhn(cartao) == True:
            print("AMEX")
        else:
            print("INVALID")

    else:
        print("INVALID")


def algoritmoDeLuhn (n):

    ni = 1
    nMult = 0
    somaPar = 0
    somaImpar = 0
    somaTotal = 0
#separe número por número
    while n > 0:
        numero = n % 10
        n = floor(n / 10)
        #a partir do penúltimo número pegue os números de 2 em 2 multiple por 2 e some os algarismos
        if ni % 2 == 0:
            nMult = numero * 2
            #se o resultado da multiplicação for maior que 10 separe os algarismos e some eles
            if nMult > 9:
                nc = nMult % 10
                nMult = floor(nMult / 10)
                nMult += nc

            somaPar += nMult
        #a partir do último número pegue os números de 2 em 2 e some os algarismos
        else:
            somaImpar += numero

        ni += 1
    #some tudo, se o último algarismo da soma for 0 o cartão é verdadeiro
    somaTotal = somaPar + somaImpar
    verificacao = somaTotal % 10

    if verificacao == 0:
        return True
    else:
        return False

main()
