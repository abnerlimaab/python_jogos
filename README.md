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