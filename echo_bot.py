from telegram import Update, ReplyKeyboardMarkup, ReplyKeyboardRemove
from telegram.ext import Updater, MessageHandler, Filters, CallbackContext
from key import TOKEN

bd = load_workbook('database.xlsx')


def main():
    updater = Updater(
        token=TOKEN,
        use_context=True
    )

    # диспетчер распределяет сообщения по обработкам
    dispatcher = updater.dispatcher

    # создаем обработчик, который ловит все сообщения
    echo_handler = MessageHandler(Filters.all, do_echo)
    hello_handler = MessageHandler(Filters.text('Привет'), say_hello)
    keyboard_handler = MessageHandler(Filters.text('Клавиатура'), keyboard)

    # регестрируем обработчик
    dispatcher.add_handler(keyboard_handler)
    dispatcher.add_handler(hello_handler)
    dispatcher.add_handler(echo_handler)


    updater.start_polling()
    updater.idle()


def do_echo(update: Update, context: CallbackContext):
    name = update.message.from_user.first_name
    user_id = update.message.chat_id
    text = update.message.text if update.message.text else 'Текста нет'
    sticker = update.message.sticker
    update.message.reply_text(text=f'Ку, {name}!\n ты написал: {text}')


def say_hello(update: Update, context: CallbackContext):
    name = update.message.from_user.first_name
    user_id = update.message.chat_id
    text = update.message.text
    update.message.reply_text(text=f'Ку, {name}.\n'
                                   f'Я - бот, но тебя в бс нагну. _.\n'
                                   f'Как твои дела?')



def keyboard(update: Update, context: CallbackContext):
    buttons = [
        ['0I0', ';-;', '. _.'],
        ['Привет', 'пока']
    ]
    update.message.reply_text(
        text='Куб, теперь у тебя есть клавиатура',
        reply_markup=ReplyKeyboardMarkup(  # reply_markups=keys
            buttons,
            resize_keyboard=True,
            # one_tap_keyboard=True, # скрывает клавиатуру после её использования
        )
    )



if __name__ == '__main__':
        main()

