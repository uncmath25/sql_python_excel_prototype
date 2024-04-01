import argparse
import os
import pymysql
import xlsxwriter


class SqlPythonExcelManager():
    """
    Manager for querying sql and building an excel workbook
    """

    def __init__(self):
        """
        Initializes db credentials
        """
        self._DB_USER = str(os.environ['DB_USER'])
        self._DB_PASSWORD = str(os.environ['DB_PASSWORD'])
        self._DB_HOST = str(os.environ['DB_HOST'])
        self._DB_PORT = int(os.environ['DB_PORT'])
        self._DB_DATABASE = str(os.environ['DB_DATABASE'])
        print(f'username: {self._DB_USER}')
        print(f'password: {self._DB_PASSWORD}')
        print(f'host: {self._DB_HOST}')
        print(f'port: {self._DB_PORT}')
        print(f'database: {self._DB_DATABASE}')

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
    
    def _import_transactions(self):
        """
        Imports the transaction data
        """
        IMPORT_TRANSACTIONS_QUERY = 'SELECT * FROM transactions'
        return self._query_database(IMPORT_TRANSACTIONS_QUERY)[0]
    
    def _build_sample_excel(self):
        """
        Builds a sample excel
        """
        workbook = xlsxwriter.Workbook('/temp/hello.xlsx')
        worksheet = workbook.add_worksheet()
        worksheet.write('A1', 'Hello world')
        workbook.close()
    
    def build_excel(self):
        """
        Build the excel workbook using the database
        """
        print("Running Sql Python Excel Prototype!")
        print(self._import_transactions())
        self._build_sample_excel()


def run():
    """
    Run the program using the cli inputs
    """
    manager = SqlPythonExcelManager()
    manager.build_excel()


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='SQL Python Excel Prototype')
    args = parser.parse_args()

    try:
        run()
    except Exception as e:
        print(e)
