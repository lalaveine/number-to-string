last_digit = {
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

from_10_to_19 = {
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

second_digit = {
    '2': 'двадцать',
    '3': 'тридцать',
    '4': 'сорок',
    '5': 'пятьдесят',
    '6': 'шестьдесят',
    '7': 'семьдесят',
    '8': 'восемьдесят',
    '9': 'девяносто',
}

def number_to_string(number: int) -> str:
    if not check_number(number):
        print("Закрываю программу...")
        exit()

    number = divide_number_to_groups(number)
    print(number)
    number_str = None

    if len(number) is 1:
        number = number[0]
        number_of_digits = len(number)

        if number_of_digits is 1:
            number_str = last_digit[number[0]]
        elif number_of_digits is 2:
            if number[0] is not '1':
                number_str = f'{second_digit[number[0]]} {last_digit[number[1]]}'
            else:
                number_str = from_10_to_19[number[1]]

    return number_str


def check_number(number: int) -> bool:
    if number > 999999 or number < 1:
        print('Число выходит за пределы допустимых значений.')
        return False

    return True


def divide_number_to_groups(number: int) -> list:
    number = list(str(number))
    return list(filter(None, [number[:-3], number[-3:]]))



num = 17
print(number_to_string(num))
