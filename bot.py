import logging
from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes
from tonconnect import TonConnect

from config import BOT_TOKEN, TONKEEPER_WALLET

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Welcome to LuckifyGameBot! Use /withdraw to get your TON.")

async def withdraw(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user_id = update.effective_user.id
    wallet = TonConnect(wallet_address=TONKEEPER_WALLET)
    result = wallet.send_ton(user_id=user_id, amount=0.5)  # Example amount
    if result['status'] == 'success':
        await update.message.reply_text("Withdrawal successful!")
    else:
        await update.message.reply_text("Withdrawal failed.")

if __name__ == '__main__':
    app = ApplicationBuilder().token(BOT_TOKEN).build()
    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler("withdraw", withdraw))
    app.run_polling()