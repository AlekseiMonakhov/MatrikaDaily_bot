import random
from aiogram import executor, Bot, Dispatcher, types
from apscheduler.schedulers.asyncio import AsyncIOScheduler

token = ''
bot = Bot(token=token, parse_mode=types.ParseMode.HTML)

dp = Dispatcher(bot)
scheduler = AsyncIOScheduler()
players_list = []
index_list = ['1', '10', '10r', '11', '11r', '12', '12r', '13', '13r', '14', '14r', '15', '16', '17', '18', '19', '19r',
              '2', '20', '20r', '21', '21r', '22', '22r', '23', '23r', '24', '24r', '25', '25r', '26', '26r', '27',
              '27r', '28', '28r', '29', '29r', '3', '30', '30r', '31', '31r', '32', '32r', '33', '33r', '34', '34r',
              '35', '35r' , '36', '36r', '37', '37r', '38', '38r', '39', '39r', '4', '40', '40r', '41', '41r', '42',
              '42r', '43', '43r', '44', '44r', '45', '45r', '46', '46r', '47', '47r', '48', '48r', '49', '49r', '5',
              '50', '50r', '6', '7', '7r', '8', '8r', '9', '9r']


@dp.message_handler(commands=['card'])
async def lets_play(message: types.Message):
    global players_list
    user_id = message.from_user.id
    if user_id in players_list:
        await message.answer(f'{message.from_user.first_name}, сегодня Вы уже получали Карту дня!')
    else:
        read_mantra = 'oṃ a kṣa hrīṃ namaḥ'
        random_choice = (random.choice(index_list))
        karta = open(f'Matrika/{random_choice}.jpg', 'rb')
        text = open(f'Poems/{random_choice}.txt', 'r')
        await bot.send_photo(message.chat.id, karta, caption=text.read(), reply_to_message_id=message.message_id)
        karta.close()
        text.close()
        players_list.append(user_id)


def clear_list():
    global players_list
    players_list.clear()


def schedule_jobs():
    scheduler.add_job(clear_list, 'cron', hour=23, minute=59)


if __name__ == '__main__':
    schedule_jobs()
    scheduler.start()
    executor.start_polling(dp, skip_updates=True)
