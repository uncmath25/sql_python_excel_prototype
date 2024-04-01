import os
import pymysql


class DbManager():
    """
    Manager for querying the database
    """
    _TRANSACTIONS_TABLE = "transactions"

    def __init__(self):
        """
        Initializes db credentials
        """
        self._DB_USER = str(os.environ['DB_USER'])
        self._DB_PASSWORD = str(os.environ['DB_PASSWORD'])
        self._DB_HOST = str(os.environ['DB_HOST'])
        self._DB_PORT = int(os.environ['DB_PORT'])
        self._DB_DATABASE = str(os.environ['DB_DATABASE'])

    def _query_database(self, query):
        """
        Queries the mysql database and returns any fetched data
        """
        conn = pymysql.connect(user=self._DB_USER, passwd=self._DB_PASSWORD, host=self._DB_HOST,
                               port=self._DB_PORT, database=self._DB_DATABASE, local_infile=True)

        cur = conn.cursor()
        cur.execute(query)
        data = cur.fetchall()
        if cur.description is not None:
            column_names = [str(row[0]) for row in cur.description]
        else:
            column_names = None

        cur.close()
        conn.commit()
        conn.close()

        return(data, column_names)
    
    def import_transactions(self):
        """
        Imports the transaction data
        """
        IMPORT_TRANSACTIONS_QUERY = f'SELECT * FROM {DbManager._TRANSACTIONS_TABLE}'
        return self._query_database(IMPORT_TRANSACTIONS_QUERY)
