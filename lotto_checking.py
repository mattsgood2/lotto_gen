import random
import sys
# randomly generates your euro lotto numbers
# need to add lucky stars to the end of the list, maybe with extend.

main_numbers_list = []
stars_numbers_list = []
main_numbers = list(range(1, 51))
stars_numbers = list(range(1,10))

class TheNumbers():
    # print('Would you like to Randomly Gen Euro Lotto numbers ?''\n')
    if input('Would you like to Randomly Gen Euro Lotto numbers ? [Y]es or [N]o -->  ') == 'y'.lower():
        while True:
            main = random.choice(main_numbers)
            stars = random.choice(stars_numbers)

            if main not in main_numbers_list:
                main_numbers_list.append(main)

            main_numbers_list.sort()

            if len(main_numbers_list) == 5:
                print('main_numbers {}, '.format(main_numbers_list))
                # print('Would you like some Lucky Stars ?')
                if input('Would you like some Lucky Stars ? yes or no--> ')== 'y':
                    print('great choice')
                    break
                    # if input()=='n'.lower():
                    #     print('Goodbye')
                    #     break
                # user_input = input()
                # if user_input == 'n'.lower():
                #     print("Goodbye")
                #     break
                    # if input == 'n'.lower():

                        # print('Goodbye')

                        # break
                # print('GOOD LUCK')

        #######################################################################

            # if stars not in stars_numbers_list:
            #     stars_numbers_list.append(stars)
            #     stars_numbers_list.sort()
            #     if len(stars_numbers_list) == 2:
            #         print('lucky stars {}, '.format(stars_numbers_list))






TheNumbers()
# if already in my_list

# To run program in powershell type python lotto_checking.py
