from redmail import gmail
from redmail import outlook
from dotenv import load_dotenv
import os


def send_email(recipient_mail:str, debtor_name:str, debt_amount:int, due_date:str) -> None:

    # get envoirement variables 
    load_dotenv()
    SENDER_EMAIL = os.getenv("SENDER_MAIL")
    EMAIL_SENDER_PASSWORD = os.getenv("MAIL_SENDER_PASSWORD")

    # autentification to gmail
    outlook.username = 'byclaimservice@alivaria.by'
    outlook.password = '@sE3c5U@'

    # get html content
    with open("template\\email_template.html", "r", encoding="utf-8") as file:
        html_content = file.read()

    # send email
    outlook.send(
        subject="Example email",
        receivers=[recipient_mail],
        html=html_content,

        # pass addresses to images in html-layout
        body_images={
            "corp_logo": "template\\images\\corporate-logo-removebg-preview.png",
            "inst_icon": "template\\images\\instagram-icon.png",
            "link_icon": "template\\images\\linkedin-icon.png",
            "site_icon": "template\\images\\site-icon.png",
        },
        
        # pass values of variables in html-layout
        body_params={
            "debtor_name": debtor_name,
            "debt_amount": debt_amount,
            "due_date": due_date,
        }
    )


def main() -> None:
    # get envoirement variables 
    load_dotenv()
    RECIPIENT_EMAIL = os.getenv("RECIPIENT_MAIL")

    # run function
    send_email(recipient_mail='alexandr.kosyrew1@gmail.com',
               debtor_name="Козырев Александр",
               debt_amount=12345,
               due_date="12.12.2021")

if __name__ == "__main__":
    main()

    


