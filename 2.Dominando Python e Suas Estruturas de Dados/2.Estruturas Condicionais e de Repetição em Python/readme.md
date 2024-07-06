# Indentação e blocos de comandos

### A Estética
A identação do código é uma forma de manter o código fonte mais *legível* e *manutenível*.

Em Python ela exerce um segundo papel, através da identação o interpretador consegue determinar **onde** um bloco de comando inicia e onde ele termina.

## Bloco de Comando
- As linguagens de programação costuman utilziar caracteres ou palavras reservadas para determinar o início e o fim do bloco.
- Em Java e C, por exemplo, utilizamos chaves:

***Bloco em Java😋***
```
void sacar(double valor) {
    if(this.saldo >= valor) {
        this.saldo -= valor;
    }
}
```
***Bloco em Java sem formatar🤮***
```
void sacar(double valor) {
if(this.saldo >= valor) {
this.saldo -= valor;
}
}
```

### Utilizando Espaços
Existe uma convenção em Python que define as boas práticas para escrita de código na linguagem.
 - É indicado a utilizar 4 espaços em branco por nível de identação
 - Ou seja, a cada novo bloco, adicionamos 4 novos espaços em branco.

 ***Bloco em Python🐍***
```
def sacar(self, valor: float) -> None:
    if self.saldo >= valor:
        self.saldo -= valor
```

<hr>

# Estruturas Condicionais
#### O que são?
    São estruturas que permitem o desvio de fluxo de controle 
    quando determinadas expressões lógicas são atendidas
- Estruturas de código que funcionam ao depender de uma validação prévia

## If/ If-else / Elif
### If
> Para criar uma estrutura condicional simples, composta por um único desvio, podemos utilizar a palavra reservada **if**.
O comando irá testar a expressão lógica e em caso de retorno verdadeiro, as ações presentes no bloco de código serão executadas.

Exemplo:
```
saldo = 2000.0
saque = float(input("Informe o valor do saque: "))

if saldo >= saque:
    print("Saque realizado!")

if saldo < saque:
    print("Saldo insuficiente!")
```

### If/else
> Para criar uma estrutua condicional com dois desvios utilizamos as palavras reservadas **if** e **else**.
O bloco If irá testar a condição e caso não seja verdadeira o bloco de código do else será executado.

Ex:
```
saldo = 2000.0
saque = float(input("Informe o valor do saque: "))

if saldo >= saque:
    print("Saque realizado!")
else:
    print("Saldo insuficiente!")
```

### If/else/elif
> Quando temos mais de 2 desvios, para isso utilizamos a palavra reservado **elif**.
- Não existe um número máximo de elifs que podemos utilizar
- Evite grandes estruturas condicionais, pois elas aumentam a complexidade do código.

Ex:
```
opcao = int(input("Informe uma opção: [1] Sacar \n[2] Extrato: "))

if opcao == 1:
    valor = float(input("Informe a quantia par o saque: "))
elif opcao == 2:
    print("Exibindo o extrato...")
else:
    sys.exit("Opção inválida")
```


## If Aninhado
>Podemos criar estruturas aninhadas, para isso, basta adicionar estruturas if/elif/else dentro do outro bloco if/elif/else

Ex:
```
if conta_normal:
    if saldo >= saque:
        print("Saque realizado com sucesso")
    elif saque <= (saldo + cheque_especial):
        print("Saque realizado com uso do cheque especial")
elif conta_universitaria:
    if saldo >= saque:
        print("Saque realizado com sucesso")
    else:
        print("Saldo insuficiente")
```

## If Ternário

> O If Ternário permite escrever uma condição em uma única linha.
Ele é composta por três partes
- 1° Retorno caso a expressão retorne verdadeiro
- 2° Expressão Lógica
- 3º Retorno caso a expressão não seja atendida.

> 'retorno Verdadeiro if **condição** else 'retorno falso'

Ex:
```
    status = "Sucesso" if saldo >= saque else "Falha"

    print(f"{status} ao realizar o saque!")
```

<hr>

# Estruturas de Repetição

## O que são?
> - São estruturas utilizadas para repetir um trecho de código um determinado número de vezes
> - Esse numero pode ser conhecido previamente ou determinado através de uma expressão lógica

Ex:
- Executar um código X quantidade de vezes
- Executar um código até que o valor X seja encontrado


```
    a = int(input('Informe um número inteiro: '))
    print(a)

    a += 1
    print(a)

    a += 1
    print(a)
```
E se eu quiser os 100 próximos números da sequencia?
```
repita 100 vezes:
    a += 1
    print(a)

```

## For e built-in range
### For
> O comando **for** é usado para percorrer um objeto iterável.
Faz sentido usar **for** quando sabemos o *número exato de vezes* que nosso bloco de código deve ser executado ou quando queremos percorrer um objeto iterável.

Ex:

```
    texto = input('Informe um texto: ')
    VOGAIS = "AEIOU"

    for letra in texto:
        if letra.upper() in VOGAIS:
            print(letra, end="")
    print()
```

O for é divido em duas partes:
1. O objeto iterável que desejamos percorrer, em nosso caso o `texto`
2. O item que esta sendo iterado naquele momento, `letra`

**Estrutura**
    
` for var in objeto: `

### Range
Range é uma função built-in do Python
- Usada para produzir uma sequência de números inteiros a partir de um início para um fim
- range(i,j)
> Recebe 3 argumentos: 
> - stop(obrigatório)
> - start(opcional)
> - step(opcional)

 `range(start, stop,[step])`

Ex:
```
list(range(4))   >>> [0, 1, 2, 3]
```

## While
> É usado para repetir um bloco de código várias vezes
- Faz sentido usar o while quando não sabemos o número exato de vezes que nosso bloco de código será executado

Ex:
```
    opcao = -1

    while opcao != 0:
        opcao = int(input('[1] Sacar \n[2] Extrato \n[0] Sair \n: '))

        if oppcao == 1:
            print('Sacando...')
        elif opcao == 2:
            print('Exibindo o extrato...')
```

### Break

É uma palavra reservada que serve para interromper alguma repetição.