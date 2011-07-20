from gaesessions import SessionMiddleware

# Make webapp.template use django 1.2
webapp_django_version = '1.2'

def webapp_add_wsgi_middleware(app):
    app = SessionMiddleware(app, cookie_key="some really long string")
    return app