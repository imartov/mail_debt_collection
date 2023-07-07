import json
from mail_sending import mail_sending


def get_data():
    ''' connection to database '''
    
    with open('test_data.json', 'r', encoding='utf-8') as file:
        data = json.load(file)
    
    for name, debtor_data in data.items():
        if 'Sasha' in name:

            recipient_mail = debtor_data["recipient_mail"]

            with open('text_message.txt', 'r', encoding='utf-8') as file:
                text_message = file.read()

            text_message = text_message.format(debtor_name=debtor_data["debtor_name"],
                                            contract_number=debtor_data["contract_number"],
                                            contract_date=debtor_data["contract_date"],
                                            due_date=debtor_data["due_date"],
                                            debt_period=debtor_data["debt_period"])
            
            mail_sending(message=text_message, recipient_mail=recipient_mail)


def main():
    get_data()


if __name__ == "__main__":
    main()