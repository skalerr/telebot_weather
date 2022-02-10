
import math #Импорт математики

#Импорт погоды
import pyowm
from pyowm import OWM
from pyowm.utils import config
from pyowm.utils import timestamps

#settings
from pyowm.utils.config import get_default_config
config_dict = get_default_config()
config_dict['language'] = 'ru'  # your language here, eg. Portuguese
owm = OWM('3116d44c233a0f7b723c578a786e48af', config_dict) #token для owm
mgr = owm.weather_manager()




#!venv/bin/python
import logging
import config
from aiogram import Bot, Dispatcher, executor, types


#log level
logging.basicConfig(level=logging.INFO)

#bot init 
bot = Bot(token=config.TOKEN) #берем токен из конфига
dp = Dispatcher(bot)



# Хэндлер на команду /start
@dp.message_handler(commands="start")
async def cmd_start(message: types.Message):
    await message.reply("Привет напиши название города а я напишу погоду")


# Хэндлер на команду /test1
@dp.message_handler(commands="test1")
async def cmd_test1(message: types.Message):
    await message.reply("Test 1")


#echo
#@dp.message_handler()
#async def echo(message: types.Message):
	#await message.answer(message.text)

@dp.message_handler()
async def any_text_message2(message: types.Message):
	
	observation = mgr.weather_at_place(message.text)
	w = observation.weather
	temp = w.temperature('celsius') ["temp"]
	round (temp)
	await message.answer ("В городе " + message.text + " сейчас " + w.detailed_status + "\n" + "Температура: " + str(round(temp)) + " градуса по C " "\n\n")

	if temp < -10:
		await message.answer (" Одевайся теплее")

	elif temp > 5:
		await message.answer  ("Уже не так холодно")

	elif temp < -5:
		await message.answer  ("Немного прохладно")

	elif temp > 10:
		await message.answer  ("Становится теплее")
	else: 
		await message.answer  ("???")





#run long-polling
if __name__ == "__main__":
	executor.start_polling(dp, skip_updates=True)