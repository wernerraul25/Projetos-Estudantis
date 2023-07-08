palavra = str(input("Digite a palavra: "))
contador = 0

for letra in palavra:
    if letra == 'a' or letra == 'e' or letra == 'i' or letra == 'o' or letra == 'u':
        contador = contador + 1

print("A palavra tem", contador ,"vogal(is)")