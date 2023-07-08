def palindromo(palavra):
    palavra = palavra.lower()
    palavra_reversa = palavra[::-1]

    return palavra == palavra_reversa

palavra = str(input("Digite a palavra: "))

if palindromo(palavra):
    print("A palavra é um palíndromo!")
else:
    print("A palavra NÃO é um palíndromo!")
