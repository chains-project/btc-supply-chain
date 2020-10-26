#!/usr/bin/python3
"""
Checks all known sha256 checksums in the bitcoin software supply chain.

https://github.com/monperrus/btc-supply-chain
"""

import glob
import json
import requests
import hashlib
import os
from urllib.parse import urlparse

json_files = []
json_files += glob.glob("db/wallets/*")
json_files += glob.glob("db/full-nodes/*")


for i in json_files:
    wallet = json.load(open(i))
    versions = wallet["versions"]
    
    # for Bitcoin Core, we only check the last ones in in CI, otherwise it takes too much time
    if wallet['name'] and len(versions)>4 == "Bitcoin Core": versions = versions[-4]
    
    for v in versions:
        for source in v['sources']:
          a = urlparse(source)
          fname = os.path.basename(a.path)
          local_file = "target/"+fname
          if not os.path.exists(local_file):
            r = requests.get(source, allow_redirects=True)
            if r.status_code == 404:
              raise Exception("HTTP 404 on "+source)
            open(local_file, 'wb').write(r.content)
            
          # now we have the file locally
          # computing the sha256
          sha256 = hashlib.sha256(open(local_file, 'rb').read())
          
          if sha256.hexdigest() != v['sha256']:
            raise Exception("Under attack! SHA256 does not match " + source)

          print(source + ": verified")

        


