import logging
import logging.config
import tornado.httpserver
import tornado.ioloop
import tornado.options
import tornado.web
from os import getenv

from dotenv import load_dotenv, find_dotenv
from tornado.httpserver import HTTPServer
from tornado.ioloop import IOLoop
from tornado.options import define, options

from config.factories import config
from config.loader import Loader
from dao.factories import mysql_factory
from handlers.healthcheckHandler import HealthcheckHandler
from handlers.statusHandler import StatusHandler
from handlers.whoisHandler import WhoisHandler
from services.factories import account_service_factory, queue_service_factory

__version__ = '0.0.0'


def make_app():
    define("port", default=8080, help="run on the given port", type=int)

    define("logging_config_path",
           default=getenv('LOGGING_CONFIG_PATH', 'config/logging-local.yml'),
           help="Path of logging config file",
           type=str)

    define("app_config_path",
           default=getenv('GATEWAY_CONFIG_PATH', 'config/local.yml'),
           help="Path of gateway config file",
           type=str)

    tornado_conf_path = getenv('TORNADO_CONFIG_PATH', 'config/tornado-local.conf')
    tornado.options.parse_config_file(tornado_conf_path)

    load_dotenv(find_dotenv())

    configLoader = Loader()
    logging_config = configLoader.load_from_file(options.logging_config_path)
    logging.config.dictConfig(logging_config)

    app_conf = configLoader.load_from_file(options.app_config_path)

    config.override(app_conf)

    tornado.options.parse_command_line()

    return tornado.web.Application(handlers=[
        (r'/(?:status)?', StatusHandler, dict(version=__version__)),
        (r'/health(check)?', HealthcheckHandler, dict(
            version=__version__,
            mysql=mysql_factory(),
        )),
        (r'/whois/(?P<cpf>[0-9]{11})', WhoisHandler, dict(
            account_service=account_service_factory(),
            queue_service=queue_service_factory()
        )),
    ])


if __name__ == "__main__":
    app = make_app()

    http_server = HTTPServer(app)
    http_server.listen(options.port)

    logger = logging.getLogger(__name__)
    logger.info("Listening on TCP port %d", options.port)

    # Execution will block here until Ctrl+C (Ctrl+Break on Windows) is pressed.
    try:
        IOLoop.instance().start()
    except (KeyboardInterrupt, SystemExit):
        pass
