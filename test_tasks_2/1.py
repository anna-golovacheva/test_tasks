def move_zero(num_list: list) -> list:
    """
    Функция перемещает нули в конец массиваю
    :param num_list: list
    :return: list
    """
    last_item = 0
    for i in range(len(num_list)):
        if num_list[i] != 0:
            num_list[i], num_list[last_item] = num_list[last_item], num_list[i]
            print(num_list)
            last_item += 1

    return num_list


if __name__ == '__main__':
    new_list = move_zero([1, 0, 4, 3, 0, 7, 0, 0, 8])
    print(new_list)
