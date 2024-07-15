# Estruturas de Dados

## Listas
### Criação e Acesso a dados
 **Criando Listas**
 > Listas em Python podem armazenar de maneira sequencial qualquer tipo de objeto. Podemos cirar listas utilizando o construtor **list**, a função *range* ou colocando valores separados por vírcula dentro de colchetes. Listas são objetos mutáveis, portanto podemos alterar seus valores após a criação.

 **Declaração**
    - Utilizando construtor **list**
        `letras - list("python")`
    - Utilizando a função *range*
        `numeros = list(range(10))`
    - Valores separados por vírgulas dentro de colchetes
        `carro = ["Ferrari", "F8",  4200000, 2020, 2900, "São Paulo", True]`
    
 **Acesso direto**
 > A lista é uma sequência, portanto podemos acessar seus dados utilizando **índices**.
 Contamos o índice de determinada sequência a partir do zero.

```
    frutas = ["maçã", "laranja","kiwi","manga"]

    frutas[0]   >>> maçã
    frutas[3]   >>> manga

```

 **índices Negativos**
 >Sequências suportas indexação negativa. A contagem começa em -1

```
    frutas = ["maçã", "laranja","kiwi","manga"]

    frutas[-1]   >>> manga
    frutas[-3]   >>> laranja

```
**Listas Aninhadas**
>Listas podem armazenar todos os tipos de objetos Python, inclusive, listas podem armazenar outras listas. Com isso podemos criar estruturas bidimensionais(tabelas) e acessar informando os índices de linha e coluna. 
Este na verdade é o conceito de MATRIZES

```
matriz = [
        [1, 'a', 2],
        ['b', 3, 4],
        [6, 5, 'c]
]

matriz[0]       >>> [1, 'a', 2]
matriz[0][0]    >>> 1
matriz[0][-1]   >>> 2
matriz[-1][-1]  >>> 'c'
```


**Fatiamento**

Além de acessar elementos diretamente, podemos extrair um conjunto de valores de uam sequência. Para isso basta passar o índice inicial e/ou final para acessar o conjunto. Podemos ainda informar quantas posições o cursor deve 'pular' no acesso

```
lista = ['p','y','t','h','o','n']

lista[2:]   >>>['t','h','o','n']
lista[:2]   >>>['p','y']
lista[1:3]  >>>['y','t']
lista[0:3:2]    >>>['p','t']
lista[::]   >>> ['p','y','t','h','o','n']
lista[::-1] >>> ['n','o','h','t','y','p']

```

**Iterar listas**

A forma mais comum para percorrer os dados de uma lista é utilizando o comando **for**

```
carros = ['gol', 'celta', 'palio']

for indice, carro in enumerate(carros):
    print(f'{indice}: {carro}')

```

**Compreensão de listas**

A compreensão de listas oferece uma sintaxe mais curta quando você deseja:
- Criar uma nova lista com base nos valores de uma lista existente(filtro)
- Gerar uma nova lista aplicando alguma modificação nos elementos de uma lista existente

**Versão 1**
```
numeros = [1, 30, 21, 2, 9, 65, 34]
pares []

for numero in numeros:
    if numero % 2 == 0:
        pares.apprend(numero)
```

**Versão 2**
```
numeros = [1, 30, 21, 2, 9, 65, 34]
pares = [numero for numero in numeros if numero % 2 == 0]
```

**Modificando valores Versão 1**
```
numeros = [1, 30, 21, 2, 9, 65, 34]
quadrado []

for numero in numeros: 
    quadrado.apprend(numero ** 2)
```

**Modificando valores Versão 2**
```
numeros = [1, 30, 21, 2, 9, 65, 34]
quadrado = [numero ** 2 for numero in numeros]
```

## Métodos da classe LIST

**[ ].append**
```
lista = []

lista.append(1)
lista.append('Python')
lista.append([40,30,20])

print(lista)    >>> [1, 'Python, [40,30,20]]
```

**[ ].clear**
```
lista = [1, 'Python, [40,30,20]]
lista.clear()
print(lista) >>> []

```

**[ ].copy**

```
lista = [1, 'Python, [40,30,20]]
lista.copy()
print(lista)    >>> []
```

