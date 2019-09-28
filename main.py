from numpy import issubdtype, signedinteger

third_digits_list = {
    '0': 'ноль',
    '1': 'один',
    '2': 'два',
    '3': 'три',
    '4': 'четыре',
    '5': 'пять',
    '6': 'шесть',
    '7': 'семь',
    '8': 'восемь',
    '9': 'девять',
}

from_10_to_19_list = {
    '0': 'десять',
    '1': 'одиннадцать',
    '2': 'двенадцать',
    '3': 'тринадцать',
    '4': 'четырнадцать',
    '5': 'пятнадцать',
    '6': 'шестнадцать',
    '7': 'семнадцать',
    '8': 'восемнадцать',
    '9': 'девятнадцать',
}

second_digits_list = {
    '2': 'двадцать',
    '3': 'тридцать',
    '4': 'сорок',
    '5': 'пятьдесят',
    '6': 'шестьдесят',
    '7': 'семьдесят',
    '8': 'восемьдесят',
    '9': 'девяносто',
}

first_digits_list = {
    '0': '',
    '1': 'сто',
    '2': 'двести',
    '3': 'триста',
    '4': 'четыреста',
    '5': 'пятьсот',
    '6': 'шестьсот',
    '7': 'семьсот',
    '8': 'восемьсот',
    '9': 'девятьсот',
}

last_thousand_list = {
    '0': 'тысяч',
    '1': 'одна тысяча',
    '2': 'две тысячи',
    '3': 'три тысячи',
    '4': 'четыре тысячи',
    '5': 'пять тысяч',
    '6': 'шесть тысяч',
    '7': 'семь тысяч',
    '8': 'восемь тысяч',
    '9': 'девять тысяч'
}


def number_to_string(number: int) -> str:
    if not check_number(number):
        return

    number = divide_number_to_groups(number)

    if len(number) is 1:
        return " ".join(group_to_string(number[0]))
    elif len(number) is 2:
        print()
        group_1 = group_to_string(number[0])

        if len(number[0]) > 1 and number[0][-2] is '1':
            group_1.append(last_thousand_list['0'])
        else:
            group_1 = group_to_string(number[0])[:-1]
            group_1.append(last_thousand_list[number[0][-1]])

        group_2 = group_to_string(number[1])

        return f'{" ".join(group_1)} {" ".join(group_2)}'


def check_number(number: int) -> bool:
    invalid_types = isinstance(number, str) or isinstance(number, bool) or isinstance(number, float)
    out_of_valid_range = number > 999999 or number < 1
    if invalid_types:
        print('ОШИБКА: Недопустимый тип.')
        return False
    elif out_of_valid_range:
        print('ОШИБКА: Число выходит за пределы допустимых значений.')
        return False

    return True


def divide_number_to_groups(number: int) -> list:
    number = list(str(number))
    return list(filter(None, [number[:-3], number[-3:]]))


def group_to_string(group: list) -> list:
    number_of_digits = len(group)

    if number_of_digits is 1:
        return [third_digits_list[group[0]]]
    elif number_of_digits is 2:
        if group[0] is '1':
            return [from_10_to_19_list[group[1]]]
        else:
            second_digit = second_digits_list[group[0]]

            third_digit = third_digits_list[group[1]] if group[1] is not '0' else ''

            return list(filter(None, [second_digit, third_digit]))

    elif number_of_digits is 3:
        first_digit = first_digits_list[group[0]]

        second_digit = ''
        if group[1] is '1':
            second_digit = from_10_to_19_list[group[2]]
        elif group[1] is not '0':
            second_digit = second_digits_list[group[1]]

        third_digit = ''
        if group[1] is '1':
            third_digit = ''
        elif group[2] is not '0':
            third_digit = third_digits_list[group[2]]

        return list(filter(None, [first_digit, second_digit, third_digit]))
