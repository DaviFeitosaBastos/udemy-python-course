"""  
Closure e funcoes que retornam outras funcs
"""
import os

def clear():
    os.system('clear')

def greatings(greating):
    def great(name):
        return f'{greating}, {name}'
    return great


say_morning = greatings('Good morning')
say_night = greatings('Good Night')

clear()

for nome in ['maria', 'joana', 'luiz']:
    print(say_morning(nome))
    print(say_night(nome))