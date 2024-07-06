# Tipos de Operadores com Python🧮

## Operadores Aritméticos
### O que são?
> Executam operações matemáticas como adição, subtração com operandos.

Exemplos:
> **Adição:**
print(1 + 1) >>> 2

> **Subtração:**
print(10 - 2) >>> 8

> **Multiplicação:**
print(4 * 3) >>> 12

> **Divisão:**
print(12 / 3) >>> 4.0

> **Divisão Inteira:**
print(12 // 2) >>> 6

> **Módulo:** Resto da Divisão
print(10 % 3) >>> 1

> **Exponenciação:**
print(2 ** 3) >>> 8


## Precedência de Operadores
Na matemática existe uma regra que indica quais operações devem ser executadas primeiro.
Isso é útil pois ao analisar uma expressão, a depender da ordem das opreações o valor pode ser diferente:

> x = 10 - 5 * 2
x é igual a 10 ou a 0?

#### Na matemática
A definição indica a seguinte ordem como a correta:
1. Parêntesis
2. Expoêntes
3. Multiplicações e divisões (da esquerda para a direita)
4. Somas e subtrações (da esquerda para a direita)

Exemplos:
```
    print(10 - 5 * 2) >>> 0
    print((10 - 5) * 2) >>> 10
    print(10 ** 2 * 2) >>> 200
    print(10 ** (2 * 2) >>> 10000)
    print(10 / 2 * 4) >>> 20.0
```
<hr>

## Operadores de Comparação
### O que são?
 São operadores utilizados para compararar dois valores. 
 - Os retornos serão sempre valores booleanos.

**Igualdade:**
 ```
    saldo = 450
    saque = 200

    print(saldo == saque)   >>> False
 ```

**Diferença:**
 ```
    saldo = 450
    saque = 200

    print(saldo != saque)   >>> True
 ```

**Maior que / Maior ou Igual:**
 ```
    saldo = 450
    saque = 200

    print(saldo > saque)   >>> True
    print(saldo >= saque)   >>> True
 ```

**Menor que / Menor ou Igual:**
 ```
    saldo = 450
    saque = 200

    print(saldo < saque)   >>> False
    print(saldo <= saque)   >>> False
 ```
<hr>

## Operadores de Atribuição
### O que são?
São operadores utilizados para definir o valor inicial ou sobrescrever o valor de uma variável

**Atribuição Simples:**
 ```
    saldo = 500
    print(saldo) >>> 500
 ```
**Atribuição com Adição:**
 ```
    saldo = 500
    saldo += 200
    print(saldo) >>> 700
 ```
**Atribuição com Subtração:**
 ```
    saldo = 500
    saldo -= 100
    print(saldo) >>> 400
 ```
**Atribuição com Multiplicação:**
 ```
    saldo = 500
    saldo *= 2
    print(saldo) >>> 1000
 ```
**Atribuição com Divisão:**
 ```
    saldo = 500
    saldo /= 5
    print(saldo) >>> 100.0

    saldo = 500
    saldo //= 5
    print(saldo) >>> 100
 ```
**Atribuição com Módulo:**
 ```
    saldo = 500
    saldo %= 480
    print(saldo) >>> 20
 ```
**Atribuição com Exponenciação:**
 ```
    saldo = 80
    saldo **= 2
    print(saldo) >>> 6400
 ```
 <hr>

 ## Operadores Lógicos
 ### O que são?
 
 São operadores utilizados em conjunto com os operadores de comparação, para montar uma expressão lógica.
 Quando um operador de comparação é utlizado, o resultado retornado é um booleano, dessa forma podemos combinar operadores de comparação com os operadores lógicos, exemplo:
 >*op_comparacao + op_logico + op comparacao... N...*

```
   saldo = 1000
   saque = 200
   limite = 100

   saldo >= saque  >>> True
   saque <= limite >>> False
```

Usando as seguintes variáveis como exemplo:
```
   saldo = 1000
   saque = 200
   limite = 100
```

**Operador E**
 - Saldo maior ou igual a Saque **E** Saque menor ou igual a limite
  `saldo >= saque and saque <= limite  >>> False` 

**Operador OU**
- Saldo maior ou igual a Saque **OU** Saque menor ou igual a limite
  `saldo >= saque or saque <= limite  >>> True`

**Operador Negação**
- Operador **not**
- A Negação nega o valor original devolvido pelo elemento.
   `contatos_emergencia = []` - Lista vazia em Python é considerado um boolean falso.
  `not 1000 > 1500  >>> True` - Inverso do verdadeiro
  `not contatos_emergencia  >>> True`
  `not "saque 1500;"  >>> False`
  `not ""  >>> True`

**Parênteses**
```
   saldo = 1000
   saque = 200
   limite = 100
   conta_especial = True
```

`saldo >= saque and saque <= limite or conta_especial and saldo >= saque  >>> True`

`(saldo >= saque and saque <= limite) or (conta_especial and saldo >= saque)  >>> True`

<hr>

## Operadores de Identidade
### O que são?
São operadores utilizados para comparar se dois objetos testados ocupam a mesma posição na memória.
> Operador : **is**

Exemplo:
```
   curso = "Curso de Python"
   nome_curso = curso
   saldo, limite = 200, 200
```
`curso is nome_curso >>> True`
`curso is not nome_curso >>> False`
`saldo is limite >>> True`

objetoA is objetoB?

<hr>

## Operadores de Associação
### O que são?
São utilizados para verificar se um objeto está presente em uma seqência

> Operador: **in**

Exemplo

```
   curso = "Curso de Python"
   frutas = ["laranja", "uva", "limão"]
   saques = [1500, 100]
```

`"Python" in curso  >>> True`
`"maçã" not in frutas  >>> True`
`200 in saques  >>> False`