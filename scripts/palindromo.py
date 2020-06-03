word = input('ingresa una palabra ')
# print(word[::-1])
word_reverse = word[::-1]
# print(type(word_reverse))
# print(word_reverse)
if word == word_reverse:
    print(f'la palabra {word} es palindromo porque {word} = {word_reverse}')
else:
    print(f'la palabra {word} no es palindromo porque escrita al revés es {word_reverse}')