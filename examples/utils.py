# https://github.com/hyperledger/indy-sdk/blob/main/docs/how-tos/write-did-and-query-verkey/python/utils.py

from pathlib import Path
from tempfile import gettempdir

PROTOCOL_VERSION = 2


def get_pool_genesis_txn_path(pool_name):
    path_temp = Path(gettempdir()).joinpath("indy")
    path = path_temp.joinpath("{}.txn".format(pool_name))
    save_pool_genesis_txn_file(path)
    return path


def pool_genesis_txn_data():
    return """{"reqSignature":{},"txn":{"data":{"data":{"alias":"tbtk1","blskey":"3Fd47gxCTnumCK6tWw67QNvuuTdV5Log98W5zqph47CtPuMGhxquQeQdDtExBTKrf2h34Fzq6n9wDq9sMVosCF57sNAAYXUJ9SPCnLfZi9HGzarzufXzgLdemJd3EfR9L2hYJMCMNedTkGXBEkQoAL2YcgzkgMiTdZMvH6oDgDuPqAn","blskey_pop":"R7ZqdRqyhSMkEzP7BKXJZrooMRTzNXBAQ72sXT2CTe55unygvVw1J1kRGQZT6LcgSUBXfWCxirTWcSzaeAQLmX2rJTNd3B5P9nPjzmLjyo3qxKNnaVMvKLsMpzsJaLniMjHdXeggUbAWPZUSs1cRxVvoviWSmV7cX5EGXLVH913EXH","client_ip":"5.252.204.141","client_port":"9702","node_ip":"10.29.29.2","node_port":"9701","services":["VALIDATOR"]},"dest":"4TzzhKsPCBwTYTnATF9JSRRMcvf5TnWnn5DEncDjeQiN"},"metadata":{"from":"7MnUxhDh56UmUmZGdurvzk"},"type":"0"},"txnMetadata":{"seqNo":1,"txnId":"266ee63fbf82e0cda7ab6a04caf179265238927625d5a9f029a4eb8dcef888ef"},"ver":"1"}
{"reqSignature":{},"txn":{"data":{"data":{"alias":"tbtk2","blskey":"HxrGvTkTzrLvCotTU2JZfJoCYgsTTpLAB8bkbiqQtPaop6KvZ1qwDwpepBbwjA5ayGiGr3hfesc64knk4FWKqjGYjZNYYTUqtdusT7pJ5j4mPpVaWxJNTnNUm6purJRQjwsnrJMGaVp8e5nSw9rT2dPNdixGXPijP5eNwfrBmCLuWP","blskey_pop":"RKMUNpLptTzHVSEtxhvY8NgsTga2xMntpoVNZbjScLqQjyBVAMk2TxAEdTWJcSS17ADCU2tRtNQCeVh4Z2H54ueicHLRv48tSwJhajMqNSzB5GSQZVJoM73yWBW9sTGTH8yH9jux8upBaGvBk7XWmXqUWEUsXdBL6Ei8JSxe8jFyUK","client_ip":"5.252.204.141","client_port":"9704","node_ip":"10.29.29.3","node_port":"9703","services":["VALIDATOR"]},"dest":"FvM37TPMy4kpkvDcbXb5rVxizEnVFTNre1veeWNdx2EG"},"metadata":{"from":"UNh4syxSLQWWpJxM8JM4og"},"type":"0"},"txnMetadata":{"seqNo":2,"txnId":"b70ec813929f49260a40783ba85f15906a4e2dd75a487c8c5fde531b6e2be7c1"},"ver":"1"}
{"reqSignature":{},"txn":{"data":{"data":{"alias":"tbtk3","blskey":"2nTYJPkgkAXeZpWLBGxKStcfPGx9n7E6kYiddjudWohc42H2Lzd3BtFpsSRur9YnEVkFPbXLqkArj3g3YuNUv1fxEE2LDU9zRwBL34hT4FZomtgKrACgL72MY943jb7sh5ALpK3PEn3sTDTBvM5zeoKtyw2FvnkNknZe8kMmD5dDVjo","blskey_pop":"RYWHWW3nVuD2sSqQgD7TYfzQCP1nYkbnMFkZeohApesTDYYPN7kNgjzGDzvsjmT1nejd5PbyhEmFJgmkPTCHVtweAeUXZhjqqhWwpFP24iYBC9yGDxyxy9tcHocALpAQknuaSoM38EBpX2J3ZbppM4EKB8eeg7ScD5SVGXWQPN1sMZ","client_ip":"5.252.204.141","client_port":"9706","node_ip":"10.29.29.4","node_port":"9705","services":["VALIDATOR"]},"dest":"F4PVpB9yhddQqPKdqJJqmA9go75DWMJPArXVyiZ5DVFA"},"metadata":{"from":"So2p6V1T1NU8pQEAtC2z1x"},"type":"0"},"txnMetadata":{"seqNo":3,"txnId":"b3921432e4073d619a57a4b12588cefe5102c6575469264444bb0bc7098de175"},"ver":"1"}
{"reqSignature":{},"txn":{"data":{"data":{"alias":"tbtk4","blskey":"4juqxWyMuYbbYTE5vzxbN747MvxSjfY94SoUZ2MJsS8XxZDp6G2mkYk6tHX3guRF6xq8CYiM3adETrq41NJSWC4pRvHLPsaJsBR2w3tYnnk79kQ8JDZKc272N5G1paNLwVcrEGwRsc2WhERgVbqz1UVXQn1BLrowSX67dRkcMLRwotT","blskey_pop":"Qw7DVjrVe5ujQdLrJXSE3Xu95aroeJiHJXnrVXaC3R4QzzVTdh6NRGP2So3hAmt5hBUCa2taf4JnSGNr6d2sgsCJ5jngdBH7mKTHDFiHyEemvfiGxyXF82ybhQAsCRbr6rknZ1dSn4EZUmfG5iRX1rK5H59wMLwjELGEGnLXdP6Ym5","client_ip":"5.252.204.141","client_port":"9708","node_ip":"10.29.29.5","node_port":"9707","services":["VALIDATOR"]},"dest":"5zsoBCXGjxhKhNY5c2HAQR8A6duKqezGJwrPCojs67op"},"metadata":{"from":"AArF7p2Bckz6qwzoEHeRSP"},"type":"0"},"txnMetadata":{"seqNo":4,"txnId":"c4649f64b28ab9935f77368e3805b841af30e1363c4971836036bbd7aa7f2fee"},"ver":"1"}"""


def save_pool_genesis_txn_file(path):
    data = pool_genesis_txn_data()
    path.parent.mkdir(parents=True, exist_ok=True)
    with open(str(path), "w+") as f:
        f.writelines(data)
