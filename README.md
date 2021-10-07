## Introdução ao Python 3

### Estruturas de repetição:

**While**

```python
while(condicao):
    #Código
```

**for**

```python
for variavel in range(inicio, fim, incremento):
    #codigo (O valor de incremento é opcional)
```
As palavras reservadas break e continue auxiliam no controle do loop sendo esta para encerramento do loop e aquela apenas para encerramento de uma iteração.

### Estruturas condicionais

**if**

```python
if(condicao):
    #Código
elif(condicao):
    #Código
else:
    #Código
```

### Interpolação de String

```python
print("texto {} texto {}".format(variavel1, variavel2))
```

### Gerando números aleatórios

Para gerar números pseudoaleatórios utilizaremos a função randrange da biblioteca random para que os números sejam gerados dentro do range informado.
Obs: O número final é exclusivo.

```python
import random

random.randrange(numero_inicial, numero_final + 1)
```

### Retornando o valor absoluto de um número

Utilizando a função abs() obtemos o valor absoluto de um número (desconsiderando o sinal). Desta forma, o exemplo abaixo teria como retorno 100.

```python
abs(-50-50)
```

### Definindo funções

Para criar uma função utilizamos a palavra reservada def como no exemplo abaixo:

```python
def escolhe_jogo():
    print("===============================")
    print("Escolha seu jogo:")
    print("===============================")

    jogo =  int(input("(1) Advinhação (2) Forca"))

    if (jogo == 1):
        advinhacao.jogar()
    elif (jogo == 2):
        forca.jogar()
```
Obs: É muito importante incluir a condicional que define as funções que serão executadas caso o arquivo seja interpretado diretamente como no exemplo abaixo:

```python
if (__name__ == "__main__"):
    jogar()
```
A condição analisa se o arquivo aberto é o main do projeto.
