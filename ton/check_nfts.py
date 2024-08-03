import requests
from .get_wallet_address import bounceable_b64url

COLLECTION_ADDRESS = "EQDHHPuYhYjOhBNt-OpUxxdrLgj2yjT7b_VpodfioyNi7l4M"


def get_wallet_nfts(right_address):
    msg = ""
    BASE_URL = f"https://tonapi.io/v2/accounts/{right_address}/nfts?collection={COLLECTION_ADDRESS}&limit=1000&offset=0&indirect_ownership=true"
    response = requests.get(BASE_URL).json()
    items = response["nft_items"]
    for item in items:
        item = item["metadata"]["name"]
        msg += f"{item}\n"
    return msg


if __name__ == "__main__":
    address = bounceable_b64url("UQAkWuybVMoZI3jkMnkNL9rBNwjM7nVKaH876uWkUX-ir5qY")
    wallet_nfts = get_wallet_nfts(address)
