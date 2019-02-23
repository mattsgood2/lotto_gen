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

### randomly generates your euro lotto numbers
### Working on this app as I dont trust the lotto's lucky dip, least this way I know its Truely random ###

class lotto:
    main_numbers_list = []
    stars_numbers_list = []
    main_numbers = list(range(1, 51))
    stars_numbers = list(range(1,10))

# sets up the app to run as one unit
    def setup(self):
        self.start_me()
        self.stars()
        self.print_email_sms()
        self.send_sms()

# randomly creates lotto numbers, and if already in list will not duplicate them
# Need to add better options on input
    def start_me(self):
        yes_no = input('\nGenerate Euro Lotto numbers ? [Y]es or [N]o -->  ').lower()

        if yes_no == "n":
            print("GOODBYE")
            sys.exit()
        if yes_no == "y":
            print("Lets GO !!")
        elif yes_no != "y" or "n":
            print(f' {yes_no} IS NOT CORRECT, PLEASE ENTER [Y] or [N]')
            return self.start_me()

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
    def print_email_sms(self):
        time_now = datetime.datetime.now()
        timestr = time_now.strftime("%c")

        main_n_str = str(self.main_numbers_list)
        stars_n_str = str(self.stars_numbers_list)

        p = open("/Users/matts/mywork/Lotto_numbers.txt", "a")
        p.write("\nMain Numbers" + " = " + main_n_str.strip('[]') + ", " + "Lucky Stars" + " = " +
                                         stars_n_str.strip('[]') + " | Date Made = " + timestr + "\n")
        print(f'\nMain Numbers {main_n_str.strip("[]")} \nLucky Stars * {stars_n_str.strip("[]")}\n')

        email = input("Email Me [Y]es or [N]o > ")
        if email == "y":
            print("Email Sent")
            port = 465
            smtp_server = "smtp.aol.com"
            sender_email = os.getenv("MYEMAIL")
            # receiver_email = os.getenv("PIMEMAIL")
            receiver_email = input("Enter Email > ")
            # print("Email Sent to ")
            print(f'\nEmail Sent to {receiver_email}\nCheck Spam ! ')
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
            # f'{main_n_str.strip("[]")},{stars_n_str.strip("[]")}'


            context = ssl.create_default_context()
            with smtplib.SMTP_SSL(smtp_server, port, context=context) as server:
                server.login(sender_email, password)
                server.sendmail(sender_email, receiver_email, message.as_string())
        elif email == "n":
            print("\n   **! Write Them Down !** \n")
        # else:
        #     raise TypeError
        # print(f'{email} is not a Valid input')

#send sms with lotto numbers
    def send_sms(self):
        main_n_str = str(self.main_numbers_list)
        # print(main_n_str.strip('[]'))
        stars_n_str = str(self.stars_numbers_list)
        # print(stars_n_str.strip('[]'))

        send_sms = input("SEND SMS ? [Y] or [N] > " ).lower()
        if send_sms == "y":
            print("\nSMS SENT !")
            account_sid = os.getenv("TWIL_ACCOUNT_SID")
            auth_token = os.getenv("TWIL_AUTH_TOKEN")
            client = Client(account_sid, auth_token)

            body = f'Lotto Numbers are {main_n_str.strip("[]")}, Lucky Stars {stars_n_str.strip("[]")}'

            message = client.messages \
                            .create(
                                 body= body,
                                 from_= os.getenv("TWILIO_NUMBER"),
                                 to= os.getenv("MY_NUMBER"),
                                 # to= input("Enter Number > ")

                         )
### ADD BODY MESSAGE TO OWN MESSAGE ###
### ADD TESTS TO THIS ! ###
        elif send_sms == "n":
            print("\nGOOD LUCK\n")

# this allows the app to work under one class, with the above setup def
    def __init__(self):
        self.setup()


# calls the app to start
lotto()

# To run program in powershell type "python lotto_checking.py"
