from telegram.ext import Updater,CommandHandler, MessageHandler, Filters
import ephem, datetime
PROXY = {'proxy_url': 'socks5://t1.learn.python.ru:1080',
    'urllib3_proxy_kwargs': {'username': 'learn', 'password': 'python'}}
def greet_user(bot, update):
    print('Вызван /start')
    update.message.reply_text('Привет!')
def get_constellation(bot, update):
    planet_nm=update.message.text.split()[1] 
    planet_name=planet_nm.capitalize()
    print(planet_name)
    date =datetime.date.today()
    planet_obj = getattr(ephem, planet_name)(date)
    print(planet_name+' in '+ ephem.constellation(planet_obj)[1])
    update.message.reply_text(planet_name+' in '+ ephem.constellation(planet_obj)[1])
def main():
    mybot = Updater('1080427203:AAGu0s11hutdBWyOB1dJlIIfO0uGbek1ncQ', request_kwargs=PROXY)
    dp = mybot.dispatcher
    dp.add_handler(CommandHandler("start", greet_user))
    dp.add_handler(CommandHandler("planet", get_constellation))
    mybot.start_polling()
    mybot.idle()
main()
