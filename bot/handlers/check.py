from aiogram import Router, types, F
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import StatesGroup, State
from bot.keyboards.menu import main_menu
import httpx

check_router = Router()


class CheckTokenPrice(StatesGroup):
    waiting_for_coin = State()


coin_aliases = {
    "btc": "bitcoin",
    "eth": "ethereum",
    "usdt": "tether",
    "bnb": "binancecoin",
    "xrp": "ripple",
    "sol": "solana",
    "ada": "cardano",
    "doge": "dogecoin",
    "usdc": "usd-coin",
    "trx": "tron",
    "steth": "lido-staked-ether",
    "matic": "matic-network",
    "dot": "polkadot",
    "avalanche": "avalanche-2",
    "avax": "avalanche-2",
    "link": "chainlink",
    "shib": "shiba-inu",
    "matic": "polygon",
    "lunc": "terra-luna",
    "busd": "binance-usd",
    "ltc": "litecoin"
}


@check_router.message(F.text == '💰 Check Price')
async def check_command(message: types.Message, state: FSMContext):
    await message.answer("🔍 What crypto are you curious about?\n\nJust type the coin symbol (e.g. `BTC`, `ETH`).",
                         parse_mode="Markdown")
    await state.set_state(CheckTokenPrice.waiting_for_coin)


@check_router.message(CheckTokenPrice.waiting_for_coin)
async def coin_input_handler(message: types.Message, state: FSMContext):
    coin_input = message.text.strip().lower()
    coin_id = coin_aliases.get(coin_input, coin_input)
    url = f"https://api.coingecko.com/api/v3/simple/price?ids={coin_id}&vs_currencies=usd"
    async with httpx.AsyncClient() as client:
        response = await client.get(url)
        data = response.json()

    if not data or coin_id not in data:
        await message.answer("⚠️ Oops, couldn't find that coin.\nPlease double-check the name and try again.")
        return

    price = data[coin_id]['usd']

    await message.answer(f"💰 *{coin_input.upper()}* is currently worth *${price}* USD", parse_mode="Markdown", reply_markup=main_menu)
    await state.clear()
