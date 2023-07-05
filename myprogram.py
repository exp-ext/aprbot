"""
https://habr.com/ru/articles/531940/
"""
from collections import defaultdict
import sys
from typing import List

import spacy

MODEL = 'en_core_web_sm'


def digits_proper_nouns(text: str) -> List:
    """
    Анализирует входной текст и возвращает список подсчетов цифр и
    собственных существительных, найденных в тексте.

    ## Аргументы:
        text (`str`): Входной текст для анализа.

    ## Возвращает:
        `List`: Список подсчетов цифр и собственных существительных,
        найденных в тексте. Каждый элемент в списке представляет собой
        кортеж, содержащий запись и соответствующий подсчет.
    """

    nlp = spacy.load(MODEL)
    counts = defaultdict(int)
    doc = nlp(text)

    for token in doc:
        if token.is_digit:
            counts[token.text] += 1
        elif token.pos_ == 'PROPN':
            counts[token.text] += 1
    return counts


def array_to_html_table(counts: List) -> str:
    """
    Генерирует HTML-таблицу, представляющую подсчеты.

    ## Аргументы:
        counts (`List`): Список подсчетов цифр и собственных существительных.

    ## Возвращает:
        `str`: Строка, содержащая HTML-представление таблицы подсчетов.
    """
    html_table = '<table>\n<tr><th>Entry</th><th>Count</th></tr>\n'
    for entry, count in counts.items():
        html_table += f'<tr><td>{entry}</td><td>{count}</td></tr>\n'
    html_table += '</table>'
    return html_table


if __name__ == '__main__':
    if len(sys.argv) != 3 or '.txt' not in sys.argv[1] or '.html' not in sys.argv[2]:
        print('Запуск программы должен выглядеть так: "python myprogram.py input.txt output.html')
        sys.exit(1)
    input_file = sys.argv[1]
    with open(input_file, "r") as file:
        text = file.read()
    with open(sys.argv[2], 'w') as file:
        file.write(array_to_html_table(digits_proper_nouns(text)))
