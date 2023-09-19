# Create your states in this folder.
from telebot.asyncio_handler_backends import State, StatesGroup


class ProjectStates(StatesGroup):
    """
    Group of states for registering
    """
    state1 = State()
    state1.name = 'sate_1_name'



