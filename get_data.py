import json
from main import send_email


def get_data() -> None:
    ''' connection to database '''
    
    # open file with debtors and save data in data variable
    with open('test_data.json', 'r', encoding='utf-8') as file:
        data = json.load(file)
    
    # run send_email function and pass ti it params
    for name, debtor_data in data.items():
        send_email(recipient_mail=debtor_data["recipient_mail"],
                   debtor_name=debtor_data["debtor_name"],
                   debt_amount=debtor_data["debt_amount"],
                   due_date=debtor_data["due_date"])


def main():
    get_data()


if __name__ == "__main__":
    main()