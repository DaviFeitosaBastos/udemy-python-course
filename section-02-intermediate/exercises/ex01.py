# Exercicio com funcoes

# Crie uma funcao que multiplica todos os argumentos
# nao nomeados recebidos
# Retorne o total para uma variavel e mostre o valor 
# da variavel.

# Crie uma funcao que retorar e o numero e impar ou par


def even_odds(x):
    if x % 2 == 0:
        return f'{x} é par'
    return f'{x} é ímpar'

def multiply(*args):
    result = 1
    for i in args:
        result *= i
    return result


numbers = multiply(1,2,3,4,5)
even_or_odd = even_odds(numbers)
print(f'{numbers}\n{even_or_odd}')