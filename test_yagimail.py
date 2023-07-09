import yagmail, os
from dotenv import load_dotenv


def send_message() -> None:

    load_dotenv()
    sender_mail = os.getenv('SENDER_MAIL')
    mail_sender_password = os.getenv('MAIL_SENDER_PASSWORD')
    recipient_mail = "alexandr.kosyrew@mail.ru"

    yagmail.register(sender_mail, mail_sender_password)
    yag = yagmail.SMTP(sender_mail)

    with open("static\\footer.html", "r", encoding="utf-8") as file:
        html_content = file.read()

    html_content += str([yagmail.inline("static\images\instagram-icon.png")])

    yag.send(to=recipient_mail,
             subject="Тестрование email-рассылки",
             contents=html_content)


def main():
    send_message()


if __name__ == "__main__":
    main()