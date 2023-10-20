# https://github.com/hyperledger/indy-sdk/blob/main/docs/how-tos/write-did-and-query-verkey/python/write_did_and_query_verkey.py

import asyncio
import json

from indy import pool, ledger
from indy.error import IndyError, ErrorCode

from utils import get_pool_genesis_txn_path, PROTOCOL_VERSION

pool_name = "ssi-turkiye-testnet"
genesis_file_path = get_pool_genesis_txn_path(pool_name)

def print_log(value_color="", value_noncolor=""):
    """set the colors for text."""
    HEADER = "\033[92m"
    ENDC = "\033[0m"
    print(HEADER + value_color + ENDC + str(value_noncolor))


async def query_ledger():
    try:
        await pool.set_protocol_version(PROTOCOL_VERSION)

        print_log(
            "\n1. Creates a new local pool ledger configuration that is used "
            "later when connecting to ledger.\n"
        )
        pool_config = json.dumps({"genesis_txn": str(genesis_file_path)})
        try:
            await pool.create_pool_ledger_config(
                config_name=pool_name, config=pool_config
            )
        except IndyError as ex:
            if ex.error_code == ErrorCode.PoolLedgerConfigAlreadyExistsError:
                pass

        print_log("\n2. Open pool ledger and get handle from libindy\n")
        pool_handle = await pool.open_pool_ledger(config_name=pool_name, config=None)

        request = await ledger.build_get_txn_request(None, None, 1)
        print(request)
        response = await ledger.submit_request(pool_handle, request)
        parsed = json.loads(response)
        print_log("response: {}".format(response))

        print_log("\n13. Closing wallet and pool\n")
        await pool.close_pool_ledger(pool_handle)

    except IndyError as e:
        print("Error occurred: %s" % e)


def main():
    loop = asyncio.get_event_loop()
    loop.run_until_complete(query_ledger())
    loop.close()


if __name__ == "__main__":
    main()
