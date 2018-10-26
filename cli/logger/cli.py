"""The module for update data from aliexpress """
import datetime
import logging

import json_config
from singleton_decorator import singleton

@singleton
class LoggerCli:
    logger = logging.getLogger(__name__)

    def __init__(self):
        config = json_config.connect('./config/log.json')

        self.logger.setLevel(logging.DEBUG)
        self.fh = logging.FileHandler(config["file"], "w")
        self.fh.setLevel(logging.DEBUG)
        self.logger.addHandler(self.fh)


    def get_fds(self):
        return [self.fh.stream.fileno()]

    def debug(self, text):
        date = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        self.logger.debug('{} {}'.format(date, text))
