import requests
import json
import asyncio
from get_wallet_address import bounceable_b64url
from database.func import add_transaction


def get_wallet_transactions(address):
    right_address = bounceable_b64url(address)
    BASE_URL = f"https://toncenter.com/api/v2/getTransactions?address={right_address}&limit=20&to_lt=0&archival=true"
    r = requests.get(BASE_URL)
    response = json.loads(r.text)
    return response["result"]


async def find_transaction(user_wallet, comment):
    transactions = get_wallet_transactions(
        "UQAkWuybVMoZI3jkMnkNL9rBNwjM7nVKaH876uWkUX-ir5qY"
    )
    for transaction in transactions:
        msg = transaction["in_msg"]
        if msg["source"] == user_wallet and msg["message"] == comment:
            await add_transaction("123", "123", "123")


if __name__ == "__main__":
    asyncio.run(find_transaction("1", "2"))
