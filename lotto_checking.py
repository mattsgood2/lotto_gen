import random

# import sys
# randomly generates your euro lotto numbers
# need to add lucky stars to the end of the list, maybe with extend.

main_numbers_list = []
stars_numbers_list = []
main_numbers = list(range(1, 51))
stars_numbers = list(range(1,10))


# print('Would you like to Randomly Gen Euro Lotto numbers ?''\n')
def lotto_num():

    if input('Would you like to Randomly Gen Euro Lotto numbers ? [Y]es or [N]o -->  ') == 'y'.lower():
        while True:
            main = random.choice(main_numbers)

            if main not in main_numbers_list:
                main_numbers_list.append(main)

            main_numbers_list.sort()

            if len(main_numbers_list) == 5:
                return main_numbers_list
                break

##checks and randomly gens lucky star Numbers##
def stars():

    if input('Would You like some Lucky Stars ? --> [Y]es or [N]o ') == 'y'.lower():
        while True:
            star = random.choice(stars_numbers)

            if star not in stars_numbers_list:
                stars_numbers_list.append(star)

            stars_numbers_list.sort()

            if len(stars_numbers_list) == 2:
                return stars_numbers_list
                # print('Thanks For Using Me, Bye ! ')
                break

def printing():
    print('Main Numbers {} \nLucky Stars * {} \n'.format(main_numbers_list, stars_numbers_list))


lotto_num()
stars()
printing()
# TheNumbers()
# if already in my_list

# To run program in powershell type python lotto_checking.py
