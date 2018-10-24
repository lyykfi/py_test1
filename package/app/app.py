import falcon

from package.app.routes.category import CategoryResource


class ServerApp(object):
    app = None

    def __init__(self):
        self.app = falcon.API()

    def start(self):
        self.app.add_route('/category', CategoryResource())
