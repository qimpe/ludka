from aiogram.fsm.context import FSMContext
from aiogram.types import Message
from aiogram.fsm.state import State,StatesGroup


class UserRegister(StatesGroup):
    tg_id=State()
    address=State()