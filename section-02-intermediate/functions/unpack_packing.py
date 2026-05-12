"""  
args - Argumentos nao nomeados
* - *args (empacotamente e desempacotamento)
"""

# Lembre-te de desempacotamento
# x, y, *resto = 1, 2, 3, 4
# print(x, y, resto)


# def soma(x, y):
#     return x + y

def soma(*args): # Empacota
    total = 0
    for numero in args:
        total += numero
    return total



soma_1_2_3 = soma(1, 2, 3)

soma_4_5_6 = soma(4, 5, 6)


numeros = 1, 2, 3, 4, 5, 6, 7, 78, 10 # Tupla
outra_soma = soma(*numeros) # Desempacota
print(outra_soma)

print(sum(numeros))