import sys
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


class lotto:
    main_numbers_list = []
    stars_numbers_list = []
    main_numbers = list(range(1, 51))
    stars_numbers = list(range(1,10))

# sets up the app to run as one unit
    def setup(self):
        self.start_me()
        # self.lotto_num()
        self.stars()
        self.print_email()
        # self.sending_email_out()


# randomly creates lotto numbers, and if already in list will not duplicate them
# Need to add better options on input
    def start_me(self):
        # try:
        yes_no = input('\nGenerate Euro Lotto numbers ? [Y]es or [N]o -->  ').lower()
### need to add try except for input ###
        if yes_no == "n":
            print("GOODBYE")
            sys.exit()
        elif yes_no == "y":
            print("Lets GO !!")

            while True:
                main = random.choice(self.main_numbers)

                if main not in self.main_numbers_list:
                    self.main_numbers_list.append(main)

                self.main_numbers_list.sort()

                if len(self.main_numbers_list) == 5:
                    return self.main_numbers_list


# checks and randomly creates lucky star Numbers ##
    def stars(self):
        while True:
            star = random.choice(self.stars_numbers)

            if star not in self.stars_numbers_list:
                self.stars_numbers_list.append(star)

            self.stars_numbers_list.sort()

            if len(self.stars_numbers_list) == 2:
                return self.stars_numbers_list

# prints all the main and Lucky stars umbers and formats them nicely
###  Give opton to send email if wanted! ###
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

        email = input("Email Me [Y]es or [N]o > ")
        if email == "y":
            print("Email Sent")
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
        elif email == "n":
            print("\n   **! Write Them Down !** \n")


#send sms with lotto numbers
    # def send_sms(self):
        send_sms = input("Send me a Text ? [Y],[N]")
        if send_sms == "y":
            print("SENT SMS")
            account_sid = os.getenv["ACCOUNT_SID"]
            auth_token = os.getenv["AUTH_TOKEN"]
            client = Client(account_sid, auth_token)

            body = "Hi your lotto numbers are {0} Lucky Stars {1} today ".format(self.main_numbers_list,
                                                                        self.stars_numbers_list)

            message = client.messages.create(
                body = body,
                to =os.environ['MY_NUMBER'], #Should be reservation.phone_number,
                from_ = os.environ['TWILIO_NUMBER'],
            )
        else:
            sys.exit()
        # print(message.sid)
            # pass




# this allows the app to work under one class, with the above setup def
    def __init__(self):
        self.setup()

# calls the app to start
lotto()

# To run program in powershell type "python lotto_checking.py"
