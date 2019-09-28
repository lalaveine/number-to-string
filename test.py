import numpy as np

from main import number_to_string

integers = np.random.randint(1, 999999, 5)
for number in integers:
    print(f'{number}: {number_to_string(number)}')
