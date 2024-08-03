import requests

def bounceable_b64url(address,raw=False):
    BASE_URL=f"https://tonapi.io/v2/address/{address}/parse"
    response=requests.get(BASE_URL).json()
    if raw:
        response=response["raw_form"]
    else:
        response=response["bounceable"]["b64url"]
    return response
        
        
if __name__=="__main__":
    bounceable_b64url("UQAkWuybVMoZI3jkMnkNL9rBNwjM7nVKaH876uWkUX-ir5qY",True)
        
    