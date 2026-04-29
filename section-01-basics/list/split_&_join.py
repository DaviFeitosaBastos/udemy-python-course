"""  
split e join com list e str
split - divide uma string
join - une uma string
strip - limpa espacos
rstrip - limpa espacos para a direita
lstrip - limpa espacos para a esquerda
"""

frase = '          Olha só que,        coisa interessante                           '

lista_frases_cruas = frase.split(',')


lista_frases = []
for i, frase in enumerate(lista_frases_cruas):
    lista_frases.append(lista_frases_cruas[i].strip())

# print(lista_frases_cruas)
# print(lista_frases)


frase_unidas = ', '.join(lista_frases) # So iteraveis

print(frase_unidas)