""" 
enumerate - enumerate iteraveis (indices)
"""

# [(0,'Maria'),(1,'Helena'),(2,'Luiz'),(3,'Joao')]
lista = ['Maria', 'Helena', 'Luiz']

lista.append('Joao')

for indice, nome in enumerate(lista):
    print(indice, nome, lista[indice])

# for item in enumerate(lista):
#     indice, nome = item
#     print(indice, nome)

# for tupla_enumerada in enumerate(lista):
#     print("For da tupla:")
#     for valor in tupla_enumerada:
#         print(f"\t{valor}")



# lista_enumerada = list(enumerate(lista))

# if i use enumerate in a var 

# for i in enumerate(lista):
#     print(i)

#            1         2         3
# fruits = ["apple", "banana", "cherry"]

# for index, fruit in enumerate(fruits, start=1):
#     print(index, fruit)

# # 1 apple
# # 2 banana
# # 3 cherry

""" 
enumerate() return a object lazy (a iterator), not a list. He generates pairs on demand:
"""

# print(enumerate(fruits))
# # <enumerate object at 0x...>

# print(list(enumerate(fruits)))
# # [(0, 'apple'), (1, 'banana'), (2, 'cherry')]