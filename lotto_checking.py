import random
import sys
# randomly generates your euro lotto numbers
# need to add lucky stars to the end of the list, maybe with extend.

main_numbers_list = []
stars_numbers_list = []
main_numbers = list(range(1, 51))
stars_numbers = list(range(1,10))

class TheNumbers():
    print('Would you like to Randomly Gen Euro Lotto numbers ?''\n')

    if input('[Y]es or [N]o  ') == 'y'.lower():
        while True:
            main = random.choice(main_numbers)
            stars = random.choice(stars_numbers)

            if main not in main_numbers_list:
                main_numbers_list.append(main)
                if stars not in stars_numbers_list:
                    stars_numbers_list.append(stars)


            main_numbers_list.sort()
            stars_numbers_list.sort()

            if len(main_numbers_list) == 5:
                print(main_numbers_list)
                if len(stars_numbers_list) == 2:
                    print (main_numbers_list, stars_numbers_list)
                    print (main_numbers_list)


                sys.exit()


TheNumbers()
# if already in my_list

# To run program in powershell type python lotto_checking.py
