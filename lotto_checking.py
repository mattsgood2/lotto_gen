import random
# randomly generates your euro lotto numbers
# need to add lucky stars to the end of the list, maybe with extend.

main_numbers_list = []
stars_numbers_list = []
main_numbers = list(range(1, 51))
stars_numbers = list(range(1,10))

### Working on this app as i dont trust the lotto lucky dip least this way I know its Truely random ###
#### Needs alot of re-write due to it being not the best ###


### checkes main bumbers are not already within the list if not then prints out ###
def lotto_num():

    if input('\nWould you like to Randomly Gen Euro Lotto numbers ? [Y]es or [N]o -->  ') == 'y'.lower():
        while True:
            main = random.choice(main_numbers)

            if main not in main_numbers_list:
                main_numbers_list.append(main)

            main_numbers_list.sort()

            if len(main_numbers_list) == 5:
                return main_numbers_list
                break

## checks and randomly gens lucky star Numbers ##
def stars():

    if input('\nWould You like some Lucky Stars ? --> [Y]es or [N]o ') == 'y'.lower():
        while True:
            star = random.choice(stars_numbers)

            if star not in stars_numbers_list:
                stars_numbers_list.append(star)

            stars_numbers_list.sort()

            if len(stars_numbers_list) == 2:
                return stars_numbers_list
                break
### prints all the main numbers and Lucky stars ###
def printing():
    print('\nMain Numbers {} \nLucky Stars * {} \n'.format(main_numbers_list, stars_numbers_list))


lotto_num()
stars()
printing()
# if already in my_list

# To run program in powershell type python lotto_checking.py
