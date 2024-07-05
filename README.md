# Python AI Backend Developer

## Conhecendo a linguagem Python

## Por que usamos tipos?
  - Os tipos servem para definir as caracteristicas e comportamentos de um valor ( objeto) para o interpretador.
  - Subdivide quais operações eu posso fazer com o valor que foi informado, se é um número ou não, se posso fazer operações matemáticas ou não...
  - Informa qual a quantidade em memória que essa variável vai consumir

  Por exemplo: 
    "Com esse tipo eu sou capaz de realizar operações matemáticas."
    "Esse tipo para ser armazenado em memória irá consumir 24 bytes."

### Os tipos built-in são:
| Tipo | Nomenclatura |
| ----------- | ----------- |
| Texto | str |
| Numérico | int, float, complex |
| Sequência | list, tuple, range |
| Mapa | dict |
| Coleção | set, frozenset|
| Booleano | bool |
| Binário | bytes, bytearray, memoryview |
<hr>

# Tipos Numéricos

### Números Inteiros
> São representados pela classe **int** e possuem precisão ilimitada.
São exemplos válidos de números inteiros:
1, 10, 100, -1, -10, -100... 99001823

### Números de Ponto Flutuante
> São usados para representar os números racionais e sua implementação é feita pela classe **float**.
São exemplos válidos de números de ponto flutuante:
1.5, -10.543, 0.76... 9995481.002

<hr>

# Booleanos e Strings

## Booleano
> É usado para representar **verdadeiro** ou **falso**
É implementado pela classe **bool**.
Em *Python* o tipo booleano é uma sublcasse de **int**, uma vez que **qualquer número diferente de 0 representa verdadeiro e 0 representa falso**.
São exemplos de booleanos:
*True* e *False*

## Strings
> Strings ou cadeia de caracteres são usadas para representar valores alfanuméricos, em Python as strings são definidas utilizando a classe **str**.
São exemplos válidos de string:

`"Python"`, `'Python'`, `"""Python"""`, `"p"` 
<hr>

# Modo Interativo

O interpretador Python pode executar um modo que possibilite o desenvolvedor a escrever código e ver o resultado na hora.

## Iniciando o Modo Interativo

Existem duas formas de iniciar o modo interativo.

1. No interpretador
 > Escrever `Python` e apertar *Enter*. Assim, iniciando o modo Interativo
2. Script com flag -i
 > Executar `python -i nomeDoArquivo.py`

3. Para sair digite **`exit()`**

## Funções dir e help
### dir
 - Sem argumentos, retorna al ista de nomes no escopo local atual
 `dir()`
 - Com um argumento, retorna uma lista de atributos válidos para o objeto
 `dir(100)`

### help
 - Invoca o sistema de ajuda integrado. É possível fazer buscas em modo interativo ou informar por parâmetro qual o nome do *módulo*, *função*, *classe*, *métod*o ou *variável*. Ex:
 `help()` `help(100)`


<hr>

## Variáveis e Constantes
### Variáveis
 - Em linguagens de programação podemos definir valores que podem sefrer alterações no deccorer da execução do programa.
 - Esses valores recebem o nome de variáveis, pois eles nascem com um valor e não necessariamente devem permanecer com o mesmo durante a execução do programa

      `age = 23`
      `name = 'Douglas'`
ou 
      `age, name = (23, Douglas)`

        `print(f'Meu nome é {name} e eu tenho {age} ano(s) de idade.')`

#### Alterando valores
- Perceba que não precisamos definir o tipo de dados na variável, o Python faz isso automaticamente para nós.
- Por isso não podemos simplesmente criar uma variável sem atribuir um valor.
Para alterar o valor da variável basta fazer uma atribuição de um novo valor:

  `age = 25`
  `name = 'Douglas Caique'`

  `print(f'Meu nome é {name} e eu tenho {age} ano(s) de idade.')` // Meu nome é Douglas Caique e eu tenho 25 ano(s) de idade.

### Constantes
- Assim como as variáveis, **constantes** são utilizadas para *armazenar valores*.
- Uma constante nasce com um vlaor e **permanece** com ele até o final da execução do programa, ou seja, o valor é **imutável**

### Python não tem Constantes
- Em Python não existe uma palavra reservada para informar ao interpretador que o vlaor é constante.
Em algumas linguagens por exemplo: **Java** e **C**m utilizamos *final* e *const*, respectivamente para declarar uma constante.

> Em Python usamos a convenção que diz ao programador que a variável é uma constante. Para fazer isso, você deve criar a variável com o nome todo em **LETRAS MAIÚSCULAS**

  `NOME_DA_VARIAVEL = 'Constante'`
  `STATES = ['SP', 'RJ, 'BA']`

  #### Boas Práticas
  - O padrão de nomes deve ser *snake case*
  - Escolher nomes sugestivos
  - Nome de constantes todo em maiúsculo
  <hr>

# Conversão de Tipos
Em alguns momentos será necessário converter o tipo de uma variável para manipular de forma diferentes. Por exemplo:
> Variáveis do tipo *string*, que armazenam números e precisamos fazer alguma operação matemática com esse valor.

### Inteiro para Float
`preco = 10  `
`preco = float(preco)`
`preco = 10 / 2`
`print(preco) >>> 5.0`

### Float para Inteiro
`preco = 10.30  `
`preco = int(preco)`
`print(preco) >>> 10`

### Conversão por Divisão
`preco = 10  `
`print(preco / 2) >>> 5.0`
`print(preco // 2) >>> 5`

### Número para String
`preco = 10.50`
`idade = 28`
`print(str(preco)) >>> 10.5`
`print(str(idade)) >>> 28`
`texto = f"idade {idade} preco {preco}`
`print(texto) >>> idade 28 preco 10.5`

### String para Número
`preco = "10.50"`
`idade = "28"`

`print(float(preco))  >>> 10.50`
`print(int(idade)) >>> 28`

### Erro de Conversão
- Nem sempre será possível converter um tipo para outro.
Exemplo:
`preco = "Python"`
`print(float(preco)) >>> ValueError` 