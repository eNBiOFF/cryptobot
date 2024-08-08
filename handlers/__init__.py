from aiogram import Dispatcher
from .start import register_start_handlers
from .help import register_help_handlers
from .referral_link import register_referral_link
from .balance import register_balance_handlers
from .subscrived import register_subscribed_handlers

def register_handlers(dp: Dispatcher):
    register_start_handlers(dp)
    register_help_handlers(dp)
    register_referral_link(dp)
    register_balance_handlers(dp)
    register_subscribed_handlers(dp)