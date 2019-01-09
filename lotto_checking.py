import random
import sys
# randomly generates your euro lotto numbers
# need to add lucky stars to the end of the list, maybe with extend.

main_numbers_list = []
main_numbers = list(range(1, 51))
stars_numbers = list(range(1,10))

class TheNumbers():
    print('Would you like to Randomly Gen Euro Lotto numbers ?''\n')

    if input('[Y]es or [N]o  ') == 'y'.lower():
        while True:
            main = random.choice(main_numbers)
            if main not in main_numbers_list:
                main_numbers_list.append(main)

            main_numbers_list.sort()

            if len(main_numbers_list) == 5:
                print (main_numbers_list)
                sys.exit()
        # print(random.choice(numbers))
        # print('Working')
        # sys.exit()
        #
    # else:
    #     print('Thanks for playing See Ya next time')





TheNumbers()
# if already in my_list

# To run program in powershell type python lotto_checking.py