**[ ].count**
- conta o numero de um elemento especificodentro da lista
cores = ['vermelho]

**[ ].extend**
- Adiciona/junta novos elementos entre listas
- Não elimina valores duplicados

**[ ].index**
- Encontra a primeira ocorrencia de um elemento na lista

**[ ].pop**
- Retira o último elemento da lista
- A lista é organizada automaticamente como pilha. Logo o ultimo elemento adicionado será o primeiro a ser retirado

**[ ].remove**
- Remove um objeto em si, não necessitando do índice do mesmo.
- Remove a primeira ocorrência


**[ ].reverse**
- Inverte a ordem da lista, espelhamento

**[ ].sort**
- Ordena a lista

**[ ].len**
- Verifica o tamanho da listas

**[ ].sorted**
- Ordena os iteráveis


## Tuplas
> São estruturas de dados muito parecidas com as listas,  principal diferênça é que tupla são **IMUTÁVEIS**, enquanto a lista é mutável.
Podemos criar tuplas atráves da classe **tuple**, ou colocando valores separados por vírgula de parenteses.


```
frutas = ("laranja", "pera", "uva",)

letras = tuple("python")

numeros = tuple([1,2,3,4])

```

**Acesso direto**
A tupla é uma sequência, portanto podemos acessar seus dados utilizando índices.


```
frutas = ("maçã", "laranja", "uva", "pera",)

frutas[0]   >>> maçã
```

**Tuplas aninhadas**

Tuplas podem armazenar todos os tipos de objetos Python, portnato podemos ter tuplas que armazenam outras tuplas.
Com isso podemos criar estruturas bidimensionais.



```
matriz = (
    (1,'a',2),
    ('b',3,4),
    (6,5'c')
)
```


## Conjuntos
> Um set é uma coleção que não possui objetos repetidos
- Usamos sets para representar conjuntos matemáticos ou eliminar itens dubplicados de um iterável
- Elimina os itens duplicados dentro de um objeto iterável

```
numeros = set([1, 2, 3, 1, 3, 4])
print(numeros)

letras = set('abacaxi')
print(letras)

carros = set(('gol', 'palio', 'celta', 'palio'))
print(carros)

linguagens = {'python', 'java', 'python', 'c#'}
print(linguagens)

```

**Acessando Dados**

Conjuntos em Python não suportam indexação e nem fatiamento.
Para acessar os valores, é necessário converter o conjunto para lista

```
numeros = {1, 2, 3, 2}
numeros = list(numeros)
print(numeros[0])
```


**Iterar conjuntos**\

A forma mais comum para percorrer os dados de um conjunto é utilizando o comando ***for***

```
carros = {'gol', 'palio', 'celta'}

for carro in carros:
    print(carro)
```

**Função enumerate**

> Às vezes é necessário saber qual o índice do objeto dentro do laço ***for***.
Podemos usar para isso, a função **enumerate**

```
carros = {'gol', 'palio', 'celta'}
for indice, carro in enumerate(carros):
    print(f"{indice}: {carro}")
```

**Métodos da classe set**

**{}.union**
```
conjunto_a = {1, 2}
conjunto_b = {3, 4}

conjunto_a.union(conjunto_b)
```

**{}.intersection**
```
conjunto_a = {1, 2, 3}
conjunto_b = {2, 3, 4}

conjunto_a.intersection(conjunto_b)

```

**{}.difference**
```
conjunto_a = {1, 2, 3}
conjunto_b = {2, 3, 4}

conjunto_a.difference(conjunto_b)
conjunto_b.difference(conjunto_a)
```

**{}.symmetric_difference**
```
conjunto_a = {1, 2, 3}
conjunto_b = {2, 3, 4}

conjunto_a.symmetric_difference(conjunto_b)
```

**{}.issubset**
```
conjunto_a = { 1, 2, 3}
conjunto_b = { 4, 1, 2, 5, 6, 3}

conjunto_a.issubset(conjunto_b)
conjunto_b.issubset(conjunto_a)

```
**{}.issuperset**
```
conjunto_a = { 1, 2, 3}
conjunto_b = { 4, 1, 2, 5, 6, 3}

conjunto_a.issuperset(conjunto_b)
conjunto_b.issuperset(conjunto_a)
```

**{}.isdisjoint**
```
conjunto_a = {1, 2, 3, 4, 5}
conjunto_b = {6, 7, 8, 9}
conjunto_c = {1, 0}

conjunto_a.isdisjoint(conjunto_b)
conjunto_a.isdisjoint(conjunto_c)
```

**{}.add**
```
sorteio = {1, 23}

sorteio.add(25)
sorteio.add(42)

```

**{}.clear**
```

```

**{}.copy**
```

```

**{}.discard**
```

```

**{}.pop**
```

```

**{}.remove**
```

```

**{}.len**
```

```

**{}.in**



## Dicionários



## Funções