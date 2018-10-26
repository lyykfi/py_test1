"""The module for update data from aliexpress """

from cli.logger.cli import LoggerCli
from cli.request_parser.parser import AliExpressParserRequest
from web.db.import_data import DBImport


class UpdateCli:
    @staticmethod
    def run():
        logger = LoggerCli()
        logger.debug("Start update db...")

        PARSER_REQUEST = AliExpressParserRequest()
        data = PARSER_REQUEST.get_last_data()

        DB_IMPORT = DBImport()
        DB_IMPORT.import_data(data)

        logger.debug("Db updated")
