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
            number_str = third_digits_list[number[0]]
        elif number_of_digits is 2:
            if number[0] is '1':
                number_str = from_10_to_19_list[number[1]]
            else:
                second_digit = second_digits_list[number[0]]

                third_digit = third_digits_list[number[1]] if number[1] is not '0' else ''

                number_str = f'{second_digit} {third_digit}'.strip()

        elif number_of_digits is 3:
            first_digit = first_digits_list[number[0]]

            second_digit = ''
            if number[1] is '1':
                second_digit = from_10_to_19_list[number[2]]
            elif number[1] is not '0':
                second_digit = second_digits_list[number[1]]

            third_digit = ''
            if number[1] is '1':
                third_digit = ''
            elif number[2] is not '0':
                third_digit = third_digits_list[number[2]]

            first_and_second_digits = f'{first_digit} {second_digit}'.strip()
            number_str = f'{first_and_second_digits} {third_digit}'.strip()

    return number_str


def check_number(number: int) -> bool:
    if number > 999999 or number < 1:
        print('Число выходит за пределы допустимых значений.')
        return False

    return True


def divide_number_to_groups(number: int) -> list:
    number = list(str(number))
    return list(filter(None, [number[:-3], number[-3:]]))



num = 111
print(number_to_string(num))
