
# Import key classes and functions to make them available directly from the package
from .client import SinopsisAI
from .utils import log_user_message, log_assistant_response, update_conversation_in_db

__all__ = ['SinopsisAI', 'log_user_message', 'log_assistant_response', 'update_conversation_in_db']