import smtplib, os
from dotenv import load_dotenv
from email.message import EmailMessage
from email.utils import make_msgid


# test function
def send_email() -> None:

    # get envoirement variables 
    load_dotenv()
    sender_mail = os.getenv("SENDER_MAIL")
    mail_sender_password = os.getenv("MAIL_SENDER_PASSWORD")
    recipient_mail = os.getenv("RECIPIENT_MAIL")

    # Open the plain text file whose name is in textfile for reading.
    msg = EmailMessage()
    msg.set_content('')

    # set email headers
    msg['Subject'] = f'Email-sending Testing'
    msg['From'] = sender_mail
    msg['To'] = recipient_mail

    # list of files that will add to html-context
    html_files = ["static\\styles.html",
                  "static\\logo.html",
                  "static\\email_template.html",
                  "static\\footer-inst.html",
                  "static\\footer-link.html",
                  "static\\footer-site.html"]

    full_html_conntent = ""
    for html_file in html_files:
        print(html_file)

        # if html file contains image (<img src="...">) element
        if html_file in ["static\\logo.html", "static\\footer-inst.html", "static\\footer-link.html", "static\\footer-site.html"]:

            # set path to image for every html file with images element
            if html_file == "static\\logo.html":
                path_pic = "static\\images\\corporate-logo.png"
            elif html_file == "static\\footer-inst.html":
                path_pic = "static\\images\\instagram-icon.png"
            elif html_file == "static\\footer-link.html":
                path_pic = "static\\images\\linkedin-icon.png"
            elif html_file == "static\\footer-site.html":
                path_pic = "static\\images\\site-icon.png"

            # add to msg html content of evry file with image
            with open(html_file, "r", encoding="utf-8") as file:
                content_html = file.read()
                msg.add_alternative(content_html, subtype='html')
                full_html_conntent += content_html

            # code for correct desplaying logo from documentation and examples
            asparagus_cid = make_msgid()
            msg.add_alternative(content_html.format(asparagus_cid=asparagus_cid[1:-1]), subtype='html')

            with open(path_pic, 'rb') as img:
                msg.get_payload()[1].add_related(img.read(), 'image', 'jpeg',
                                                cid=asparagus_cid)
                
        # if html file don't contains any images
        else:
            with open(html_file, "r", encoding="utf-8") as file:
                html_content = file.read()
                msg.add_alternative(html_content, subtype='html')
                full_html_conntent += html_content

    with open("static\\outpute_email.html", "w", encoding="utf-8") as file:
        file.write(full_html_conntent)

    server = smtplib.SMTP("smtp.gmail.com", 587)
    server.starttls()

    server.login(user=sender_mail, password=mail_sender_password)

    server.sendmail(from_addr=sender_mail,
                    to_addrs=recipient_mail,
                    msg=msg.as_string())


if __name__ == '__main__':
    send_email()