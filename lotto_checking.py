import random

# randomly generates your euro lotto numbers
# need to add lucky stars to the end of the list, maybe with extend.

my_list = []
numbers = list(range(1, 51))

def checking_my_list():
    while True:
        new = random.choice(numbers)
        if new in my_list:
            return new
        elif new not in my_list:
            my_list.append(new)

        my_list.sort()

        if len(my_list) == 5:
            print (my_list)


checking_my_list()
# if already in my_list
