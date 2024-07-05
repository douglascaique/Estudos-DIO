# Conhecendo a linguagem
### O que são Tipos?
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

# Tipos Numéricos

### Números Inteiros
> São representados pela classe **int** e possuem precisão ilimitada.
São exemplos válidos de números inteiros:
1, 10, 100, -1, -10, -100... 99001823

### Números de Ponto Flutuante
> São usados para representar os números racionais e sua implementação é feita pela classe **float**.
São exemplos válidos de números de ponto flutuante:
1.5, -10.543, 0.76... 9995481.002

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

`"Python", 'Python', """Python""", "p"` 