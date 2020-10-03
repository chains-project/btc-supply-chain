# btc-supply-chain

`btc-supply-chain` is a database of the Bitcoin software supply chain. The goal of this database is to help the world use Bitcoin safely. It contains key information trustable bitcoin software components:

* SHA256 of libraries and applications (incl. wallets)
* GPG signatures and developer keys

**Warning**: this is work-in-progress.

Authors: Martin Monperrus et al.

## Intro

What is the Bitcoin software supply chain? It is the set of all computer programs used to run Bitcoin, in particular the node and wallet software.

**TL;DR; Never execute a wallet program that you don't verify first**


## Professional support

If you need professional support on the Bitcoin software supply chain, please contact Martin Monperrus by email. Professional support means auditing a software supply chain, checking the validity and reputation of a given developer / organization / GPG key, etc.

## Bitcoin Full Nodes

If you run a full node, you absolutely want to verify the integrity of the code you're running, see folder `full-nodes`.

For instance, the SHA256 of [Bitcoin Core v0.17.2](https://bitcoin.org/bin/bitcoin-core-0.17.2/bitcoin-0.17.2-aarch64-linux-gnu.tar.gz) is 5a6b35d1a348a402f2d2d6ab5aed653a1a1f13bc63aaaf51605e3501b0733b7a.

## Wallets

The wallet supply chain information is in folder `wallets`. To verify that you use a safe wallet program:

ALWAYS:

1. Compute the SHA256 sum of the wallet binary or installation file
2. Check that is known by Google, eg <https://encrypted.google.com?q=6b98b367acdee51961118f57d0ba40e57f369d031a43c673ad76cda97cf61db1>
  * If there is 0 results on Google **STOP AND DELETE THE FILE**, it can be a malware
3. If Google knows it, check the reliability of the websites where this SHA256 appears
3. If Google knows it, check if this appears in folder `wallets` (see section "Meta-trust" below)

DONT:

* Do NOT download wallet programs from arbitrary websites
* Paranoids never install a wallet app through the Google Play Store / Apple App Store because they cannot verify the APK signatures beforehand, they have to entirely trust Google / Apple.

To check the cryptographic GPG signature of the wallet binary, and verify that it comes from a trusted source.

1. Download the public GPG key of the developer from at least 2 reliable sources
1. Verify that it is the same key
1. Download the GPG signature file that comes with the wallet program
1. Verify that the downloaded signature of the downloaded file has been signed with the downloaded key


## Software dependencies

If you are developer of Bitcoin-related software, you want to make sure that your dependencies are not compromised. This is the data you'll find in folder `dependencies`, where there are.

* Checksums and signatures of source packages
* Checksums and signatures of binary packages
* SSL keys of repositories and package managers

## Meta-trust

Wait! Maybe this website has been compromised? That's entirely correct! You should make your own research about this website as well.

Mitigations:

* Github is an industry-grade platform with strong authentication and authorization checks.
* All commits are signed with Martin Monperrus' GPG key.

## Continuous Integration

At each commit, we verify that the data contained here is consistent, see script `check-btc-supply-chain.py`


## License

The content of this repository is licensed under the MIT license.



