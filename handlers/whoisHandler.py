import json
import tornado.web
from tornado.gen import coroutine

from helpers.date_transform import datetimeSerializer


class WhoisHandler(tornado.web.RequestHandler):
    def initialize(self, account_service, queue_service, *args, **kwargs):
        self.account_service = account_service
        self.queue_service = queue_service

    @coroutine
    def get(self, cpf, *args, **kwargs):
        who = yield self.account_service.by_cpf(cpf)
        if not who:
            self.set_status(404)
            return

        yield self.queue_service.enqueue(who)
        self.write(json.dumps(who, default=datetimeSerializer))

    def set_default_headers(self):
        self.set_header('Content-Type', 'application/json')
        self.set_header('Cache-Control', 'max-age=10')
        self.set_header('Expires', '0')
        # CORS
        self.set_header("Access-Control-Allow-Headers", "*")
        self.set_header("Access-Control-Allow-Origin", "*")
        self.set_header("Access-Control-Allow-Credentials", "true")
        self.set_header("Access-Control-Allow-Method", "GET, OPTIONS")
