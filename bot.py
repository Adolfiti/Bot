import telebot
from telebot import types
import data
from pp import parser

token = data.token
bot = telebot.TeleBot(token)
ref = data.ref
parser_data = parser(ref)
k = list(parser_data.keys())

@bot.message_handler(commands=['start'])
def handle_start(message):
    bot.send_message(message.chat.id, f"Привет, интересуешься криптовалютой?\nЯ тоже, поэтому давай посмотрим, что тут у нас есть!\nВоспользуйся командой /help, чтобы узнать, какие у меня есть функции!")
@bot.message_handler(commands=['help'])
def handle_start(message):
    bot.send_message(message.chat.id, f"/start - запуск работы бота\n/help - справка о командах бота\n/crypto - просмотр курса криптовалют")
@bot.message_handler(commands=['crypto'])
def send_countries(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    for coin in k:
        markup.add(types.KeyboardButton(coin))

    bot.send_message(message.chat.id, "Список криптовалют:", reply_markup=markup)

@bot.message_handler(content_types='text')
def message_reply(message):
    if message.text == 'Bitcoin':
        parser_data = parser(ref)
        price, link = parser_data['Bitcoin']
        bot.send_message(message.chat.id, f'{k[0]} — {price}\n{link}')

    if message.text == 'Ethereum':
        parser_data = parser(ref)
        price, link = parser_data['Ethereum']
        bot.send_message(message.chat.id, f'{k[1]} — {price}\n{link}')

    if message.text == 'TetherUS':
        parser_data = parser(ref)
        price, link = parser_data['TetherUS']
        bot.send_message(message.chat.id, f'{k[2]} — {price}\n{link}')

    if message.text == 'BNB':
        parser_data = parser(ref)
        price, link = parser_data['BNB']
        bot.send_message(message.chat.id, f'{k[3]} — {price}\n{link}')

    if message.text == 'Solana':
        parser_data = parser(ref)
        price, link = parser_data['Solana']
        bot.send_message(message.chat.id, f'{k[4]} — {price}\n{link}')

    if message.text == 'Ripple':
        parser_data = parser(ref)
        price, link = parser_data['Ripple']
        bot.send_message(message.chat.id, f'{k[5]} — {price}\n{link}')

    if message.text == 'USD Coin':
        parser_data = parser(ref)
        price, link = parser_data['USD Coin']
        bot.send_message(message.chat.id, f'{k[6]} — {price}\n{link}')

    if message.text == 'Cardano':
        parser_data = parser(ref)
        price, link = parser_data['Cardano']
        bot.send_message(message.chat.id, f'{k[7]} — {price}\n{link}')

    if message.text == 'Dogecoin':
        parser_data = parser(ref)
        price, link = parser_data['Dogecoin']
        bot.send_message(message.chat.id, f'{k[8]} — {price}\n{link}')

    if message.text == 'Avalanche':
        parser_data = parser(ref)
        price, link = parser_data['Avalanche']
        bot.send_message(message.chat.id, f'{k[9]} — {price}\n{link}')

    if message.text == 'SHIBA INU':
        parser_data = parser(ref)
        price, link = parser_data['SHIBA INU']
        bot.send_message(message.chat.id, f'{k[10]} — {price}\n{link}')

    if message.text == 'Polkadot':
        parser_data = parser(ref)
        price, link = parser_data['Polkadot']
        bot.send_message(message.chat.id, f'{k[11]} — {price}\n{link}')

    if message.text == 'ChainLink':
        parser_data = parser(ref)
        price, link = parser_data['ChainLink']
        bot.send_message(message.chat.id, f'{k[12]} — {price}\n{link}')

    if message.text == 'Polygon':
        parser_data = parser(ref)
        price, link = parser_data['Polygon']
        bot.send_message(message.chat.id, f'{k[13]} — {price}\n{link}')

    if message.text == 'TRON':
        parser_data = parser(ref)
        price, link = parser_data['TRON']
        bot.send_message(message.chat.id, f'{k[14]} — {price}\n{link}')

    if message.text == 'Wrapped Bitcoin':
        parser_data = parser(ref)
        price, link = parser_data['Wrapped Bitcoin']
        bot.send_message(message.chat.id, f'{k[15]} — {price}\n{link}')

    if message.text == 'NEAR Protocol':
        parser_data = parser(ref)
        price, link = parser_data['NEAR Protocol']
        bot.send_message(message.chat.id, f'{k[16]} — {price}\n{link}')

    if message.text == 'Bitcoin Cash':
        parser_data = parser(ref)
        price, link = parser_data['Bitcoin Cash']
        bot.send_message(message.chat.id, f'{k[17]} — {price}\n{link}')

    if message.text == 'Uniswap':
        parser_data = parser(ref)
        price, link = parser_data['Uniswap']
        bot.send_message(message.chat.id, f'{k[18]} — {price}\n{link}')

    if message.text == 'Litecoin':
        parser_data = parser(ref)
        price, link = parser_data['Litecoin']
        bot.send_message(message.chat.id, f'{k[19]} — {price}\n{link}')

    if message.text == 'Internet Computer':
        parser_data = parser(ref)
        price, link = parser_data['Internet Computer']
        bot.send_message(message.chat.id, f'{k[20]} — {price}\n{link}')

    if message.text == 'Aptos':
        parser_data = parser(ref)
        price, link = parser_data['Aptos']
        bot.send_message(message.chat.id, f'{k[21]} — {price}\n{link}')

    if message.text == 'Dai':
        parser_data = parser(ref)
        price, link = parser_data['Dai']
        bot.send_message(message.chat.id, f'{k[22]} — {price}\n{link}')

    if message.text == 'Filecoin':
        parser_data = parser(ref)
        price, link = parser_data['Filecoin']
        bot.send_message(message.chat.id, f'{k[23]} — {price}\n{link}')

    if message.text == 'Cosmos':
        parser_data = parser(ref)
        price, link = parser_data['Cosmos']
        bot.send_message(message.chat.id, f'{k[24]} — {price}\n{link}')

    if message.text == 'Ethereum Classic':
        parser_data = parser(ref)
        price, link = parser_data['Ethereum Classic']
        bot.send_message(message.chat.id, f'{k[25]} — {price}\n{link}')

    if message.text == 'Render Token':
        parser_data = parser(ref)
        price, link = parser_data['Render Token']
        bot.send_message(message.chat.id, f'{k[26]} — {price}\n{link}')

    if message.text == 'Injective':
        parser_data = parser(ref)
        price, link = parser_data['Injective']
        bot.send_message(message.chat.id, f'{k[27]} — {price}\n{link}')

    if message.text == 'ImmutableX':
        parser_data = parser(ref)
        price, link = parser_data['ImmutableX']
        bot.send_message(message.chat.id, f'{k[28]} — {price}\n{link}')

    if message.text == 'Hedera Hashgraph':
        parser_data = parser(ref)
        price, link = parser_data['Hedera Hashgraph']
        bot.send_message(message.chat.id, f'{k[29]} — {price}\n{link}')

bot.polling(none_stop=True)