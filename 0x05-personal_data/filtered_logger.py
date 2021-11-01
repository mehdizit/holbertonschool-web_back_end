#!/usr/bin/env python3
""" RedactingFormatter """

import re
from typing import List
import logging
import mysql.connector
import os

PII_FIELDS = ('name', 'email', 'phone', 'ssn', 'password')



class RedactingFormatter(logging.Formatter):
    """ Redacting Formatter class
        """

    REDACTION = "***"
    FORMAT = "[HOLBERTON] %(name)s %(levelname)s %(asctime)-15s: %(message)s"
    SEPARATOR = ";"

    def __init__(self, fields: List[str]):
        """ constructor """
        self.fields = fields
        super(RedactingFormatter, self).__init__(self.FORMAT)

    def format(self, record: logging.LogRecord) -> str:
        """ generates a log"""
        return filter_datum(self.fields, self.REDACTION, super().format(record), self.SEPARATOR)
        

def get_logger() -> logging.Logger:
    """ returns a logging.Logger object """
    logger = logging.getLogger("user_data")
    logger.setLevel(logging.INFO)
    logger.propagate = False
    handler = logging.StreamHandler()
    handler.setFormatter(RedactingFormatter(PII_FIELDS))
    logger.addHandler(handler)
    return logger


def filter_datum(fields: List[str], redaction: str, message: str, separator: str) -> str:
    """ function that return log message obfustucated """
    lst = message.split(separator)

    for f in fields:
        for i in range(len(lst)):
            if lst[i].startswith(f):
                subst = f + '=' + redaction
                lst[i] = re.sub(lst[i], '', lst[i])
                lst[i] = subst
    return separator.join(lst)


def get_db() -> mysql.connector.connection.MySQLConnection:
    """returns a connector to the database"""
    cnx = mysql.connector.connect(user= os.getenv('PERSONAL_DATA_DB_USERNAME'), password= os.getenv('PERSONAL_DATA_DB_PASSWORD', ''), host= os.getenv('PERSONAL_DATA_DB_HOST', 'localhost'), database= os.getenv('PERSONAL_DATA_DB_NAME', 'root'))
    return cnx


def main():
    """ display each row under a filtered format """
    db = get_db()
    cursor = db.cursor()
    cursor.execute("SELECT * FROM users;")
    result = cursor.fetchall()
    for row in result:
        message = f"name={row[0]}; " + \
                  f"email={row[1]}; " + \
                  f"phone={row[2]}; " + \
                  f"ssn={row[3]}; " + \
                  f"password={row[4]};"
        print(message)
        log_record = logging.LogRecord("my_logger", logging.INFO,
                                       None, None, message, None, None)
        formatter = RedactingFormatter(PII_FIELDS)
        formatter.format(log_record)
    cursor.close()
    db.close()


if __name__ == "__main__":
    main()
