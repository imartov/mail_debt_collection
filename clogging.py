'''
This module provides a method for logging
'''

import logging

logging.basicConfig(level=logging.DEBUG, filename="py_log.log",filemode="w",
    format="%(asctime)s %(levelname)s %(message)s")

def clogging(msg:str) -> None:
    logging.info(msg)

def main() -> None:
    ''' this method controls calls to other module methods '''
    pass

if __name__ == "__main__":
    main()