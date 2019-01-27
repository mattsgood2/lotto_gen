import random
import datetime
import smtplib, ssl
#### randomly generates your euro lotto numbers
### need to add lucky stars to the end of the list, maybe with extend.
### added ability to create lucky stars
### Working on this app as i dont trust the lotto's lucky dip, least this way I know its Truely random ###
### Needs alot of re-write due to it being not the best ###
### have re-wrote to create all under a class ###
### Will add an email function, to email you your numbers if needed
### will also add a sms function, to send sms with lotto Numbers


class lotto:

    main_numbers_list = []
    stars_numbers_list = []
    main_numbers = list(range(1, 51))
    stars_numbers = list(range(1,10))

# sets up the app to run as one unit
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
        timestr = time_now.strftime("%c")

        p = open("/Users/matts/mywork/Lotto_numbers.txt", "a")
        p.write("\nMain Numbers" + "-" + str(self.main_numbers_list) + "-" + "Lucky Stars" +
                                         str(self.stars_numbers_list) + " " + timestr + "\n")
        print('\nMain Numbers {} \nLucky Stars * {}\n '.format(self.main_numbers_list, self.stars_numbers_list))

#################################
# Email setup

# import smtplib, ssl

# port = 465  # For SSL
# smtp_server = "smtp.aol.com"
# sender_email = "mattsgood2@aol.com"  # Enter your address
# receiver_email = "lillypim@aol.com"  # Enter receiver address
# password = input("Type your password and press enter: ")
# message = """\
# Subject: Hi there
#
# This message is sent from Python."""
#
# context = ssl.create_default_context()
# with smtplib.SMTP_SSL(smtp_server, port, context=context) as server:
#     server.login(sender_email, password)
#     server.sendmail(sender_email, receiver_email, message)
#################################
# this allows the app to work under one class, with the above setup def
    def __init__(self):
        self.setup()

# calls the app to start
lotto()

# To run program in powershell type "python lotto_checking.py"
