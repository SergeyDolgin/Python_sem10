import telebot
import requests

bot = telebot.TeleBot("5804959261:AAEym-Bg_ut63yUTonydZGFLbvzIsjA39W8")


global res
res = requests.get('https://www.cbr-xml-daily.ru/daily_json.js').json()

# print(res['Valute']['USD']['Name'], res['Valute']['USD']['Value'])
# print(res['Valute']['EUR']['Name'], res['Valute']['EUR']['Value'])
# print(res['Valute']['GBP']['Name'], res['Valute']['GBP']['Value'])
# print(res['Valute']['JPY']['Name'], res['Valute']['JPY']['Value'])
# print(res['Valute']['CNY']['Name'], res['Valute']['CNY']['Value'])
# print(res['Valute']['TRY']['Name'], res['Valute']['TRY']['Value'])




@bot.message_handler(commands=['hello'])
def send_welcome(message):
    bot.reply_to(message, "hello, User")
    
@bot.message_handler(commands=['usd'])
def send_usd(message):
    global res
    str_usd = str(res['Valute']['USD']['Name']) +' '+str(res['Valute']['USD']['Value'])
    bot.reply_to(message, str_usd)  

@bot.message_handler(commands=['eur'])
def send_eur(message):
    global res
    str_eur = str(res['Valute']['EUR']['Name']) +' '+str(res['Valute']['EUR']['Value'])
    bot.reply_to(message, str_eur)  
    
@bot.message_handler(commands=['gbp'])
def send_gbr(message):
    global res
    str_gbp = str(res['Valute']['GBP']['Name']) +' '+str(res['Valute']['GBP']['Value'])
    bot.reply_to(message, str_gbp)   
 
@bot.message_handler(commands=['cny'])
def send_gbr(message):
    global res
    str_cny = str(res['Valute']['CNY']['Name']) +' '+str(res['Valute']['CNY']['Value'])
    bot.reply_to(message, str_cny)   
 
@bot.message_handler(commands=['try'])
def send_gbr(message):
    global res
    str_try = str(res['Valute']['TRY']['Name']) +' '+str(res['Valute']['TRY']['Value'])
    bot.reply_to(message, str_try)   
    
@bot.message_handler(commands=['jpy'])
def send_gbr(message):
    global res
    str_jpy = str(res['Valute']['JPY']['Name']) +' '+str(res['Valute']['JPY']['Value'])
    bot.reply_to(message, str_jpy)   

@bot.message_handler(commands=['help'])
def send_gbr(message):
    instruction = ('Для получения курса иностранной валюты напечатайте /КОМАНДУ боту\n' +
    '/usd - американский доллар\n' +
    '/eur - евро\n' +
    '/gbr - британский фунт\n' + 
    '/try - турецкая лира\n' +
    '/jpy - японская йена\n' +
    '/cny - китайский юань\n')
    bot.reply_to(message, instruction)   

   
bot.infinity_polling()
