import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart



# Gmail credentials (for the email that will be sending the notifications)
app_email_address = "robotplantnotifs@gmail.com"
app_password = "gytn kjvy trhg tpnp"



class Emailnotif:
    # def menu(self):
    #     print("1. Send email")
    #     print("2. Exit")
    #     while True:
    #         choice = input("Enter your choice: ")
    #         if choice == "1":
    #             self.email_contents()
    #             self.create_email()
    #             self.connect_to_server()
    #         elif choice == "2":
    #             print("Exit")
    #             break

    @staticmethod
    def email_contents():
        subject = "You need watering', baby I'm not foolin'"
        body = "Leaves are falling all around, it's time I was watering my plant. Thanks to you I'm much obliged for such a pleasant plant"
        return subject, body

    @staticmethod
    def create_email(email):
        subject, body = Emailnotif.email_contents()
        msg = MIMEMultipart()
        msg['From'] = app_email_address
        msg['To'] = email
        msg['Subject'] = subject
        msg.attach(MIMEText(body, 'plain'))
        text = msg.as_string()
        return text
    
    @staticmethod
    def connect_to_server(email):
        try:
            email_contents = Emailnotif.create_email(email)
            with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smpt:
                smpt.login(app_email_address, app_password)
                smpt.sendmail(app_email_address, email, email_contents)
                print("Email sent")
        except Exception as e:
            print(f"Error: {e}")


def all_email_func():
    Emailnotif.email_contents()
    Emailnotif.create_email()
    Emailnotif.connect_to_server()

