""" """
import sys
import argparse
import os
from wsgiref import simple_server

sys.path.append(os.getcwd())

from web.app.app import ServerApp

if __name__ == "__main__":

    parser = argparse.ArgumentParser()
    parser.add_argument('--port', type=int, help='server port')
    args = parser.parse_args()

    PORT = args.port or 8000

    app = ServerApp()

    print("Server was started: " + str(PORT))

    httpd = simple_server.make_server('127.0.0.1', PORT, app.app)
    httpd.serve_forever()


