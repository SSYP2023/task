"""
Вам дано целое неотрицательное число n. Сгенерируйте матрицу размера (2n + 1) \times (2n + 1)(2n+1)×(2n+1), что:

Клетки раскрашиваются в шахматном порядке, все углы черные.
На главной диагонали стоят нули.
В белые клетки последовательно записываются целые положительные числа, начиная с 1, проходя последовательно по строкам от верхней до нижней, и по столбцам от левого до правого.
В пустые черные клетки последовательно записываются целые отрицательные числа, начиная с -1, проходя последовательно по столбцам от левого до правого, и по строкам от верхней до нижней.

Формат ввода
На вход подается одно целое положительное число n (1≤n≤100).

Формат вывода
Выведите матрицу в (2n+1)(2n+1) строках по (2n+1)(2n+1) чисел, разделяя числа внутри строки пробелами.


Пример 1
Ввод
2
Вывод
0 1 -4 2 -7
3 0 4 -6 5
-1 6 0 7 -8
8 -3 9 0 10
-2 11 -5 12 0
Пример 2
Ввод
3
Вывод
0 1 -6 2 -11 3 -16
4 0 5 -9 6 -14 7
-1 8 0 9 -12 10 -17
11 -4 12 0 13 -15 14
-2 15 -7 16 0 17 -18
18 -5 19 -10 20 0 21
-3 22 -8 23 -13 24 0
Ограничение памяти
256.0 Мб
Ограничение времени
1 с
Ввод
стандартный ввод или input.txt
Вывод
стандартный вывод или output.txt

"""



n = int(input())

even = 1
row = []

for j in range(2*n+1):
    for i in range(2*n+1):
        is_black = (i+j) % 2 == 0
        if i == j:
            digit = 0
        elif not is_black:
            digit = even
            even += 1
        else:

            if i == 0:
                digit_before = 0
            if i % 2 == 0:
                digit_before = i * (n + n - 1) / 2
            else:
                digit_before = (i - 1) * (n + n - 1) / 2 + n
            num_in_col = 1 if j == 0 else (((j+1) if (j+1) % 2 == 0 else j + 2) / 2)
            num_in_col = num_in_col - 1 if num_in_col * 2 > i else num_in_col
            digit = (digit_before + num_in_col) * (-1)
        row.append(str(int(digit)))
    print(" ".join(row))
    row.clear()
