from aiogram import Dispatcher

from .start import start_router
from .help import help_router
from .cancel_alert import clear_router
from .set_alert import set_router
from .view_alerts import view_router
from .trends import trends_router
from .check import check_router
from .rates import rates_router


def register_all_handlers(dp: Dispatcher):
    dp.include_router(help_router)
    dp.include_router(clear_router)
    dp.include_router(start_router)
    dp.include_router(set_router)
    dp.include_router(view_router)
    dp.include_router(trends_router)
    dp.include_router(check_router)
    dp.include_router(rates_router)