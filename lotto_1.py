import random

# this works but repeats some of same numbers

my_list = []
numbers = list(range(1, 51))

while True:
    new = random.choice(numbers)
    my_list.append(new)
    if len(my_list) == 5:
        print(my_list)
        break
