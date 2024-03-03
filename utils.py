from sqlalchemy import select
from sqlquery import clients
from sqlquery import engine


class GetUniqueClientData:

    def __init__(self, key_name: str, client_data: list) -> None:
        self.client_data = client_data
        self.key_name = key_name

    def get_exist_unp_list(self) -> list:
        stmt = select(clients.c[str(self.key_name)])
        with engine.connect() as connection:
            result = list(connection.execute(stmt))
        result = [item[0] for item in result]
        return result

    def get_unp_from_input_client_data(self) -> list:
        return [item[self.key_name] for item in self.client_data]
    
    def get_unique(self, from_list:list, exclude_list:list) -> list:
        return [item for item in from_list if item not in exclude_list]

    def get_data_by_key(self, keys_list:list, from_list:list) -> list:
        result_data = []
        for item in from_list:
            if item[self.key_name] in keys_list:
                result_data.append(item)
        return result_data
    
    def run(self) -> list:
        exist_unp_list = self.get_exist_unp_list()
        input_unp_list = self.get_unp_from_input_client_data()
        unique_unp_list = self.get_unique(from_list=input_unp_list, exclude_list=exist_unp_list)
        return self.get_data_by_key(keys_list=unique_unp_list, from_list=self.client_data)


def main() -> None:
    pass

if __name__ == "__main__":
    main()