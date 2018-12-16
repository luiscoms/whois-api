import json
from tornado.testing import AsyncHTTPTestCase

import app


class StatusHandlerTest(AsyncHTTPTestCase):

    def get_app(self):
        return app.make_app()

    def test_status(self):
        response = self.fetch('/status')
        self.assertEqual(response.code, 200)
        json_response = json.loads(response.body.decode('utf-8'))
        self.assertIn("version", json_response)
