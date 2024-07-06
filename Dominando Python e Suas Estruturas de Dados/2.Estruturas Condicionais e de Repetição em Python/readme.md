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

## Estruturas Condicionais

