import requests
import json
import secrets
from random import randrange
from hashlib import sha256

def req_endpoint(endpoint, data=None, port=5000):
    base_url = f'http://localhost:{port}'
    url = f'{base_url}{endpoint}'
    is_post = any(kwd in endpoint for kwd in ['transactions/new', 'nodes/register'])
    if is_post:
        print('POST')
        req = requests.post(url, json=data)
    else:
        print('GET')
        req = requests.get(url)
    return req.json()


def simulate_transaction(sender=False, recipient=False, amount=False):
    sender = secrets.token_hex(16) if not sender else sender
    recipient = secrets.token_hex(16) if not recipient else recipient
    amount = randrange(1,100) if not amount else amount
    transaction = {
        'sender': sender,
        'recipient': recipient,
        'amount': amount
    }
    return transaction


nodes = {
    'nodes': [f'http://localhost:{i}' for i in range(5000, 5020)]
}

req_endpoint('/transactions/new', data=simulate_transaction('quan', 'alvaro', 666))
req_endpoint('/mine')
req_endpoint('/chain')