# btc-supply-chain: the Bitcoin software supply chain database

`btc-supply-chain` is a database about the Bitcoin software supply chain. The goal of this database is to help the world use Bitcoin safely. It contains the key information required to trust bitcoin software components, starting with SHA256 of code for wallets, nodes and bitcoin libraries. This database is valuable:

- for Bitcoin users, because they have an external source of information to verify the authenticity of the software they use (through verifying the SHA256 hash)
- for Bitcoin developers of wallet/nodes, in order to submit their hash to a third party database

Contributions are welcome as pull-requests.

If you need professional support about the Bitcoin software supply chain, please contact [Martin Monperrus](https://www.monperrus.net/martin/contact) by email. 

* auditing a bitcoin software supply chain
* set up a verifiable reproducible build pipeline
* reproduce a particular build
* checking the validity of a file / developer key / organization.
## Related work

* <https://bitcoinissafe.com/> is a related project, with a focus on antivirus software adoption for Bitcoin tools.
* <https://BinaryWatch.org> Checksum Checker, scheduled checks on Bitcoin project binaries,  by Coinkite.

We automatically download the binaries every hour
<https://bitcoinissafe.com/> is a great related project, with a focus on antivirus software adoption of Bitcoin tools.


## Web page

<https://github.com/monperrus/btc-supply-chain/wiki> contains the SHA256 of the latest version. It is meant to be indexed by the major search engines, starting with Google.

## Bitcoin Full Nodes

If you run a full node, you absolutely want to verify the integrity of the code you're running.
For instance, the SHA256 of [Bitcoin Core v0.17.2](https://bitcoin.org/bin/bitcoin-core-0.17.2/bitcoin-0.17.2-aarch64-linux-gnu.tar.gz) is 5a6b35d1a348a402f2d2d6ab5aed653a1a1f13bc63aaaf51605e3501b0733b7a.

See folder `db/full-nodes`

## Wallets

The wallet supply chain information is in folder `wallets`. 

To verify that you use a safe wallet program:

1. Compute the SHA256 sum of the wallet binary or installation file you've just downloaded
    * Do it in the browser at <https://sprin.github.io/TrustyHash/>
    * For advanced users, see https://help.ubuntu.com/community/HowToSHA256SUM
2. Check that is known by Google, eg <https://encrypted.google.com?q=6b98b367acdee51961118f57d0ba40e57f369d031a43c673ad76cda97cf61db1>. If there is 0 results on Google **STOP AND DELETE THE FILE**, it can be a malware trying to steal your bitcoin.
3. If Google knows it, check the reliability of the websites where this SHA256 appears
3. If Google knows it, check whether the SHA256 sum appears in folder `db/wallets` (see section "Meta-trust" below)

DONT:

* Do NOT download wallet programs from arbitrary websites
* Do NOT install a wallet app through the Google Play Store / Apple App Store because you cannot verify the APK signatures beforehand, you have to entirely trust Google / Apple.

Advanced users want to [verify the cryptographic GPG signature](https://www.wikihow.com/Verify-a-GPG-Signature) of the wallet binary, and verify that it comes from a trusted source.


## Software Dependencies

Now we're talking. Verifying the software supply chain at the developer level is much harder than verifying a single wallet or node software. One needs to verify the provenance of all libraries and tools (eg compiler) used to create the final executable (see the excellent talk by [Carl Dong](https://github.com/dongcarl) at <https://youtu.be/I2iShmUTEl8>). 

There is excellent tool support for verifying a supply chain:

* [Guix](https://guix.gnu.org/):  Guix is a package manager with secure and deterministic packaging. [See the Bitcoin-core pipeline](https://github.com/bitcoin/bitcoin/blob/master/contrib/guix/README.md)
* [Gitian](https://gitian.org/): Gitian enables one to set up secure and deterministic build process. See the [Gitian process of bitcoin-core](https://github.com/bitcoin-core/docs/blob/master/gitian-building.md)

## Checking btc-supply-chain

To verify that the data contained in this repo is consistent, see script `check-btc-supply-chain.py`.

## Meta-trust

Wait! Maybe this website has been compromised? That's entirely correct! You should make your own research about this website as well. Mitigation:

* We use double-factor authentication
* All commits are signed with Martin Monperrus' GPG key.
* Public keys of repositories and package managers



## License

The content of this repository is licensed under the MIT license.



