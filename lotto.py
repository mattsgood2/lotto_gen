import sys
# import os
import random
import datetime
import smtplib, ssl
# ########################
# # from senditnow import SendEmail
#
class startup:
    main_numbers_list = []
    stars_numbers_list = []
    main_numbers = list(range(1, 51))
    stars_numbers = list(range(1,10))

    def setup(self):
        self.playing()
        # self.start()
        # self.stars()


    def playing(self):
        play = input("play Y or N").lower()
        if play == "y":
            return self.main()
        if play == "n":
            print("EXIT")
            sys.exit()

    def main(self):
        while True:
            main = random.choice(self.main_numbers)

            if main not in self.main_numbers_list:
                self.main_numbers_list.append(main)

            self.main_numbers_list.sort()

            if len(self.main_numbers_list) == 5:
                self.stars()


    def stars(self):
        while True:
            star = random.choice(self.stars_numbers)

            if star not in self.stars_numbers_list:
                self.stars_numbers_list.append(star)

            self.stars_numbers_list.sort()

            if len(self.stars_numbers_list) == 2:
                self.me()


    def me(self):
        print("m{}, s{}".format(self.main_numbers_list, self.stars_numbers_list))
        sys.exit()


    def __init__(self):
        self.setup()
# from email.mime.text import MIMEText
# from email.mime.multipart import MIMEMultipart
# from twilio.rest import Client
# from dotenv import load_dotenv
# load_dotenv()
#
# ### randomly generates your euro lotto numbers
# ### Working on this app as I dont trust the lotto's lucky dip, least this way I know its Truely random ###
#
# class lotto:
#     main_numbers_list = []
#     stars_numbers_list = []
#     main_numbers = list(range(1, 51))
#     stars_numbers = list(range(1,10))
#
# # sets up the app to run as one unit
    # def setup(self):
    #     self.start_me()
    #     self.stars()
    #     self.print_email_sms()
    #     # self.send_sms()
    #     self.printing()

#
# # randomly creates lotto numbers, and if already in list will not duplicate them
# # Need to add better options on input
# def start_me():
#     while True:
#         main = random.choice(self.main_numbers)
#
#         if main not in self.main_numbers_list:
#             self.main_numbers_list.append(main)
#
#         self.main_numbers_list.sort()
#
#         if len(self.main_numbers_list) == 5:
#             return self.main_numbers_list
        # if yes_no == "n":
        # print("GOODBYE")
            # sys.exit()
            # os.sys("clear")

        # elif yes_no != "y" or "n":
            # print(f'\n *> {yes_no.upper()} <* IS NOT CORRECT, PLEASE ENTER [Y] or [N]')
            # return self.start_me()
            # os.system('clear')
# #
# # # checks and randomly creates lucky star Numbers ##
    # def stars(self):
    #     while True:
    #         star = random.choice(self.stars_numbers)
    #
    #         if star not in self.stars_numbers_list:
    #             self.stars_numbers_list.append(star)
    #
    #         self.stars_numbers_list.sort()
    #
    #         if len(self.stars_numbers_list) == 2:
    #             return self.stars_numbers_list
