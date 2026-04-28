"""  
Imprecisao de ponto flutuante

Double-precision floating-point format IEEE -754
"""
from decimal import Decimal # more precisely

numero_1 = Decimal(0.1)
numero_2 = Decimal(0.7)
numero_3 = numero_1 + numero_2

print(numero_3)
print(f'{numero_3:.2f}')
print(round(numero_3, 2))