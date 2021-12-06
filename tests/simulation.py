import requests
import secrets
from random import randrange
from hashlib import sha256
import random
import matplotlib.pyplot as plt

def req_endpoint(endpoint, port=5000, data=None):
    # Check valid request
    get_reqs = ['/nodes/resolve', '/chain', '/mine', '/wallets']
    post_reqs = ['/nodes/register', '/transaction']
    if endpoint not in get_reqs + post_reqs:
        print('invalid request')
        return -1
    # Determine request address and method
    base_url = f'http://127.0.0.1:{port}'
    url = f'{base_url}{endpoint}'
    is_post = any(kwd in endpoint for kwd in post_reqs)
    if is_post:
        if data is None:
            print('POST requests required data')
            return -1
        else:
            req = requests.post(url, json=data)
    else:
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


### Simulation

def who_doesit(p=.5):
    return int(random.random() < p)

# Spawn nodes
# NOTE: do this in terminal
nodes_uuids = ['alice', 'bob']
nodes_dict = dict(zip(nodes_uuids, range(5000, 5000+len(nodes_uuids))))

# Register nodes
nodes_register_body = {
    'nodes': [f'http://127.0.0.1:{i}' for i in range(5000, 5000+len(nodes_uuids))]
}
for node_port in nodes_dict.values():
    req_endpoint('/nodes/register', port=node_port, data=nodes_register_body)

# Simulation
balances = []
periods = range(0, 10)

for t in periods:
    # Transaction
    sender = nodes_uuids[who_doesit(.1)]
    recipient = [n for n in nodes_uuids if n != sender].pop()
    req_endpoint(
        '/transaction',
        data=simulate_transaction(sender, recipient, random.uniform(0, .5))
    )
    # Mine
    miner = nodes_uuids[who_doesit(0)]
    req_endpoint(
        '/mine',
        port=nodes_dict.get(miner)
    )
    # Consensus
    for node_port in nodes_dict.values():
        req_endpoint('/nodes/resolve', port=node_port)
    # Record balances
    wallets = req_endpoint(
        '/wallets'
    )
    balances.append([x.get('balance') for x in wallets.values()])

# Unpack and plot balances
alice, bob = zip(*balances)
plt.plot(alice, label='alice')
plt.plot(bob, label='bob')
plt.legend()
plt.show()