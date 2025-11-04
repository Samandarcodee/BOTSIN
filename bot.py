import os
import logging
from telegram import Update
from telegram.ext import Application, CommandHandler, MessageHandler, filters, ContextTypes

# Logging sozlamalari
logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO
)
logger = logging.getLogger(__name__)

# Bot tokenini environment variabledan olish
BOT_TOKEN = os.getenv('BOT_TOKEN')
if not BOT_TOKEN:
    raise ValueError("BOT_TOKEN environment variable topilmadi!")

# Start komandasi
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Start komandasi uchun handler"""
    welcome_message = """
🤖 Salom! Men Telegram botman!

📋 Mavjud komandalar:
/start - Botni qayta ishga tushirish
/help - Yordam ma'lumotlari
/hello - Salomlashish
/about - Bot haqida ma'lumot

Men sizning xabaringizni qaytarib yuboraman!
    """
    await update.message.reply_text(welcome_message)

# Help komandasi
async def help_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Help komandasi uchun handler"""
    help_text = """
🆘 Yordam:

Bu bot sizning xabarlaringizni qaytarib yuboradi va oddiy komandalarni bajaradi.

📝 Komandalar:
• /start - Botni boshlash
• /help - Yordam ko'rsatish
• /hello - Salomlashish
• /about - Bot haqida

Sizga yordam kerak bo'lsa, menga xabar yuboring!
    """
    await update.message.reply_text(help_text)

# Hello komandasi
async def hello(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Hello komandasi uchun handler"""
    user_name = update.effective_user.first_name
    await update.message.reply_text(f"👋 Salom, {user_name}! Qanday yordam bera olaman?")

# About komandasi
async def about(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """About komandasi uchun handler"""
    about_text = """
ℹ️ Bot haqida:

Bu bot Railway platformasida deploy qilingan Python Telegram boti.

🔧 Texnologiyalar:
• Python 3
• python-telegram-bot
• Railway (deployment platform)

Bot oddiy komandalarni bajaradi va foydalanuvchi xabarlariga javob beradi.
    """
    await update.message.reply_text(about_text)

# Echo handler - foydalanuvchi xabarlarini qaytarish
async def echo(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Foydalanuvchi xabarlarini qaytarib yuborish"""
    user_message = update.message.text
    await update.message.reply_text(f"📨 Sizning xabaringiz: {user_message}")

# Error handler
async def error_handler(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Errorlarni log qilish"""
    logger.error(f"Update {update} caused error {context.error}")

def main():
    """Botni ishga tushirish"""
    logger.info("Bot ishga tushmoqda...")
    
    # Application yaratish
    application = Application.builder().token(BOT_TOKEN).build()
    
    # Command handlerlarni qo'shish
    application.add_handler(CommandHandler("start", start))
    application.add_handler(CommandHandler("help", help_command))
    application.add_handler(CommandHandler("hello", hello))
    application.add_handler(CommandHandler("about", about))
    
    # Message handler - barcha text xabarlar uchun
    application.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, echo))
    
    # Error handler
    application.add_error_handler(error_handler)
    
    # Botni ishga tushirish
    logger.info("Bot ishga tushdi va xabarlarni kutmoqda...")
    application.run_polling(allowed_updates=Update.ALL_TYPES)

if __name__ == '__main__':
    main()

