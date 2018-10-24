import falcon

from web.app.router_list import ROUTES


class ServerApp(object):
    app = None

    def __init__(self):
        self.app = falcon.API()
        for router in ROUTES:
            self.app.add_route(router['path'], router['router'])

