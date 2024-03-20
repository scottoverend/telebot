import logging
from telegram import Update
from telegram.ext import ApplicationBuilder, ContextTypes, CommandHandler
from pycoingecko import CoinGeckoAPI

cg = CoinGeckoAPI()

async def send_price_btc(update: Update, context: ContextTypes.DEFAULT_TYPE):
    price_data = cg.get_price(ids='bitcoin', vs_currencies='usd')
    price = price_data['bitcoin']['usd']
    await context.bot.send_message(chat_id=update.effective_chat.id, text=f"The price of bitcoin is ${price}")

async def send_price_eth(update: Update, context: ContextTypes.DEFAULT_TYPE):
    price_data = cg.get_price(ids='ethereum', vs_currencies='usd')
    price = price_data['ethereum']['usd']
    await context.bot.send_message(chat_id=update.effective_chat.id, text=f"The price of ethereum is ${price}")

async def send_price_sol(update: Update, context: ContextTypes.DEFAULT_TYPE):
    price_data = cg.get_price(ids='solana', vs_currencies='usd')
    price = price_data['solana']['usd']
    await context.bot.send_message(chat_id=update.effective_chat.id, text=f"The price of solana is ${price}")

##def send_welcome(message):
        ##bot.reply_to(message, "Howdy")
        
if __name__ == '__main__':
    application = ApplicationBuilder().token('7082309788:AAHS2HHwLDjoeQE99zk68BUBr-RNcnVnw_Y').build()
    
    price_handler1 = CommandHandler('bitcoinprice', send_price_btc)
    
    price_handler2 = CommandHandler('ethereumprice', send_price_eth)
    
    price_handler3 = CommandHandler('solanaprice', send_price_sol)
    
    ##message = CommandHandler('hello', send_welcome)
    
    application.add_handler(price_handler1)
    
    application.add_handler(price_handler2)
    
    application.add_handler(price_handler3)
    

##the website is: 
