import argparse

from db_manager import DbManager
from excel_manager import ExcelManager


def run():
    """
    Run the program using the cli inputs
    """
    db_manager = DbManager()
    excel_manager = ExcelManager()
    transactions, columns = db_manager.import_transactions()
    EXCEL_FILE_NAME = "temp"
    excel_manager.build_excel(columns, transactions, EXCEL_FILE_NAME)


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='SQL Python Excel Prototype')
    args = parser.parse_args()

    try:
        run()
    except Exception as e:
        print(e)
