import unittest
from app import blueprint
from gevent.pywsgi import WSGIServer

from app.main import create_app

app = create_app('dev')


app.app_context().push()
app.register_blueprint(blueprint)


def run():
    app.debug = True
    http_server = WSGIServer(('', 5000), app)
    http_server.serve_forever()


def test():
    """Runs the unit tests."""
    tests = unittest.TestLoader().discover('app/test', pattern='test*.py')
    result = unittest.TextTestRunner(verbosity=2).run(tests)
    if result.wasSuccessful():
        return 0
    return 1


if __name__ == '__main__':
    run()
