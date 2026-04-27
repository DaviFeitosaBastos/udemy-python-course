""" 
Iteravel -> str, range, etc (__iter__)
Iterador -> quem entregar um valor por vez
next -> me entregue o proximo valor
iter -> me entrega seu iterador
"""
texto = 'Davi' # iteravel
iterador = iter(texto) # iterator


# O que o for faz por tras dos panos
""" while True:
        try:
            letra = next(iterador)
            print(letra)
        except StopIteration:
            break 
"""


for letra in texto:
    print(letra)
    break