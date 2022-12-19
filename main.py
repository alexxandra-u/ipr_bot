from aiogram import Bot, types
from aiogram.dispatcher import Dispatcher
from aiogram.utils import executor
from random import randrange

bot = Bot(token='5923840344:AAFVGgNT9VHHgwkLafvDuiTS2zYg6NjXV6A')
dp = Dispatcher(bot)

list_of_activities = ["пойти погулять", "сделать домашку", "научиться готовить новое блюдо", "выйти на пробежку",
                      "посмотреть фильм", "встретиться с друзьями", "почитать книгу", "сходить в музей", "сходить в театр",
                      "спланировать путешествие на отпуск", "убраться дома", "поиграть в компьютерные игры", "поучить иностранный язык",
                      "поискать вакансии в интернете", "лечь поспать", "навестить кого-то из родственников"]

list_of_forecasts = ["твой день пройдет успешней, чем ты думаешь", "тебя ждет много трудностей",
                     "тебя ждет самый обычный день", "сегодня в твоей жизни произойдет что-то волшебное",
                     "этот день тебе захочется забыть навсегда", "в этот день твоя жизнь сильно поменяется",
                     "тебя ждут веселые приключения", "тебе сегодня придется изрядно понервничать"]

list_of_pictures = ["https://fikiwiki.com/uploads/posts/2022-02/1644712077_14-fikiwiki-com-p-prikolnie-kartinki-pro-korov-17.jpg",
                    "https://content.skyscnr.com/m/2a043bb8088ae62d/original/GettyImages-492881830.jpg?resize=1800px:1800px&quality=100",
                    "https://i.pinimg.com/originals/de/71/bb/de71bb8a57ff473cc58ebc6af58c4858.jpg",
                    "https://i.pinimg.com/736x/88/21/c6/8821c6ec60160d88971283826c7ab293.jpg",
                    "https://wonder-day.com/wp-content/uploads/2022/03/wonder-day-avatar-memes-cats-70.jpg",
                    "https://bugaga.ru/uploads/posts/2013-11/1385637779_zabavnyshi-24.jpg",
                    "https://i.ytimg.com/vi/ra62WZTdOBs/maxresdefault.jpg", "https://i.ebayimg.com/images/g/likAAOSwxH1T89ry/s-l400.jpg"]

list_of_facts = ["В среднем самые высокие люди – голландцы.", "Сенегальские женщины тратят на добывание воды в среднем 17,5 часов в неделю.",
                 "Самое распространённое имя в мире – Мухаммед.", "Ваше левое легкое меньше правого, из-за того, что оно “освобождает” место для сердца.",
                 "Звук, который вы слышите, когда вы хрустите суставами – звук взрывающихся пузырьков азота.",
                 "Если отправить птиц в космос – они вскоре умрут. Птицам нужна гравитация, чтобы глотать.", "Коалы спят 22 часа в сутки!",
                 "Бриллианты можно сделать из текилы."]



@dp.message_handler(commands=['start'])
async def process_start_command(message: types.Message):
    await message.reply("Привет!\nНапиши мне что-нибудь!")


@dp.message_handler(commands=['help'])
async def process_help_command(message: types.Message):
    await message.reply("")


@dp.message_handler(commands=['what_should_i_do'])
async def choose_activity(message: types.Message):
    i = randrange(len(list_of_activities))
    mes = "Ты мог бы, например, " + list_of_activities[i]
    await message.reply(mes)


@dp.message_handler(commands=['day_forecast'])
async def get_day_forecast(message: types.Message):
    i = randrange(len(list_of_forecasts))
    mes = "Звезды говорят, что " + list_of_forecasts[i]
    await message.reply(mes)


@dp.message_handler(commands=['cute_picture'])
async def get_cute_picture(message: types.Message):
    i = randrange(len(list_of_pictures))
    link = list_of_pictures[i]
    await bot.send_photo(message.chat.id, types.InputFile.from_url(link))


@dp.message_handler(commands=['interesting_fact'])
async def get_fact(message: types.Message):
    i = randrange(len(list_of_facts))
    mes = "Твой интересный факт на сегодня: " + list_of_facts[i]
    await message.reply(mes)


@dp.message_handler(commands=['my_exam_result'])
async def get_fact(message: types.Message):
    i = randrange(11)
    mes = "За экзамен ты получишь оценку " + str(i)
    await message.reply(mes)


@dp.message_handler()
async def echo(message: types.Message):
    mes = "Я такое не умею"
    await message.reply(mes)


if __name__ == '__main__':
    executor.start_polling(dp)