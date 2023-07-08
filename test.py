# Import smtplib for the actual sending function
import smtplib, os
from dotenv import load_dotenv

# Import the email modules we'll need
from email.message import EmailMessage
from email.utils import make_msgid

load_dotenv()
sender_mail = os.getenv('SENDER_MAIL')
mail_sender_password = os.getenv('MAIL_SENDER_PASSWORD')
recipient_mail = "alexandr.kosyrew@mail.ru"

textfile = "text_message.txt"

# Open the plain text file whose name is in textfile for reading.
with open(textfile, "r", encoding="utf-8") as fp:
    # Create a text/plain message
    msg = EmailMessage()
    msg.set_content('')

# me == the sender's email address
# you == the recipient's email addresss
msg['Subject'] = f'The contents of {textfile}'
msg['From'] = sender_mail
msg['To'] = recipient_mail

with open("static\\logo.html", "r", encoding="utf-8") as file:
    logo = file.read()
    
asparagus_cid = make_msgid()
msg.add_alternative(logo.format(asparagus_cid=asparagus_cid[1:-1]), subtype='html')

with open("static\\corporate-logo.png", 'rb') as img:
    msg.get_payload()[1].add_related(img.read(), 'image', 'jpeg',
                                     cid=asparagus_cid)
    
with open("static\\email_template.html", "r", encoding="utf-8") as file:
    body = file.read()
    msg.add_alternative(body, subtype="html")

server = smtplib.SMTP("smtp.gmail.com", 587)
server.starttls()

server.login(user=sender_mail, password=mail_sender_password)

# Send the message via our own SMTP server.
server.sendmail(from_addr=sender_mail,
                    to_addrs=recipient_mail,
                    msg=msg.as_string())


test_html = """\
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
"""