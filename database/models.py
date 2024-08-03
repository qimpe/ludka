from tortoise import fields 
from tortoise.models import Model

class User(Model):
    tg_id=fields.IntField(pk=True)
    address=fields.CharField(max_length=256,default=None,null=True)
    
    
    class Meta:
        table="users"
    
class Transaction(Model):
    payer=fields.CharField(max_length=48)
    hash=fields.CharField(max_length=50,unique=True)
    comment=fields.CharField(max_length=50)
    
    class Meta:
        table="transactions"


