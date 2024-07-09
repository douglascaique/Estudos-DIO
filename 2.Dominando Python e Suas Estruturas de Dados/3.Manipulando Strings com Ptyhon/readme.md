# Manipulando Strings com Python

## Conhecendo Métodos Úteis da classe String

- A classe String do Python é famosa por ser rica em métodos
- Possui uma interface fácil de trabalhar

Em algumas linguagens, manipualr sequências de caracteres não é um trabalho trivial, porém, em Python, esse trabalho é muito simples.

**Maiúscula, minúscula e título**
```
curso = "pYtHon"

print(curso.upper())   >>> PYTHON
print(curso.lower())   >>> python
print(curso.title())   >>> Python
```

**Eliminando espaços em branco**
```
curso = "     Python "

print(curso.strip())   >>> "Python"
print(curso.lstrip())   >>> "Python "
print(curso.rstrip())   >>> "     Python"
```

**Junções e Centralização**
```
curso = "Python"

print(curso.center(10, "#"))   >>> "##Python##"
print(".".join(curso))   >>> "P.y.t.h.o.n"

```

<hr>

## Interpolação de variáveis

Em Python nos temos 3 formas de interpolar variáveis
1. Usando o sinal ***%***     >>>     - *Não é recomendado*
2. Utilizando o método ***format***
3. Utilizando ***f strings***

**Old Style - %**
- %s = String
- %d = Inteiro
- %f - Ponto Flutuante

Colocar no código os valores substituíveis e acrescentar no final do código qual a variável que será substituída


```
nome = 'Douglas'
idade = 25
profissao = 'Programador'
linguagem = 'Python'

print("Olá, me chamo %s, Eu tenho %d anos de idade, trabalho como $s e estou matriculado no curso de %s" % (nome, idade, profissao, linguagem))

>>> Olá, me chamo Douglas, Eu tenho 25 anos de idade, trabalho como Programador e estou matriculado no curso de Python
```

**Método Format**

- {} - Utiliza chaves como Template Strings
- Pode escolher a posição da variável de acordo posição da atribuição da .format
- Permite a reutilização de variáveis de uma forma mais simples


```
nome = 'Douglas'
idade = 25
profissao = 'Programador'
linguagem = 'Python'

print("Olá, me chamo {}, Eu tenho {} anos de idade, trabalho como {} e estou matriculado no curso de {}") .format (nome, idade, profissao, linguagem)

print("Olá, me chamo {0}, Eu tenho {1} anos de idade, trabalho como {2} e estou matriculado no curso de {3}") .format (nome, idade, profissao, linguagem)

>>> Olá, me chamo Douglas, Eu tenho 25 anos de idade, trabalho como Programador e estou matriculado no curso de Python
```

- Permite nomear as variáveis
```
print("Olá, me chamo {nome}, Eu tenho {idade} anos de idade, trabalho como {profissao} e estou matriculado no curso de {linguagem}") .format (nome=nome, idade=idade, profissao=profissao, linguagem=linguagem)
```

- Permite trabalhar com objetos/dicionário
```
pessoa = {
    nome = 'Douglas',
    idade = 25,
    profissao = 'Programador',
    linguagem = 'Python'
}

print("Olá, me chamo {nome}, Eu tenho {idade} anos de idade, trabalho como {profissao} e estou matriculado no curso de {linguagem}") .format (**pessoa)
```

**Método F-String**
- Método muito mais simples e objetivo
- Sem necessidade de identificadores no final.
```
nome = 'Douglas'
idade = 25
profissao = 'Programador'
linguagem = 'Python'

print(f"Olá, me chamo {nome}, Eu tenho {idade} anos de idade, trabalho como {profissao} e estou matriculado no curso de {linguagem}")
```

**Formatar Strings com F-String**
```
PI = 3.14159

print(f"Valor de PI: {PI:.2f}") >>> "Valor de PI: 3.14"
print(f"Valor de PI: {PI:10.2f}") >>> "Valor de PI:          3.14"
```

<hr>

## Fatiamento de string

É uma técnica utilizada para retornar substring(partes da string original)
- Informa inicio - start
- Informa fim - stop
- Informa passo - step

`[start: stop[,step]]`

nome_completo = "Lucas Borges Bagulhão Chapado"

nome_completo[0]        >>> "L"
nome_completo[:4]       >>> "Lucas"
nome_completo[5:]       >>> "Borges Bagulhão Chapado"
nome_completo[5:11]     >>> "Borges"
nome_completo[0:20:2]   >>> "LcsBre auh"
nome_completo[:]        >>> "Lucas Borges Bagulhão Chapado"
nome_completo[::-1]     >>> "odapahC oãhlugaB segroB sacuL"

<hr>

## String múltiplas linhas

São definidas informando ***3 aspas*** simples ou duplas durante a atribuição
Podem ocupar várias linhas do código, e todos os espaços em branco são incluidos na string final


***Strings Triplas***
```
nome = "Douglas"

mensagem = f"""
Olá, meu nome é {nome},
        Eu estou aprendendo Python
"""
```