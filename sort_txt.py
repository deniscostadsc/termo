from pathlib import Path


def sort_words(word) -> tuple[int, str]:
    unique_letters = len(set(word))
    count_vowels = 0
    for letter in set(word):
        if letter in 'aeiou':
            count_vowels += 1
    return (-(unique_letters + count_vowels), word)

words : list[str] = []

with open('termo.txt', 'r') as f:
    for line in f:
        words.append(line.strip())

words.sort(key=sort_words)

with open('termo.txt_temp', 'w') as f:
    txt_content = "\n".join(words) + '\n'
    f.write(txt_content)

termo_txt = Path('termo.txt')
termo_txt.unlink()
termo_txt_temp = Path('termo.txt_temp')
termo_txt_temp.rename(termo_txt)