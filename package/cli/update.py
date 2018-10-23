"""The module for update data from aliexpress """
from package.aliexpress.request_parser.parser import AliExpressParserRequest
from package.db.import_data import DBImport


class UpdateCli:
    @staticmethod
    def run(self):
        PARSER_REQUEST = AliExpressParserRequest()
        data = PARSER_REQUEST.get_last_data()

        DB_IMPORT = DBImport()
        DB_IMPORT.import_data(data)
