import os
from typing import Dict

import requests


class OMDbAPIClient:
    def fetch(self, title):
        return requests.get(self._get_request_url(title)).json()

    def _get_request_url(self, title):
        api_key = os.environ["OMDB_API_KEY"]
        return f"http://www.omdbapi.com/?t={title}&apikey={api_key}"
