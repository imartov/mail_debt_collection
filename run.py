import logging
from get_data import get_data
from utils import GetUniqueClientData
from sqlquery import TransformData
from sqlquery import clients
from sqlquery import insert_data


logging.basicConfig(level=logging.DEBUG, filename="py_log.log",filemode="a",
                    format="%(asctime)s %(levelname)s %(message)s")

def run() -> None:
    recipients = get_data()
    transformdrecipients = TransformData(input_data=recipients).clients()
    uniqueclientdata = GetUniqueClientData(key_name="unp", client_data=transformdrecipients).run()
    logging.info(uniqueclientdata)
    if uniqueclientdata:
        insert_data(table_name=clients, insert_data=uniqueclientdata)

def main() -> None:
    run()

if __name__ == "__main__":
    main()
