from aiogram import Bot,Dispatcher,types,executor
import openai
import api

bot = Bot(api.BOT)
db = Dispatcher(bot)

openai.api_key = Bot(api.openai)

@db.message_handler(commands=['start'])
async def start(message: types.Message):
    await message.answer("Hello "+message.from_user.full_name+",Ask me anything")



@db.message_handler()
async def queries(message: types.Message):
    response = openai.Completion.create(
    model="text-davinci-003",
    prompt= message.text,
    temperature=0.5,
    max_tokens=1024,
    top_p=1,
    frequency_penalty=0.0,
    presence_penalty=0.0
    #stop=["\n"]
    )
    await message.answer(response.choices[0].text)

if __name__ == '__main__':
    executor.start_polling(db, skip_updates=True)
    