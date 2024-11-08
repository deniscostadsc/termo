WORD_SIZE = 5

wrong_place_letters : list[str] = ['', '', '', '', '']
not_in_word_letter : str = ''
correct_letters : list[str] = ['', '', '', '', '']


def filter_words(word):
    for index, letter in enumerate(word):
        if correct_letters[index] and not letter == correct_letters[index]:
            return False
        if wrong_place_letters[index]:
            if letter in wrong_place_letters[index]:
                return False
            for wrong_letter in ''.join(wrong_place_letters):
                if not wrong_letter in word:
                    return False
        if not_in_word_letter and letter in not_in_word_letter:
            return False
    return True

words : list[str] = []

with open('termo.txt', 'r') as f:
    for line in f:
        words.append(line.strip())

print(f'Nós temos {len(words)} palavras na nossa lista')
print(f'Entre com a palavra: {words[0]}')

while True:
    valid = input('Essa é uma palavra válida? y/n')
    if valid == 'n':
        del words[0]
        print(f'Entre com a palavra: {words[0]}')
        continue

    count_corrects = 0
    for index, letter in enumerate(words[0]):
        result = input(f"What was the result for the letter {letter}? 1 - correct  2 - wrong place  3 - not in word")
        
        if result == '1':
            correct_letters[index] = letter
            count_corrects += 1
        
        elif result == '2':
            wrong_place_letters[index] += letter
        
        else:
            not_in_word_letter += letter
    
    if count_corrects == 5:
        print('Acertou a palavra!')
        break
    
    words = list(filter(filter_words, words))
    
    print(f'Nós temos {len(words)} palavras na nossa lista')
    print(f'Entre com a palavra: {words[0]}')