import telebot
from config import TOKEN, keys
from extensions import ConvertionExcepton, CriptoConverter



bot = telebot.TeleBot(TOKEN)



@bot.message_handler(commands= ['start','help'])
def helper(message: telebot.types.Message):
    text = 'Чтобы начать работу введите одну из команд: \n <имя валюты> \
        <в какую валюту перевести> \
        <количество переводимой валюты>\
        \n Увидеть список возможных валют: /values'
    bot.reply_to(message, text)
    
@bot.message_handler(commands= ['values'])
def value(message: telebot.types.Message):
    text = 'Доступные валюты:'
    for key in keys.keys():
        text = '\n'.join((text, key, ))
        
    bot.reply_to(message, text)        


@bot.message_handler(content_types= ['text', ])
def convert(message: telebot.types.Message):
    try:
        values = message.text.split(' ')
    
        if len(values) != 3:
           raise ConvertionExcepton('Слишком много параметров')

        quote, base, amount = values
        total = CriptoConverter.convert(quote, base, amount) 
        price = float(total) * float(amount)  
    except ConvertionExcepton as e:
        bot.reply_to(message, f'Ошибка пользователя. \n{e}')

    except Exception as e:
        bot.reply_to(message, f'Не удалось обработать команду\n {e}')

    text = f'Цена {amount} {quote} в {base} = {price}'
    bot.send_message(message.chat.id, text)


bot.polling(non_stop=True)