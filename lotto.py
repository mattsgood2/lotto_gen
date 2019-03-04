import sys
import time
import os
import random
import datetime
import smtplib, ssl
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from twilio.rest import Client
from dotenv import load_dotenv
load_dotenv()


class startup:
    main_numbers_list = []
    stars_numbers_list = []
    main_numbers = list(range(1, 51))
    stars_numbers = list(range(1,10))

    def setup(self):
        self.playing()

### Generates Lotto Numbers ###
    def playing(self):
        os.system('cls')
        play = input("\n Generate Euro Number [Y] or [N] > ").lower()
        if play == "y":
            print("\n Lets Pick ! \n")
            time.sleep(1),self.main()

        if play == "n":
            print("\n EXIT, GOODBYE !\n")
            sys.exit()

        if play != "y" or "n":
            print("\n ENTER [Y]es or [N]o ! \n")
            self.playing()

### Checks if You Want Email ###
    def send_email_now(self):
        email = input("\n Send Email, [Y] or [N] > ").lower()

        if email == "y":
            print("\n Lets Send This Email")
            time.sleep(1),self.send_email()

        if email == "n":
            self.to_file()

        if email != "y" or "n":
            print("\n ENTER [Y]es or [N]o ! \n")
            self.send_email_now()


### Input for Sending SMS ###
    def sending_sms(self):
        send_text = input("\n SEND SMS [Y] or [N] > ").lower()
        if send_text == "y":
            self.send_sms()

        if send_text == "n":
            print("\n GOODLUCK \n")
            sys.exit()

        if send_text != "y" or "n":
            print("\n ENTER [Y]es or [N]o ! \n")
            self.sending_sms()

### Generates the Main Numbers ###
    def main(self):
        while True:
            main = random.choice(self.main_numbers)

            if main not in self.main_numbers_list:
                self.main_numbers_list.append(main)

            self.main_numbers_list.sort()

            if len(self.main_numbers_list) == 5:
                self.stars()

### Generates the Lucky Stars ###
    def stars(self):
        while True:
            star = random.choice(self.stars_numbers)

            if star not in self.stars_numbers_list:
                self.stars_numbers_list.append(star)

            self.stars_numbers_list.sort()

            if len(self.stars_numbers_list) == 2:
                os.system('cls')
                self.print_nums()

### Prints The Numbers Out ###
    def print_nums(self):
        print(f'\n\n Main Numbers {str(self.main_numbers_list).strip("[]")} Stars {str(self.stars_numbers_list).strip("[]")}')
        # print("\nGOODLUCK !\n")
        self.send_email_now()


### Sends The Email Out ###
    def send_email(self):
        main_n_str = str(self.main_numbers_list)
        stars_n_str = str(self.stars_numbers_list)

        port = 465
        smtp_server = "smtp.aol.com"
        sender_email = os.getenv("MYEMAIL")
        receiver_email = os.getenv("PIMEMAIL")
        # receiver_email = input("Enter Email > ")
        print(f'\nEmail Sent to {receiver_email}  Check Spam ! \n')
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
            self.to_file()
            # sys.exit()

### Copies to a File ###
    def to_file(self):
        time_now = datetime.datetime.now()
        timestr = time_now.strftime("%c")

        main_n_str = str(self.main_numbers_list)
        stars_n_str = str(self.stars_numbers_list)

        p = open("/Users/matts/mywork/Lotto_take_2.txt", "a")
        p.write("\nMain Numbers" + " = " + main_n_str.strip('[]') + ", " + "Lucky Stars" + " = " +
                                         stars_n_str.strip('[]') + " | Date Made = " + timestr + "\n")
        time.sleep(.600),print("\n COPY TO FILE")
        self.sending_sms()
        # print(f'\nMain Numbers {main_n_str.strip("[]")} \nLucky Stars * {stars_n_str.strip("[]")}\n')

    def send_sms(self):
        main_n_str = str(self.main_numbers_list)
        stars_n_str = str(self.stars_numbers_list)

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

        print("\n SMS AWAY !!!\n")
        time.sleep(.600),print("\n\n GOODLUCK")




    def __init__(self):
        self.setup()

# # calls the app to start
startup()

#
# # To run program in powershell type "python lotto_checking.py"
