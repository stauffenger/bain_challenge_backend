import random

import requests

from utils import log

# The Nominatim doesn't accept the default User-Agent from the requests library. (https://operations.osmfoundation.org/policies/nominatim/)
# Ideally, you should build your own Nominatim. (https://nominatim.org/release-docs/develop/admin/Installation/)
# "Auto-complete search This is not yet supported by Nominatim and you must not implement such a service on the client side using the API."
# Random user agent code: https://www.zenrows.com/blog/python-requests-user-agent#random-user-agent
user_agents = [
    'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Safari/537.36'
    'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Safari/537.36'
    'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36'
    'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36'
    'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36'
    'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/16.1 Safari/605.1.15'
    'Mozilla/5.0 (Macintosh; Intel Mac OS X 13_1) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/16.1 Safari/605.1.15'
]

def get_latitude_longitude(address):
    headers = {'User-Agent': random.choice(user_agents)}
    response = requests.get('https://nominatim.openstreetmap.org/search', headers=headers, params={ "q": address, "format": "jsonv2" })
    if response.status_code == 200:
        return response.json()
    else:
        log.write(f"Erro while trying to retireve the address '{address}' geolocation.")
        raise NameError(response.status_code, response.text)