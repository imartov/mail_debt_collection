

def message(debtor_name:str,
            contract_number:str,
            contract_date:str,
            due_date:str,
            debt_period:str) -> str:
    message = f'Тестовое сообщение.\n\
                Используемые переменные:\n\
                - Имя контрагента: {debtor_name}\n\
                - Номер договора: {contract_number}\n\
                - Дата договора: {contract_date}\n\
                - Дата оплаты: {due_date}\n\
                - Срок задолженности: {debt_period}\n\n\
                Если вы получили данное сообщение, значит еmail-рассылка работает!'
    
    return message


def main():
    message()


if __name__ == '__main':
    main()
