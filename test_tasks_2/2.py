def odd_pyramid_sum(row: int) -> int:
    """
    Функция вычисляет сумму соответствующего ряда пирамиды нечетных чисел.
    :param row: int
    :return: int
    """
    first_num = sum(range(1, row)) * 2 + 1
    last_num = first_num + (row - 1) * 2
    row_sum = int((first_num + last_num) * row / 2)

    return row_sum


if __name__ == '__main__':
    print(odd_pyramid_sum(5))
