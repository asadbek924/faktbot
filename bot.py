

# API_TOKEN = '5998858004:AAEc7FOuh2lB7YBvWRUH9GLLZaC3Ur3P-n4'

from aiogram import Bot, Dispatcher, executor, types
import logging
import requests
from pprint import pprint

logging.basicConfig(level=logging.INFO)

bot = Bot(token="6248065966:AAEmMK_fwS_v1VTZj61q1tmI_1e-TXzdK_A")
dp = Dispatcher(bot)

@dp.message_handler(commands=["start"])
async def start(message: types.Message):
    await message.answer(f"Assalomu alaykum, {message.chat.first_name}!")
    await message.answer("ob havo malumotini bilish: \n/weather <shahar_nomi>\n/help")

@dp.message_handler(commands=["weather"])
async def get_weather(message: types.MessageId):
    id=message.from_user.full_name
    # await bot.send_message(id(3487383039),f"salom {full_name}\n {message.text}") 
    try:
        city_name = message.text.split()[1]  
        weather_data = get_weather_data(city_name)
        await message.reply(weather_data)
    except IndexError:
        await message.reply("Xatolik yuz berdi. Shahar nomini kiritib yuboring.")

def get_weather_data(city):
    token = "7311aa89429bc363d47d76b65ae85633"
    
    
    res = requests.get(f"https://api.openweathermap.org/data/2.5/weather?&q={city}&appid={token}")
    

    weather_info = res.json()
    
    locality = weather_info['name']
    region = weather_info['sys']['country']
    weather_desc = weather_info['weather'][0]['description']
    temperature = weather_info['main']['temp'] - 273.15  
    humidity = weather_info['main']['humidity']
    wind_speed = weather_info['wind']['speed']
    
    return f"Mavjud ob-havo ma'lumotlari:\nShahar: {locality},\nViloyat / Mamlakat: {region},\nOb-havo holati: {weather_desc},\nHarorat: {temperature:.1f} °C,\nNamlik: {humidity}%,\nShamol tezligi: {wind_speed} km/s."

if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)