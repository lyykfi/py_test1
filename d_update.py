import os
from time import sleep

import json_config
from daemonize import Daemonize

from cli.logger.cli import LoggerCli
from cli.update import UpdateCli

config = json_config.connect('./config/daemon.json')

work_dir = os.getcwd()

def main():
    while True:
        os.chdir(work_dir)
        UpdateCli.run()
        sleep(5*60)

daemon = Daemonize(
    app="test_app",
    pid=config["PIDFILE"],
    action=main,
    keep_fds=LoggerCli().get_fds(),
    verbose=True)
daemon.start()