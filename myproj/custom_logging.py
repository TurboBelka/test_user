import logging
import requests


class MyCustomHandler(logging.Handler):
    def handle(self, record):
        response = requests.post(
            "http://127.0.0.1:8000/index/log/",
            data={'log': record.getMessage()}
        )
        return response
