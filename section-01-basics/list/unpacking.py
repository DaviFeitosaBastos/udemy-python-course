""" 
Introdução ao unpacking 
"""


# Packing, you should pack the rest of values to use only the first variable
# and unpacking
_, _, nome, *_ = ['Maria', 'Helena', 'Luiz']
print(nome)