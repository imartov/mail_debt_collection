from redmail import gmail
from dotenv import load_dotenv
import os


def send_email() -> None:

    # get envoirement variables 
    load_dotenv()
    SENDER_EMAIL = os.getenv("SENDER_MAIL")
    EMAIL_SENDER_PASSWORD = os.getenv("MAIL_SENDER_PASSWORD")
    RECIPIENT_EMAIL = os.getenv("RECIPIENT_MAIL")

    # autentification to gmail
    gmail.username = SENDER_EMAIL
    gmail.password = EMAIL_SENDER_PASSWORD

    # get html content
    with open("template\\email_template.html", "r", encoding="utf-8") as file:
        html_content = file.read()

    # send email
    gmail.send(
        subject="Example email",
        receivers=[RECIPIENT_EMAIL],
        html=html_content,
        body_images={
            "corp_logo": "template\\images\\corporate-logo-removebg-preview.png",
            "inst_icon": "template\\images\\instagram-icon.png",
            "link_icon": "template\\images\\linkedin-icon.png",
            "site_icon": "template\\images\\site-icon.png",
        }
    )


if __name__ == "__main__":
    send_email()


