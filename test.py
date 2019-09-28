import numpy as np

from main import number_to_string

# hand_number = 771675
# print(f'{hand_number}: {number_to_string(hand_number)}')

valid_data = np.random.randint(1, 999999, 5)
for number in valid_data:
    print(f'{number}: {number_to_string(number)}')

try:
    string = "тест"
    print(f'{string}: {number_to_string(string)}')
except TypeError as e:
    print(e)

negative_int = -1
print(f'{negative_int}: {number_to_string(negative_int)}')

large_int = 1000000
print(f'{large_int}: {number_to_string(large_int)}')

boolean = True
print(f'{boolean}: {number_to_string(boolean)}')

floating_number = 1.24
print(f'{floating_number}: {number_to_string(floating_number)}')
