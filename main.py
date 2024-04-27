import asyncio
import binascii
import logging
import sys

import cryptography.fernet
from aiogram import Bot, Dispatcher, F
from aiogram.client.default import DefaultBotProperties
from aiogram.enums import ParseMode
from aiogram.filters import CommandStart
from aiogram.types import Message
from aiogram.utils import keyboard

import json
import caesar
import des
import fernet


def init(config_path: str) -> (str, str, str, str):
    try:
        config = json.load(open(config_path))
        token = config["token"]
        des_key = config["des_key"].encode("utf-8")
        caesar_key = int(config["caesar_key"])
        fernet_key = config["fernet_key"].encode("utf-8")
        return token, des_key, caesar_key, fernet_key

    except FileNotFoundError as e:
        print(f"bad filepath {config_path}")
        sys.exit(1)

    except json.decoder.JSONDecodeError as e:
        print(f"json parsing failed {e}")
        sys.exit(2)

    except Exception as e:
        print(f"unexpected error while parsing config {e}")
        sys.exit(-1)


TOKEN, DES_KEY, CAESAR_KEY, FERNET_KEY = init("config.json")
dp = Dispatcher()
MESSAGE = None

builder = keyboard.ReplyKeyboardBuilder()
builder.button(text='DES encrypt')
builder.button(text='DES decrypt')
builder.button(text='Caesar encrypt')
builder.button(text='Caesar decrypt')
builder.button(text='Fernet encrypt')
builder.button(text='Fernet decrypt')


@dp.message(CommandStart())
async def command_start_handler(message: Message) -> None:
    await message.answer("First, write the text, and then select the appropriate button for encryption or decryption.")
    await message.answer(text="buttons", reply_markup=builder.as_markup())


@dp.message(F.text.lower() == 'des encrypt')
async def des_encrypt(message: Message) -> None:
    try:
        global MESSAGE
        if MESSAGE is not None:
            global DES_KEY
            await message.answer(des.encrypt(DES_KEY, MESSAGE))
        else:
            await message.answer("At first, write the text")
    except Exception as e:
        await message.answer(f"Something wrong ({e})")


@dp.message(F.text.lower() == 'des decrypt')
async def des_encrypt(message: Message) -> None:
    try:
        global MESSAGE
        if MESSAGE is not None:
            global DES_KEY
            await message.answer(des.decrypt(DES_KEY, MESSAGE))
        else:
            await message.answer("At first, write the text")
    except binascii.Error as e:
        await message.answer("Invalid input")
    except Exception as e:
        await message.answer(f"Something wrong {(e)}")


@dp.message(F.text.lower() == 'caesar encrypt')
async def caesar_encrypt(message: Message) -> None:
    try:
        global MESSAGE
        if (MESSAGE is not None):
            global CAESAR_KEY
            await message.answer(caesar.encrypt(MESSAGE, CAESAR_KEY))
        else:
            await message.answer("At first, write the text")
    except AssertionError as e:
        await message.answer("Invalid input")
    except Exception as e:
        await message.answer(f"Something wrong ({e.with_traceback(None)})")


@dp.message(F.text.lower() == 'caesar decrypt')
async def caesar_decrypt(message: Message) -> None:
    try:
        global MESSAGE
        global CAESAR_KEY
        if MESSAGE is not None:
            await message.answer(caesar.decrypt(MESSAGE, CAESAR_KEY))
        else:
            await message.answer("At first, write the text")
    except AssertionError as e:
        await message.answer("Invalid input")
    except Exception as e:
        await message.answer(f"Something wrong ({e.with_traceback(None)})")


@dp.message(F.text.lower() == 'fernet encrypt')
async def fernet_encrypt(message: Message) -> None:
    try:
        global MESSAGE
        if MESSAGE is not None:
            global FERNET_KEY
            await message.answer(fernet.encrypt(MESSAGE, FERNET_KEY))
        else:
            await message.answer("At first, write the text")
    except Exception as e:
        await message.answer(f"Something wrong ({e.with_traceback(None)})")


@dp.message(F.text.lower() == 'fernet decrypt')
async def fernet_encrypt(message: Message) -> None:
    try:
        global MESSAGE
        global FERNET_KEY
        if MESSAGE is not None:
            await message.answer(fernet.decrypt(MESSAGE, FERNET_KEY))
        else:
            await message.answer("At first, write the text")
    except cryptography.fernet.InvalidToken as e:
        await message.answer("Invalid input")
    except Exception as e:
        await message.answer(f"Something wrong ({e.with_traceback(None)})")


@dp.message()
async def text_handler(message: Message) -> None:
    try:
        global MESSAGE
        MESSAGE = message.text
        await message.answer(text='Choose the next action', reply_markup=builder.as_markup())
    except Exception as e:
        await message.answer(f"Something wrong ({e.with_traceback(None)})")


# we got params to Bot with init() and then start polling, using dispatcher,
# then on any message we have few handlers for processing them
async def main() -> None:
    bot = Bot(token=TOKEN, default=DefaultBotProperties(parse_mode=ParseMode.HTML))
    await dp.start_polling(bot)


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO, stream=sys.stdout)
    asyncio.run(main())
