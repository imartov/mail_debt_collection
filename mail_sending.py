
import smtplib, ssl, os
from dotenv import load_dotenv
from email.mime.text import MIMEText


# def mail_sending(message:str, recipient_mail:str) -> None:

#     message = 'текстывсвы'.decode('utf-8')
    
#     # sender_mail = os.getenv('SENDER_MAIL')
#     # mail_sender_password = os.getenv('MAIL_SENDER_PASSWORD')

#     sender_mail = "pythontest285@gmail.com"
#     mail_sender_password = "hhyblqqkvgtjoadq"

#     server = smtplib.SMTP("smtp.gmail.com", 587)
#     server.starttls()

#     server.login(user=sender_mail, password=mail_sender_password)

#     msg = MIMEText(message)
#     msg["Subject"] = "Тестиование массовой рассылки для направления электронных претензий"

#     server.sendmail(from_addr=sender_mail,
#                     to_addrs=recipient_mail,
#                     msg=message)


def mail_sending(message:str, recipient_mail:str) -> None:
    port = 587  # For SSL
    smtp_server = "smtp.gmail.com"
    sender_mail = os.getenv('SENDER_MAIL')
    # recipient_mail = "alexandr.kosyrew@mail.ru"
    mail_sender_password = os.getenv('MAIL_SENDER_PASSWORD')
    # message = """\
    # Subject: Hi there
    # Отправка сообщения, тест\n
    # This message is sent from Python."""

    # context = ssl.create_default_context()
    # with smtplib.SMTP_SSL(smtp_server, port, context=context) as server:

    server = smtplib.SMTP("smtp.gmail.com", 587)
    server.starttls()

    server.login(user=sender_mail, password=mail_sender_password)
    server.send_message(msg=message, from_addr=sender_mail, to_addrs=recipient_mail)


def main():
    load_dotenv()
    # my_msg = 'отправка текстового сообщения'
    # message = '{}'.format(my_msg).encode('utf-8')
    mail_sending()


if __name__ == '__main__':
    main()