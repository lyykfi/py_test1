from web.app.routes.category import CategoryResource

ROUTES = [
    {
        'path': '/category',
        'router': CategoryResource()
    }
]