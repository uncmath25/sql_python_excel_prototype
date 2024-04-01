import os
import string
import xlsxwriter


class ExcelManager():
    """
    Manager for building the excel spreadsheet
    """
    _XLSX_EXT = "xlsx"

    def __init__(self):
        """
        Initializes db credentials
        """
        self._OUTPUT_DIR = str(os.environ['OUTPUT_DIR'])

    def _build_full_path(self, file_name):
        """
        Builds the appropriate xlsx full path
        """
        return os.path.join(self._OUTPUT_DIR, file_name) + "." + ExcelManager._XLSX_EXT
    
    @staticmethod
    def _convert_idx_to_column(idx):
        """
        Converts the select index to the appropriate column character
        """
        return string.ascii_uppercase[idx]
    
    @staticmethod
    def _build_excel_data(worksheet, columns, transactions):
        """
        Builds the excel data
        """
        for i, col in enumerate(columns):
            worksheet.write(f'{ExcelManager._convert_idx_to_column(i)}1', col)
        for i, transaction in enumerate(transactions):
            for j, x in enumerate(transaction):
                worksheet.write(f'{ExcelManager._convert_idx_to_column(j)}{i + 2}', x)

    def build_excel(self, columns, transactions, output_file_name):
        """
        Build the excel spreadsheet using the given transaction data
        """
        workbook = xlsxwriter.Workbook(self._build_full_path(output_file_name))
        worksheet = workbook.add_worksheet()
        ExcelManager._build_excel_data(worksheet, columns, transactions)
        workbook.close()
