phrase = 'aaaooo'

i = 0

qtd_apareceu_mais_vezes = 0

letra_apareceu_mais_vezes = ''

while i < len(phrase):
    letra_atual = phrase[i]
    qtd_apareceu_mais_vezes_atual = phrase.count(letra_atual)

    if letra_atual == ' ':
        i += 1
        continue

    if qtd_apareceu_mais_vezes < qtd_apareceu_mais_vezes_atual:
        qtd_apareceu_mais_vezes = qtd_apareceu_mais_vezes_atual
        letra_apareceu_mais_vezes = letra_atual

    i += 1

print(
    'A letra que mais apareceu foi '
    f'[{letra_apareceu_mais_vezes}] que apareceu '
    f'{qtd_apareceu_mais_vezes}x'
)