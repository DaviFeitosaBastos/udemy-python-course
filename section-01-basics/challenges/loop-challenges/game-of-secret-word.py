""" 
faça um jogo para o usuario advinhar qual a palavra secreta.

-Você vai propor uma palavra secreta qualquer e vai dar a possibilidade para o usuario digitar apenas uma letra.

- quando o usuario digitar uma letra, voce vai conferir se a letra digitada esta na palavra secreta.
        - se a letra digitada estiver na palavra secreta; exiba a letra;

        - Se a letra digitada nao estiver na palavra secreta; exiba *,
faça a contagem de tentativas do seu usuario
"""
import os

SECRET_WORD = 'perfum'
RIGHT_WORD = ''
attempts = 0

while True:
    letter_typed = input('Type a letter: ')
    attempts += 1

    if len(letter_typed) > 1:
        print('Type just one letter.')
        continue

    if letter_typed in SECRET_WORD:
        RIGHT_WORD += letter_typed

    word_formed = ''
    for secret_letter in SECRET_WORD:
        if secret_letter in RIGHT_WORD:
            word_formed += secret_letter
        else:
            word_formed += '*'

    print('Word formed:', word_formed)

    if word_formed == SECRET_WORD:
        os.system('clear' if os.name == 'posix' else 'cls')
        print("CONGRATS!!! YOU WON!!!")
        print("The word was", word_formed)
        print("Attempts:", attempts)
        RIGHT_WORD = ''
        attempts = 0
    