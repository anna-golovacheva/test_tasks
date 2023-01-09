from re import sub


def to_camel_case(text):
    if text[0].isupper():
       text = sub(r"(_|-)+", " ", text).title().replace(" ", "")
    else:
       text = sub(r"(_|-)+", " ", text).title().replace(" ", "")
       text = text[0].lower() + text[1:]

    return text


print(to_camel_case('Посчитайте сумму н-го ряда пирамиды нечетных чисел (начало с 0_1)'))
