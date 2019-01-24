import random
import datetime
### randomly generates your euro lotto numbers
### need to add lucky stars to the end of the list, maybe with extend.
### added ability to create lucky stars
### Working on this app as i dont trust the lotto's lucky dip, least this way I know its Truely random ###
### Needs alot of re-write due to it being not the best ###
### have re-wrote to create all under a class ###

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
# randomly creates lotto numbers, and if already in list will not duplicate them
        if input('\nWould you like to Randomly Gen Euro Lotto numbers ? [Y]es or [N]o -->  ') == 'y'.lower():
            while True:
                main = random.choice(self.main_numbers)

                if main not in self.main_numbers_list:
                    self.main_numbers_list.append(main)

                self.main_numbers_list.sort()

                if len(self.main_numbers_list) == 5:
                    return self.main_numbers_list
                    break

# checks and randomly creates lucky star Numbers ##
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
# prints all the main and Lucky stars umbers and formats them nicely
# going to add function to write to file to keep track of lotto numbers drawn
# also will add datetime to show when numbers were drawn
    def printing(self):
        time_now = datetime.datetime.now()
        p = open("/Users/matts/mywork/Lotto_numbers.txt", "a")
        p.write("\nMain Numbers" + "-" + str(self.main_numbers_list) + "-" + "Lucky Stars" + str(self.stars_numbers_list) + " " + str(time_now) + "\n")
        print('\nMain Numbers {} \nLucky Stars * {}\n '.format(self.main_numbers_list, self.stars_numbers_list))
        # print(time_now)
#################################
# Print to File, will print the lotto numbers to a File
#  def ptf ():
# ...     name = input("name > ")
# ...     n = open("ptf.txt", 'a')
# ...     n.write(name + "\n")
#above was testing in powershell
    def ptf(self):

        pass





#################################
# this allows the app to work under one class
    def __init__(self):
        self.setup()

# calls the app to start
lotto()

# To run program in powershell type "python lotto_checking.py"
