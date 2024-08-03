from aiogram.filters.command import CommandStart,Command
from aiogram import Router
from aiogram.types import Message
from database.models import User

router=Router()

@router.message(CommandStart())
async def start_cmd(message: Message):
    try:
        user,created= await User.get_or_create(tg_id=message.from_user.id)
        if user:
            await user.save()
    except Exception as e:
        print(e)
        await message.answer("U already Registered")
    await message.answer(text="Hello")
    

@router.message(Command("stats"))
async def user_stats(message: Message):
    user=await User.get(pk=message.from_user.id)
    MESSAGE=f"Id: {user.tg_id}\nAddress:{user.address}"
    await message.answer(MESSAGE)
