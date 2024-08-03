from aiogram.types import Message
from aiogram import Router,F
from ton.check_nfts import bounceable_b64url,get_wallet_nfts
from database.models import User
from aiogram.fsm.context import FSMContext
from states.change_adress import ChangeAddress
router=Router()


@router.message(F.text.lower()=='my nfts')
async def get_my_nfts(message: Message):
    user=await User.get(tg_id=message.from_user.id)
    right_address=bounceable_b64url(user.address)
    nfts=get_wallet_nfts(right_address)
    await message.answer(nfts)
    
@router.message(F.text.lower()=="edit address")
async def change_address(message: Message, state: FSMContext):
    await message.answer("Input ur address")
    address=await state.set_state(ChangeAddress.address)
    
@router.message(ChangeAddress.address,F.text)
async def save_address(message:Message, state: FSMContext):
    await state.update_data(address=message.text)
    try:
        user=await User.filter(tg_id=message.from_user.id).first()
        if user:
            user.address=message.text
            await user.save(update_fields=['address']) 
            await message.answer(f"Address saved: {message.text}")
            await state.clear()
        else:
            await message.answer("no user")
    except Exception as e:
        print(e)
        await message.answer("Error")