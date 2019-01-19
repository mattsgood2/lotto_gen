import random
# randomly generates your euro lotto numbers
# need to add lucky stars to the end of the list, maybe with extend.

# main_numbers_list = []
# stars_numbers_list = []
# main_numbers = list(range(1, 51))
# stars_numbers = list(range(1,10))

### Working on this app as i dont trust the lotto lucky dip least this way I know its Truely random ###
#### Needs alot of re-write due to it being not the best ###


### checkes main bumbers are not already within the list if not then prints out ###
class lotto:

    main_numbers_list = []
    stars_numbers_list = []
    main_numbers = list(range(1, 51))
    stars_numbers = list(range(1,10))

    def setup(self):
        self.lotto_num()
        self.stars()
        self.printing()

    def lotto_num(self):

        if input('\nWould you like to Randomly Gen Euro Lotto numbers ? [Y]es or [N]o -->  ') == 'y'.lower():
            while True:
                main = random.choice(self.main_numbers)

                if main not in self.main_numbers_list:
                    self.main_numbers_list.append(main)

                self.main_numbers_list.sort()

                if len(self.main_numbers_list) == 5:
                    return self.main_numbers_list
                    break

## checks and randomly gens lucky star Numbers ##
    def stars(self):

        if input('\nWould You like some Lucky Stars ? --> [Y]es or [N]o ') == 'y'.lower():
            while True:
                star = random.choice(self.stars_numbers)

                if star not in self.stars_numbers_list:
                    self.stars_numbers_list.append(star)

                self.stars_numbers_list.sort()

                if len(self.stars_numbers_list) == 2:
                    return self.stars_numbers_list
                    break
### prints all the main numbers and Lucky stars ###
    def printing(self):
        print('\nMain Numbers {} \nLucky Stars * {} \n'.format(self.main_numbers_list, self.stars_numbers_list))

    def __init__(self):
        self.setup()

lotto()

# lotto_num()
# stars()
# printing()
# if already in my_list

# To run program in powershell type python lotto_checking.py
