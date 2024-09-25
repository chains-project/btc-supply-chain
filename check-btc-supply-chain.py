#!/usr/bin/python
"""
Checks all known sha256 checksums in the bitcoin software supply chain.

https://github.com/monperrus/btc-supply-chain
"""

import glob
import hashlib
import json
import os
import urllib.request
from urllib.parse import urlparse

from packaging import version

json_files = []
json_files += glob.glob("db/wallets/*.json")
json_files += glob.glob("db/full-nodes/*.json")

for i in json_files:
    wallet = json.load(open(i))
    versions = wallet["versions"]

    last_version = sorted(
        [v["version_number"] for v in versions], key=lambda x: version.parse(x)
    )[-1]

    for v in versions:
        # we only CI the last added version
        if v["version_number"] != last_version:
            continue

        for source in v["sources"]:
            a = urlparse(source)
            fname = os.path.basename(a.path)
            local_file = "target/" + fname
            if not os.path.exists(local_file):

                # Identify this user-agent so server does not reject
                opener = urllib.request.build_opener()
                opener.addheaders = [("User-Agent", "CheckBTC/1.0")]
                urllib.request.install_opener(opener)
                r = urllib.request.urlopen(source)
                if r.getcode() == 404:
                    raise Exception("HTTP 404 on " + source)
                open(local_file, "wb").write(r.read())

            # now we have the file locally
            # computing the sha256
            sha256 = hashlib.sha256(open(local_file, "rb").read())

            if sha256.hexdigest() != v["sha256"]:
                raise Exception("Under attack! SHA256 does not match " + source)

            print(source + ": verified")
