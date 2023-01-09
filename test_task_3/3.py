import pandas as pd
import datetime


def secure_data(value):
    """
    Функция скрывает персональные данные номера счета или карты.
    :param value: str
    :return: str
    """
    value_list = value.split(' ')

    if value.startswith('Счет'):
        secured_data = value_list[0] + ' **' + value_list[1][-4:]
    else:
        number = value_list.pop()
        chunks = number[:4] + ' ' + number[4:6] + '**' + ' ' + '****' + ' ' + number[12:16]
        secured_data = ' '.join(value_list) + ' ' + chunks

    return secured_data


def check_value(value):
    """
    Функция проверяет переданное значение на тип Nan и вызывает функцию secure_data
    :param value: str | Nan
    :return: str
    """
    if value == value:
        data = secure_data(value)
    else:
        data = 'не указано'
    return data


def get_last_operations():
    """
    Функция создает дата-фрейм на основе json-файла, фильтрует данные
    по столбцу "state" так, чтобы остались только выполненные операции,
    сортирует их по дате, отбирает 5 самых поздних операций и выводит данные о них.
    :return: None
    """
    df = pd.read_json('operations.json')
    executed_df = df.query("state == 'EXECUTED'")
    executed_df_sorted = executed_df.sort_values(by=['date'], ascending=False)
    df_5 = executed_df_sorted.iloc[:5]

    for ind, val in df_5.iterrows():

        date = datetime.datetime.strptime(str(val['date']), '%Y-%m-%d %H:%M:%S.%f').strftime('%d.%m.%y')
        description = val["description"]

        from_whom = check_value(val["from"])

        to_whom = check_value(val["to"])

        amount = val["operationAmount"]["amount"]
        currency_name = val["operationAmount"]["currency"]["name"]

        print(f'{date} {description}')
        print(f'{from_whom} - > {to_whom}')
        print(f'{amount} {currency_name}')
        print('------------------------------------------')


if __name__ == '__main__':
    get_last_operations()
