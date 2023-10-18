
print('Hello World')

fruit_list = ['apple', 'banana', 'peach']

for fruit in fruit_list:
    print(fruit)

import random

num_list = []

for i in range(0, 9):
    num = random.randint(1, 10)
    num_list += [num]

print(num_list)

is_apple = False

for fruit in fruit_list:
    if fruit == 'apple':
        is_apple = True
    else:
        is_apple = False
    print(is_apple)

