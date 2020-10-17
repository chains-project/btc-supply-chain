# btc-supply-chain: the Bitcoin software supply chain database (WIP)

`btc-supply-chain` is a database documenting the Bitcoin software supply chain. The goal of this database is to help the world use Bitcoin safely. It contains the key information required to trust bitcoin software components:

* SHA256 of wallets, nodes and bitcoin libraries
* GPG developer keys and signatures

This information is valuable:

- for Bitcoin users, because they have a external source of information to verify a hash. In particular, where the hash only exists in a single place so far (the wallet/node website), the btc-supply-chain hash provides a second anchor on the Internet
- for Bitcoin developers of wallet/nodes, in order to submit their hash to a third party database
- for Bitcoin developers of wallet/nodes, in order to verify that their dependencies are known

What is the Bitcoin software supply chain? It is the set of all computer programs used to run Bitcoin, in particular the node and wallet software.

Contributions are welcome as pull-requests.

## Professional support

If you need professional support on the Bitcoin software supply chain, please contact Martin Monperrus by email. 

* auditing a bitcoin software supply chain
* set up a verifiable reproducible build pipeline
* reproduce a particular build
* checking the validity of a developer's / organization's GPG key.

## Bitcoin Full Nodes

If you run a full node, you absolutely want to verify the integrity of the code you're running.
For instance, the SHA256 of [Bitcoin Core v0.17.2](https://bitcoin.org/bin/bitcoin-core-0.17.2/bitcoin-0.17.2-aarch64-linux-gnu.tar.gz) is 5a6b35d1a348a402f2d2d6ab5aed653a1a1f13bc63aaaf51605e3501b0733b7a.

See folder `db/full-nodes`

## Wallets

The wallet supply chain information is in folder `wallets`. 

To verify that you use a safe wallet program:

1. Compute the SHA256 sum of the wallet binary or installation file you've just downloaded
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

btc-supply-chain contributes to this by storing important data in folder `db/dependencies` (work in progress):

* Checksums and signatures of source packages
* Checksums and signatures of binary packages
* Public keys of repositories and package managers

## Meta-trust

Wait! Maybe this website has been compromised? That's entirely correct! You should make your own research about this website as well. Mitigation:

* We use double-factor authentication
* All commits are signed with Martin Monperrus' GPG key.

## Continuous Integration

At each commit, we verify that the data contained here is consistent, see script `check-btc-supply-chain.py`.

TODO:

* check GPG signatures in CI

## License

The content of this repository is licensed under the MIT license.



