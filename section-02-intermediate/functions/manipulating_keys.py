# Manipulando chaves e valores em dicionario
pessoa = {}




# Criar chaves
chave = 'nome'
pessoa[chave] = 'Luiz Otavio'
pessoa['sobrenome'] = 'Miranda' # 

print(pessoa[chave])

# Modificar chaves
pessoa[chave] = 'Maria'


# Apagar chaves
del pessoa['sobrenome']

print(pessoa)
print(pessoa['nome'])


# Evita o erro de KeyError
if pessoa.get('sobrenome') is None: # Get por padrao ele retorna None 
    print("Nao Existe")
else:
    print(pessoa['sobrenome'])