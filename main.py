import asyncio
import logging
import sys

from aiogram import Bot, Dispatcher, F
from aiogram.client.default import DefaultBotProperties
from aiogram.enums import ParseMode
from aiogram.filters import CommandStart
from aiogram.types import Message
from aiogram.utils import keyboard
from cryptography.fernet import Fernet

import json
import Caesar
import DES
import fernet

TOKEN = "7063518702:AAFXxp_8cOZwwAXeuqTEOTlUp0S4ZMPVYOw"
dp = Dispatcher()

builder = keyboard.ReplyKeyboardBuilder()

builder.button(text='DES encrypt')
builder.button(text='DES decrypt')
builder.button(text='Caesar encrypt')
builder.button(text='Caesar decrypt')
builder.button(text='Fernet encrypt')
builder.button(text='Fernet decrypt')

keys = json.loads(open("/home/bmwproexpert/Tg/EncryptTgbot/config.json").read())

des_key = keys["des_key"].encode("utf-8")
caesar_key = int(keys["caesar_key"])
fernet_key = keys["fernet_key"].encode("utf-8")
word = None


@dp.message(CommandStart())
async def command_start_handler(message: Message) -> None:
    await message.answer("First, write the text, and then select the appropriate button for encryption or decryption.")
    await message.answer(text="buttons", reply_markup=builder.as_markup())


@dp.message(F.text.lower() == 'des encrypt')
async def des_encrypt(message: Message) -> None:
    try:
        global word
        if (word != None):
            global des_key
            await message.answer(DES.encrypt(des_key, word))
        else:
            await message.answer("At first, write the text")
    except:
        await message.answer("Something wrong")


@dp.message(F.text.lower() == 'des decrypt')
async def des_encrypt(message: Message) -> None:
    try:
        global word
        if word != None:
            global des_key
            await message.answer(DES.decrypt(des_key, word))
        else:
            await message.answer("At first, write the text")
    except:
        await message.answer("Something wrong")


@dp.message(F.text.lower() == 'caesar encrypt')
async def caesar_encrypt(message: Message) -> None:
    try:
        global word
        if (word != None):
            global caesar_key
            await message.answer(Caesar.encrypt(word, caesar_key))
        else:
            await message.answer("At first, write the text")
    except:
        await message.answer("Something wrong")


@dp.message(F.text.lower() == 'caesar decrypt')
async def caesar_encrypt(message: Message) -> None:
    try:
        global word
        global caesar_key
        if word != None:
            await message.answer(Caesar.decrypt(word, caesar_key))
        else:
            await message.answer("At first, write the text")
    except:
        await message.answer("Something wrong")


@dp.message(F.text.lower() == 'fernet encrypt')
async def fernet_encrypt(message: Message) -> None:
    try:
        global word
        if (word != None):
            global fernet_key
            await message.answer(fernet.encrypt(word, fernet_key))
        else:
            await message.answer("At first, write the text")
    except:
        await message.answer("Something wrong")


@dp.message(F.text.lower() == 'fernet decrypt')
async def fernet_encrypt(message: Message) -> None:
    try:
        global word
        global fernet_key
        if word != None:
            await message.answer(fernet.decrypt(word, fernet_key))
        else:
            await message.answer("At first, write the text")
    except:
        await message.answer("Something wrong")


@dp.message()
async def text_handler(message: Message) -> None:
    try:
        global word
        word = message.text
    except:
        await message.answer("Something wrong")


async def main() -> None:
    bot = Bot(token=TOKEN, default=DefaultBotProperties(parse_mode=ParseMode.HTML))
    await dp.start_polling(bot)


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO, stream=sys.stdout)
    asyncio.run(main())
