import os
import random
import datetime
import smtplib, ssl
########################
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from twilio.rest import Client
from dotenv import load_dotenv
load_dotenv()

########################
### randomly generates your euro lotto numbers
### need to add lucky stars to the end of the list, maybe with extend.
### added ability to create lucky stars
### Working on this app as I dont trust the lotto's lucky dip, least this way I know its Truely random ###
### Needs alot of re-write due to it being not the best ###
### have re-wrote to create all under a class ###
### Will add an email function, to email you your numbers if needed
### will also add a sms function, to send sms with lotto Numbers

### Not account_sid
# account_sid = 'AC361c9f44a26a8546c0f01a10b4e46d49' # dummie account_sid #
# auth_token = 'your_auth_token'
# client = Client(account_sid, auth_token)



class lotto:
    main_numbers_list = []
    stars_numbers_list = []
    main_numbers = list(range(1, 51))
    stars_numbers = list(range(1,10))

# sets up the app to run as one unit
    def setup(self):
        self.lotto_num()
        self.stars()
        self.print_email()
        # self.sending_email_out()

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
                    # break

# checks and randomly creates lucky star Numbers ##
    def stars(self):
    # if input('\nWould You like some Lucky Stars ? --> [Y]es or [N]o ') == 'y'.lower():
        while True:
            star = random.choice(self.stars_numbers)

            if star not in self.stars_numbers_list:
                self.stars_numbers_list.append(star)

            self.stars_numbers_list.sort()

            if len(self.stars_numbers_list) == 2:
                return self.stars_numbers_list
                    # break
# prints all the main and Lucky stars umbers and formats them nicely

    def print_email(self):
        time_now = datetime.datetime.now()
        timestr = time_now.strftime("%c")

        main_n_str = str(self.main_numbers_list)
        # print(main_n_str.strip('[]'))
        stars_n_str = str(self.stars_numbers_list)
        # print(stars_n_str.strip('[]'))

        p = open("/Users/matts/mywork/Lotto_numbers.txt", "a")
        p.write("\nMain Numbers" + " = " + main_n_str.strip('[]') + ", " + "Lucky Stars" + " = " +
                                         stars_n_str.strip('[]') + " | Date Made = " + timestr + "\n")
        print('\nMain Numbers {} \nLucky Stars * {}\n '.format(
                                                    main_n_str.strip('[]'),
                                                    stars_n_str.strip('[]'))
                                                    )

        port = 465
        smtp_server = "smtp.aol.com"
        sender_email = os.getenv("MYEMAIL")
        receiver_email = os.getenv("PIMEMAIL")
        password = os.getenv("PASSWORD")
        # password = input("Type Your Email Password: ")

        message = MIMEMultipart("alternative")
        message["Subject"] = "Lotto Numbers"
        message["From"] = sender_email
        message["To"] = receiver_email

        html = """\
            <html>
              <body>
                <p>This weeks Lotto Numbers Are <br>
                  {},<br>
                <p>Lucky Stars {},<br>
                   Good Luck <br>
                   <a href="https://github.com/mattsgood2">The Matts</a>
                   How many greats are called Matthew.
                </p>
              </body>
            </html> """.format(main_n_str.strip('[]'), stars_n_str.strip('[]'))

        part1 = MIMEText(html, "html")
        message.attach(part1)

        context = ssl.create_default_context()
        with smtplib.SMTP_SSL(smtp_server, port, context=context) as server:
            server.login(sender_email, password)
            server.sendmail(sender_email, receiver_email, message.as_string())

#send sms with lotto numbers
    def send_sms(self):
        pass

# this allows the app to work under one class, with the above setup def
    def __init__(self):
        self.setup()

# calls the app to start
lotto()

# To run program in powershell type "python lotto_checking.py"
