"""  
Higher Order Functions
Funcoes de primeira classe
"""

def greetings(msg: str, nome: str) -> str:
    return f'{msg}, {nome}!'


def execute(func, *args):
    return func(*args)



v = execute(greetings, 'bom dia', 'davi')
print(v)