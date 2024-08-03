from models import Transaction
from tortoise import Tortoise
import asyncio
def check_transaction(hash):
    transaction=Transaction.get(hash)
    print(transaction)
    if transaction:
        return True
    return False

async def add_transaction(hash,comment,payer):
    transaction=await Transaction.create(hash=hash,comment=comment,payer=payer)
    await transaction.save()
    
    
if __name__=="__main__":
    asyncio.run(add_transaction("123","123","123"))