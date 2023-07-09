import yagmail, os, base64
from dotenv import load_dotenv


def send_message() -> None:

    load_dotenv()
    sender_mail = os.getenv('SENDER_MAIL')
    mail_sender_password = os.getenv('MAIL_SENDER_PASSWORD')
    recipient_mail = "alexandr.kosyrew@mail.ru"

    yagmail.register(sender_mail, mail_sender_password)
    yag = yagmail.SMTP(sender_mail)

    with open("static_base64\\output.html", "r") as file:
        html_content = file.read()

    yag.send(to=recipient_mail,
             subject="Тестрование email-рассылки",
             contents=html_content)


def main():
    send_message()


if __name__ == "__main__":
    main()