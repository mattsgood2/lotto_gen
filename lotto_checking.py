import random
import sys
# randomly generates your euro lotto numbers
# need to add lucky stars to the end of the list, maybe with extend.

my_list = []
numbers = list(range(1, 51))

class TheNumbers():
    print('Would you like to Randomly Gen Euro Lotto numbers ?''\n')

    if input('[Y]es or [N]o  ') == 'y'.lower():
        print(random.choice(numbers))
        # print('Working')
        # sys.exit()
        #
    else:
        print('Thanks for playing See Ya next time')





TheNumbers()
# if already in my_list

# To run program in powershell type python lotto_checking.py
