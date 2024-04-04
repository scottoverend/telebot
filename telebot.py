import logging
from telegram import Update
from telegram.ext import ApplicationBuilder, ContextTypes, CommandHandler
from pycoingecko import CoinGeckoAPI

cg = CoinGeckoAPI()

async def send_price_btc(update: Update, context: ContextTypes.DEFAULT_TYPE):
    context.bot.send_message(chat_id=update.effective_chat.id, text=f".................")
    price_data = cg.get_price(ids='bitcoin', vs_currencies='usd')
    price = price_data['bitcoin']['usd']
    await context.bot.send_message(chat_id=update.effective_chat.id, text=f"The price of bitcoin is ${price}")

async def send_price_eth(update: Update, context: ContextTypes.DEFAULT_TYPE):
    context.bot.send_message(chat_id=update.effective_chat.id, text=f".................")
    price_data = cg.get_price(ids='ethereum', vs_currencies='usd')
    price = price_data['ethereum']['usd']
    await context.bot.send_message(chat_id=update.effective_chat.id, text=f"The price of ethereum is ${price}")
    
async def send_price_sol(update: Update, context: ContextTypes.DEFAULT_TYPE):
    context.bot.send_message(chat_id=update.effective_chat.id, text=f".................")
    price_data = cg.get_price(ids='solana', vs_currencies='usd')
    price = price_data['solana']['usd']
    await context.bot.send_message(chat_id=update.effective_chat.id, text=f"The price of solana is ${price}")
    
    
async def say_hello(update: Update, context: ContextTypes.DEFAULT_TYPE):
    context.bot.send_message(chat_id=update.effective_chat.id, text=f".................")
    await context.bot.send_message(chat_id=update.effective_chat.id, text=f"Hello!")
    
    
if __name__ == '__main__':
    application = ApplicationBuilder().token('7082309788:AAHS2HHwLDjoeQE99zk68BUBr-RNcnVnw_Y').build()
    
    price_handler1 = CommandHandler('bitcoinprice', send_price_btc)
    
    price_handler2 = CommandHandler('ethereumprice', send_price_eth)
    
    price_handler3 = CommandHandler('solanaprice', send_price_sol)
    
    hello_handler4 = CommandHandler('hello', say_hello)
    
    application.add_handler(price_handler1)
    
    application.add_handler(price_handler2)
    
    application.add_handler(price_handler3)
    
    application.add_handler(hello_handler4)
    
    application.run_polling()
    
    
# fairly deep explanation: https://github.com/ggerganov/llama.cpp#build 
# https://vishnu.im/posts/run-your-own-ai-bot-with-llama-telegram-bot/
# https://github.com/abetlen/llama-cpp-python?tab=readme-ov-file
# https://github.com/ggerganov/llama.cpp#build
# https://github.com/ggerganov/llama.cpp/tree/ac43576124a75c2de6e333ac31a3444ff9eb9458?tab=readme-ov-file#hot-topics
