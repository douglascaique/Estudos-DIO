# numeros = set([1, 2, 3, 1, 3, 4])
# print(numeros)

# letras = set('abacaxi')
# print(letras)

# carros = set(('gol', 'palio', 'celta', 'palio'))
# print(carros)

# linguagens = {'python', 'java', 'python', 'c#'}
# print(linguagens)

# numeros = {1, 2, 3, 2}
# numeros = list(numeros)
# print(numeros[0])

# carros = {'gol', 'palio', 'celta'}

# for carro in carros:
#     print(carro)

carros = {'gol', 'palio', 'celta'}
for indice, carro in enumerate(carros):
    print(f"{indice}: {carro}")
