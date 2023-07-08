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

# Open the plain text file whose name is in textfile for reading.
msg = EmailMessage()
msg.set_content('')

# me == the sender's email address
# you == the recipient's email addresss
msg['Subject'] = f'Тестирование email-рассылки'
msg['From'] = sender_mail
msg['To'] = recipient_mail

# add styles to html-content
with open('static\\styles.html', "r", encoding="utf-8") as file:
    styles = file.read()
    msg.add_alternative(styles, subtype='html')

# add logo block to tml-content
with open("static\\logo.html", "r", encoding="utf-8") as file:
    logo = file.read()
    
# code for correct desplaying logo
asparagus_cid = make_msgid()
msg.add_alternative(logo.format(asparagus_cid=asparagus_cid[1:-1]), subtype='html')

with open("static\\images\\corporate-logo.png", 'rb') as img:
    msg.get_payload()[1].add_related(img.read(), 'image', 'jpeg',
                                     cid=asparagus_cid)
    
# add basic content with text to html-content
with open("static\\email_template.html", "r", encoding="utf-8") as file:
    body = file.read()
    msg.add_alternative(body, subtype="html")

asparagus_cid_inst = make_msgid()
with open("static\\footer-inst.html", "r", encoding="utf-8") as file:
    footer = file.read()

msg.add_alternative(footer.format(instagram_icon=asparagus_cid_inst[1:-1]), subtype='html')

with open("static\\images\\instagram-icon.png", 'rb') as img:
    msg.get_payload()[1].add_related(img.read(), 'image', 'jpeg',
                                     cid=asparagus_cid_inst)
    
asparagus_cid_link = make_msgid()
with open("static\\footer-link.html", "r", encoding="utf-8") as file:
    footer = file.read()

msg.add_alternative(footer.format(linkedin_icon=asparagus_cid_link[1:-1]), subtype='html')

with open("static\\images\\linkedin-icon.png", 'rb') as img:
    msg.get_payload()[1].add_related(img.read(), 'image', 'jpeg',
                                     cid=asparagus_cid_link)
    
asparagus_cid_site = make_msgid()
with open("static\\footer-site.html", "r", encoding="utf-8") as file:
    footer = file.read()

msg.add_alternative(footer.format(site_icon=asparagus_cid_site[1:-1]), subtype='html')

with open("static\\images\\site-icon.png", 'rb') as img:
    msg.get_payload()[1].add_related(img.read(), 'image', 'jpeg',
                                     cid=asparagus_cid_site)

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