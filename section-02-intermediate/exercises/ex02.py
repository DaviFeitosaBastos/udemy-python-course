"""  
Crie funcoes que duplicam, triplicam e quadruplicam o numero recebido como paramentros
"""

def criar_multiplicador(multiplicador): 
    def multiplicar(numero):
        return numero * multiplicador
    return multiplicar



duplicar = criar_multiplicador(2) # Salva o argumento multiplicador 
triplicar = criar_multiplicador(3)
quadruplicar = criar_multiplicador(4)


print(duplicar(2)) # Aqui adiciona o argumento numero na funcao dentro da funcao
print(triplicar(2))
print(quadruplicar(2))
