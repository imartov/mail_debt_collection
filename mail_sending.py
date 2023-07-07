
import smtplib, ssl, os
from dotenv import load_dotenv
from email.mime.text import MIMEText


def mail_sending(message:str, recipient_mail:str) -> None:
    
    load_dotenv()
    sender_mail = os.getenv('SENDER_MAIL')
    mail_sender_password = os.getenv('MAIL_SENDER_PASSWORD')

    server = smtplib.SMTP("smtp.gmail.com", 587)
    server.starttls()

    server.login(user=sender_mail, password=mail_sender_password)

    with open("index.html", "r", encoding="utf-8") as file:
        message = file.read()

    msg = MIMEText(message, "html")
    msg["From"] = sender_mail
    msg["To"] = recipient_mail
    msg["Subject"] = "Тестиование массовой рассылки"

    server.sendmail(from_addr=sender_mail,
                    to_addrs=recipient_mail,
                    msg=msg.as_string())
    
    print("The message was sent successfuly")


# def mail_sending(message:str, recipient_mail:str) -> None:
    
#     load_dotenv()
#     from email.message import EmailMessage
#     from email.utils import make_msgid
#     import mimetypes

#     msg = EmailMessage()

#     # generic email headers
#     msg['Subject'] = 'Hello there'
#     msg['From'] = 'ABCD <abcd@xyz.com>'
#     msg['To'] = 'PQRS <pqrs@xyz.com>'

#     # set the plain text body
#     msg.set_content('This is a plain text body.')

#     # now create a Content-ID for the image
#     image_cid = make_msgid(domain='xyz.com')
#     # if `domain` argument isn't provided, it will 
#     # use your computer's name

#     # set an alternative html body
#     msg.add_alternative("""\
#     <html>
#         <body>
#             <p>This is an HTML body.<br>
#             It also has an image.
#             </p>
#             <img src="cid:{image_cid}">
#         </body>
#     </html>
#     """.format(image_cid=image_cid[1:-1]), subtype='html')

#     with open('path/to/image.jpg', 'rb') as img:

#     # know the Content-Type of the image
#         maintype, subtype = mimetypes.guess_type(img.name)[0].split('/')

#     # attach it
#         msg.get_payload()[1].add_related(img.read(), 
#                                          maintype=maintype, 
#                                          subtype=subtype, 
#                                          cid=image_cid)


def main():
    mail_sending(message=None, recipient_mail="alexandr.kosyrew@mail.ru")


if __name__ == '__main__':
    main()