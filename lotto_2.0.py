import random

# this works fixed the repeats with (sample) and changed the (append)
# to (extend) works fine

my_list = list(range(1,51))
your_nums = []

while True:
    your_nums = random.choice(my_list)
    if len(your_nums) == 5:
        print(your_nums)
        break
