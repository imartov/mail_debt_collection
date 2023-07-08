
import smtplib, ssl, os
from dotenv import load_dotenv
from email.mime.text import MIMEText

import smtplib

from email.message import EmailMessage
from email.headerregistry import Address
from email.utils import make_msgid


# def mail_sending(message:str, recipient_mail:str) -> None:
    
#     load_dotenv()
#     sender_mail = os.getenv('SENDER_MAIL')
#     mail_sender_password = os.getenv('MAIL_SENDER_PASSWORD')

#     server = smtplib.SMTP("smtp.gmail.com", 587)
#     server.starttls()

#     server.login(user=sender_mail, password=mail_sender_password)

#     with open("static\\email_template.html", "r", encoding="utf-8") as file:
#         message = file.read()

#     msg = MIMEText(message, "html")
#     msg["From"] = sender_mail
#     msg["To"] = recipient_mail
#     msg["Subject"] = "Тестиование массовой рассылки"

#     server.sendmail(from_addr=sender_mail,
#                     to_addrs=recipient_mail,
#                     msg=msg.as_string())
    
#     print("The message was sent successfuly")


def mail_sending(message:str, recipient_mail:str) -> None:
    
    load_dotenv()
    msg = EmailMessage()

    sender_mail = os.getenv('SENDER_MAIL')
    mail_sender_password = os.getenv('MAIL_SENDER_PASSWORD')
    
    msg['Subject'] = "Ayons asperges pour le déjeuner"
    msg['From'] = Address("Alivaria Brevery", "pepe", "example.com")
    msg['To'] = (Address("Penelope Pussycat", "penelope", recipient_mail),)
    
    with open("static\\email_template.html", "r", encoding="utf-8") as file:
        email_content = file.read()

    msg.set_content(email_content)
    asparagus_cid = make_msgid()
    msg.add_alternative("""\
    <html>
    <head></head>
    <body>
        <p>Salut!</p>
        <p>Cela ressemble à un excellent
            <a href="http://www.yummly.com/recipe/Roasted-Asparagus-Epicurious-203718">
                recipie
            </a> déjeuner.
        </p>
        <img src="cid:{asparagus_cid}" />
    </body>
    </html>
    """.format(asparagus_cid=asparagus_cid[1:-1]), subtype='html')

    with open("static\\corporate-logo.png", 'rb') as img:   
        msg.get_payload()[1].add_related(img.read(), 'image', 'png',
                                     cid=asparagus_cid)
        
    with open('outgoing.msg', 'wb') as f:
        f.write(bytes(msg))

    with smtplib.SMTP('localhost') as s:
        s.send_message(msg)


def main():
    mail_sending(message=None, recipient_mail="alexandr.kosyrew@mail.ru")


if __name__ == '__main__':
    main()