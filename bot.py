from telegram.ext import Updater,CommandHandler, MessageHandler, Filters
PROXY = {'proxy_url': 'socks5://t1.learn.python.ru:1080',
    'urllib3_proxy_kwargs': {'username': 'learn', 'password': 'python'}}
def greet_user(bot, update):
    print('Вызван /start')
    update.message.reply_text('Привет!')
def talk_to_me(bot, update):
    user_text = update.message.text 
    print(user_text)
    update.message.reply_text(user_text)
def main():
    mybot = Updater('1080427203:AAGu0s11hutdBWyOB1dJlIIfO0uGbek1ncQ', request_kwargs=PROXY)
    dp = mybot.dispatcher
    dp.add_handler(CommandHandler("start", greet_user))
    dp.add_handler(MessageHandler(Filters.text, talk_to_me))
    mybot.start_polling()
    mybot.idle()
main()
