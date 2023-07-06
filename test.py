import os
from dotenv import load_dotenv

def test():
    sender_mail = os.getenv('SENDER_MAIL')
    mail_sender_password = os.getenv('MAIL_SENDER_PASSWORD')

    print(sender_mail, '\n', mail_sender_password)


if __name__ == '__main__':
    load_dotenv()
    test()