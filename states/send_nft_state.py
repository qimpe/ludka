from aiogram.fsm.context import FSMContext
from aiogram.types import Message
from aiogram.fsm.state import State,StatesGroup


class NftSend(StatesGroup):
    pass

class ChangeAddress(StatesGroup):
    address=State()