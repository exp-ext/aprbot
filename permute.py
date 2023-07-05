"""
https://docs-python.ru/standart-library/modul-itertools-python/funktsija-permutations-modulja-itertools/
https://losst.pro/komanda-wc-v-linux
"""
import sys
from itertools import permutations

from timing import timing


@timing
def generate_permutations(N):
    """
    Генерирует все возможные перестановки последовательности чисел
    и нулей длины N.

    ## Аргументы:
        N (`int`): Длина последовательности.

    ## Возвращает:
        `Tuple`: Список строк, представляющих все возможные перестановки
        последовательности.

    Функция permutations() генерирует n! перестановок для списка из
    n элементов. В данном случае, n = 2N, поскольку elements содержит
    2N элементов и генерация будет представлять экспоненциальный рост O((2N)!).
    Преобразование каждой перестановки в строку это ещё N.
    Таким образом, теоретическое время выполнения алгоритма этой функции будет
    примерно O((2N)! * N).
    """
    zeros = ['0'] * N
    numbers = [str(i) for i in range(1, N + 1)]
    elements = zeros + numbers
    perms = set(permutations(elements, len(elements)))
    return tuple(''.join(perm) for perm in perms)


if __name__ == '__main__':
    if len(sys.argv) != 2:
        print('Запуск программы должен выглядеть так: "python permute.py 5"')
        sys.exit(1)

    N = int(sys.argv[1])
    perms = generate_permutations(N)

    with open('permutations.txt', 'w') as file:
        for perm in perms:
            file.write(perm + '\n')
