<p align="center"><img src="https://github.com/exp-ext/aprbot/blob/main/static/generated_image.jpeg" width="300" /></p>

### Task 1

Use English SpaCy lib, find all tokens with only digits and all proper nouns (PROPN, aka, personal nouns ) in the text, count it and output it right-aligned in the HTML.
For example, for the text "we need 2 tickets to Dublin, and 1/2 a spoon of milk" read from the stdin (use python myprogram.py < input.txt >output.html ) the program should output that "2" was found twice (output "2"), "1" was found once (output "1"), "Dublin" was found once (output "1").
Display it as an HTML table with 2 columns: the first column for the entry, and the second column for the number of times it was found.
Remember that it will be much easier to set up SpaCy on Colab rather than on a Windows machine.

### Задача 2

Написать программу на питоне, выдающую без повторений на stdout все различные перестановки N одинаковых (0) и N разных чисел (от 1 до N).
Запуск программы должен выглядеть так: "python permute.py 5"
Скажем, для N=5, это будут числа 0 0 0 0 0 1 2 3 4 5 .
Примеры таких перестановок: 0000012345 или 5012034000
Теперь выведите все такие перестановки для N=5 и сохраните их в файл.
Посчитайте с помощью wc количество строк в этом файле.
Сколько получилось?
Попробуйте оценить время, которое будет ваш алгоритм считаться для N=7 (это не значит, что ваш алгоритм должен быть самый лучший и быстрый, просто грубо оцените примерное время выполнения именно для вашего алгоритма, исходя из вашего понимания).

### Задача 3

Написать единый shell-файл для запуска первой и второй программы с параметрами, указанными выше, и получением нужных результатов.

---

Активация окружения и установка зависимостей:

```bash
python3 -m venv venv && source venv/bin/activate && python -m pip install --upgrade pip

python -m pip install -r requirements.txt

python -m spacy download en_core_web_sm
```

Запуск скрипта и выполнения задач:

```bash
bash script.sh
```
