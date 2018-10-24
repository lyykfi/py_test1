""" """
import sys
import os
from wsgiref import simple_server

sys.path.append(os.getcwd())

from package.app.app import ServerApp

if __name__ == "__main__":
    PORT = 8000

    app = ServerApp()
    app.start()

    print("Server was started: " + str(PORT))

    httpd = simple_server.make_server('127.0.0.1', PORT, app.app)
    httpd.serve_forever()


