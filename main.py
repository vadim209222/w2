from aiogram import Bot, Dispatcher, types

from aiogram.types import CallbackQuery
from aiohttp import web
from config import TOKEN_API
from keyboards import main_kb, links_kb, payment_kb


bot = Bot(token=TOKEN_API)
Bot.set_current(bot)

dp = Dispatcher(bot)
app = web.Application()

webhook_path = f'/{TOKEN_API}'


async def set_webhook():
    webhook_uri = f'https://c883-91-215-91-37.ngrok-free.app{webhook_path}'
    await bot.set_webhook(
        webhook_uri
    )


async def on_startup(_):
    await set_webhook()


@dp.message_handler(commands=['start'])
async def send_welcome(message: types.Message):
    username = message.from_user.username
    user_id = message.chat.id
    await message.answer(f'Приветствую, {username}!\n\n'
                         'Это закрытый клуб по подписке. \nОстался всего один шаг для доступа!'
                         ' а также помогу с оплатой,На канале будет размещаться информация по '
                         'саморазвитию и мотивации, советы и практики как поддерживать здоровый образ жизни, '
                         'регулярно заниматься спортом, придерживаться здорового питания, также будут размещаться'
                         ' видео с тренировками, рекомендации книг и фильмов по теме. \n\nФорма оплаты — подписка с '
                         'автоматическим продлением.\nПереходя к оплате, Вы соглашаетесь с условиями '
                         'публичной оферты\nПрисоединиться👇🏻', reply_markup=main_kb)


@dp.callback_query_handler(lambda query: query.data == 'join')
async def process_join_callback(callback_query: CallbackQuery):
    await bot.send_message(callback_query.from_user.id,'Рада, что вы решили стать частью нашей команды\n\n'
                         'Нажимаем на кнопку "подписка на 30 дней" указываем номер телефона и оплачиваем,'
                         'после успешной оплаты перед вами появится кнопка "join group" -> Поздравляю, вы стали частью нашей семьи ❤️\n\n'
                         'Стоимость активации подписки 900р/месяц \n',
                         reply_markup=payment_kb)
    # удаление сообщения предыдущей команды
    await bot.delete_message(callback_query.message.chat.id, callback_query.message.message_id)



async def handle_webhook(request):
    uri = str(request.url)
    index = uri.rfind('/')
    token = uri[index+1:]

    if token ==TOKEN_API:
        request_data = await request.json()
        update = types.Update(**request_data)

        await dp.process_update(update)

        return web.Response()
    else:
        return web.Response(status=403)

app.router.add_post(f'/{TOKEN_API}', handle_webhook)


if __name__ == '__main__':
    app.on_startup.append(on_startup)

    web.run_app(
        app,
        host='0.0.0.0',
        port=8080
    )