# #
# # # prints all the main and Lucky stars umbers and formats them nicely
# # ##  Give opton to send email if wanted! ###
# #     def print_email_sms(self):
# #         time_now = datetime.datetime.now()
# #         timestr = time_now.strftime("%c")
# #
# #         main_n_str = str(self.main_numbers_list)
# #         stars_n_str = str(self.stars_numbers_list)
# #
# #         email = input("Send Email [Y] or [N] > ").lower()
# #         if email == "y":
# #             port = 465
# #             smtp_server = "smtp.aol.com"
# #             sender_email = os.getenv("MYEMAIL")
# #             receiver_email = os.getenv("PIMEMAIL")
# #             # receiver_email = input("Enter Email > ")
# #             print(f'\nEmail Sent to {receiver_email}  Check Spam ! ')
# #             password = os.getenv("PASSWORD")
# #             # password = input("Type Your Email Password: ")
# #
# #             message = MIMEMultipart("alternative")
# #             message["Subject"] = "Lotto Numbers"
# #             message["From"] = sender_email
# #             message["To"] = receiver_email
# #
# #             html = """\
# #                 <html>
# #                   <body>
# #                     <p>This weeks Lotto Numbers Are <br>
# #                       {},<br>
# #                     <p>Lucky Stars {},<br>
# #                        Good Luck <br>
# #                        <a href="https://github.com/mattsgood2">The Matts</a>
# #                        How many greats are called Matthew.
# #                     </p>
# #                   </body>
# #                 </html> """.format(main_n_str.strip('[]'), stars_n_str.strip('[]'))
# #
# #             part1 = MIMEText(html, "html")
# #             message.attach(part1)
# #
# #             context = ssl.create_default_context()
# #             with smtplib.SMTP_SSL(smtp_server, port, context=context) as server:
# #                 server.login(sender_email, password)
# #                 server.sendmail(sender_email, receiver_email, message.as_string())
# #
# #
# #             p = open("/Users/matts/mywork/Lotto_numbers.txt", "a")
# #             p.write("\nMain Numbers" + " = " + main_n_str.strip('[]') + ", " + "Lucky Stars" + " = " +
# #                                              stars_n_str.strip('[]') + " | Date Made = " + timestr + "\n")
# #             print(f'\nMain Numbers {main_n_str.strip("[]")} \nLucky Stars * {stars_n_str.strip("[]")}\n')
# #         # print("\nEMAIL SENT ! \n")
# #
# # #send sms with lotto numbers
# #         elif email == "n":
# #
# #     # def send_sms(self):
# #             main_n_str = str(self.main_numbers_list)
# #             # print(main_n_str.strip('[]'))
# #             stars_n_str = str(self.stars_numbers_list)
# #             # print(stars_n_str.strip('[]'))
# #
# #             send_sms = input("SEND SMS ? [Y] or [N] > " ).lower()
# #             if send_sms == "y":
# #                 print("\nSMS SENT !")
# #                 account_sid = os.getenv("TWIL_ACCOUNT_SID")
# #                 auth_token = os.getenv("TWIL_AUTH_TOKEN")
# #                 client = Client(account_sid, auth_token)
# #
# #                 body = f'Lotto Numbers are {main_n_str.strip("[]")}, Lucky Stars {stars_n_str.strip("[]")}'
# #
# #                 message = client.messages \
# #                                 .create(
# #                                      body= body,
# #                                      from_= os.getenv("TWILIO_NUMBER"),
# #                                      to= os.getenv("MY_NUMBER"),
# #                                      # to= input("Enter Number > ")
# #
# #                              )
# #             p = open("/Users/matts/mywork/Lotto_numbers.txt", "a")
# #             p.write("\nMain Numbers" + " = " + main_n_str.strip('[]') + ", " + "Lucky Stars" + " = " +
# #                                              stars_n_str.strip('[]') + " | Date Made = " + timestr + "\n")
# #             print(f'\nMain Numbers {main_n_str.strip("[]")} \nLucky Stars * {stars_n_str.strip("[]")}\n')
# # ### ADD BODY MESSAGE TO OWN MESSAGE ###
# # ### ADD TESTS TO THIS ! ###
# #         elif send_sms == "n":
# #             print("\nGOOD LUCK\n")
# #
# #             p = open("/Users/matts/mywork/Lotto_numbers.txt", "a")
# #             p.write("\nMain Numbers" + " = " + main_n_str.strip('[]') + ", " + "Lucky Stars" + " = " +
# #                                              stars_n_str.strip('[]') + " | Date Made = " + timestr + "\n")
# #             print(f'\nMain Numbers {main_n_str.strip("[]")} \nLucky Stars * {stars_n_str.strip("[]")}\n')
# #
# #             return self.printing
# #
# #     def printing(self):
# #         print("TESTING THIS")
# # # this allows the app to work under one class, with the above setup def
# #
    # def __init__(self):
    #     self.setup()
#
#
#
#
# # calls the app to start
startup()

#
# # To run program in powershell type "python lotto_checking.py"
