basic = {
    '1': 'один',
    '2': 'дв',
    '3': 'три',
    '4': 'четыр',
    '5': 'пят',
    '6': 'шест',
    '7': 'сем',
    '8': 'восем',
    '9': 'девят',
}


def number_to_string(number: int) -> str:
    str_number = ''

    return str_number


def check_number(number: int) -> bool:
    if number > 999999 or number < 1:
        print('Число выходит за пределы допустимых значений.')
        return False

    return True


def divide_number_to_groups(number: int) -> list:
    number = list(str(number))
    return [number[:-3], number[-3:]]



num = 206667
var = check_number(num)
print('answer: ' + str(var))