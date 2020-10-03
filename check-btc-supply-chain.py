#!/usr/bin/python3
"""
Checks all known checksums and signatures in the bitcoin software supply chain.

https://github.com/monperrus/btc-supply-chain
"""

import glob
import json
import requests

for i in glob.glob("wallets/*"):
    wallet = json.load(open(i))
    for v in wallet["versions"]:
        print(v)
        # TODO check sha512 sum
        signature_url = requests.get(v['signature_url'])

        # TODO check signature
        


