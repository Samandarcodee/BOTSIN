import os
import logging
import threading
from typing import Optional
from flask import Flask, send_from_directory
from telegram import Update, WebAppInfo
from telegram.ext import Application, CommandHandler, MessageHandler, filters, ContextTypes
from telegram import InlineKeyboardButton, InlineKeyboardMarkup
from dotenv import load_dotenv

# Logging sozlamalari - avval sozlanadi
logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO
)
logger = logging.getLogger(__name__)

# .env faylini yuklash (agar mavjud bo'lsa) - encoding xatolariga qarshi himoya
try:
    load_dotenv(encoding='utf-8')
except Exception as e:
    logger.warning(f".env faylni yuklashda xatolik (ehtimol fayl yo'q): {e}")
    # Agar .env fayl bo'lmasa, environment variable dan o'qishga harakat qilamiz

# Bot tokenini environment variabledan olish
BOT_TOKEN = os.getenv('BOT_TOKEN')
if not BOT_TOKEN:
    raise ValueError("BOT_TOKEN environment variable topilmadi!")

# Web App URL (Railway yoki boshqa hosting URL)
WEBAPP_URL = os.getenv('WEBAPP_URL', 'https://your-app.railway.app')

# Flask server for Mini App
flask_app = Flask(__name__)

@flask_app.route('/')
def webapp_index():
    """Serve the mini app HTML file"""
    return send_from_directory('.', 'webapp.html')

@flask_app.route('/health')
def health():
    """Health check endpoint"""
    return {'status': 'ok'}, 200

def run_flask_server():
    """Flask serverni alohida threadda ishga tushirish"""
    # Railway PORT environment variabledan olish, agar bo'lmasa WEBAPP_PORT, yo'q bo'lsa 5000
    port = int(os.environ.get('PORT') or os.environ.get('WEBAPP_PORT', 5000))
    flask_app.run(host='0.0.0.0', port=port, debug=False)

# Start komandasi
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Start komandasi uchun handler"""
    if not update.message:
        return
    
    # Mini App button yaratish
    keyboard = [
        [InlineKeyboardButton(
            "🚀 Mini App ni ochish", 
            web_app=WebAppInfo(url=WEBAPP_URL)
        )]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    
    welcome_message = """
🤖 Salom! Men Telegram botman!

📋 Mavjud komandalar:
/start - Botni qayta ishga tushirish
/help - Yordam ma'lumotlari
/hello - Salomlashish
/about - Bot haqida ma'lumot
/miniapp - Zamonaviy Mini App ochish

Men sizning xabaringizni qaytarib yuboraman!
    """
    await update.message.reply_text(welcome_message, reply_markup=reply_markup)

# Help komandasi
async def help_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Help komandasi uchun handler"""
    if not update.message:
        return
    help_text = """
🆘 Yordam:

Bu bot sizning xabarlaringizni qaytarib yuboradi va oddiy komandalarni bajaradi.

📝 Komandalar:
• /start - Botni boshlash
• /help - Yordam ko'rsatish
• /hello - Salomlashish
• /about - Bot haqida
• /miniapp - Zamonaviy Mini App ochish

Sizga yordam kerak bo'lsa, menga xabar yuboring!
    """
    await update.message.reply_text(help_text)

# Hello komandasi
async def hello(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Hello komandasi uchun handler"""
    if not update.message:
        return
    user_name = update.effective_user.first_name if update.effective_user else "Foydalanuvchi"
    await update.message.reply_text(f"👋 Salom, {user_name}! Qanday yordam bera olaman?")

# Mini App komandasi
async def miniapp(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Mini App ochish uchun handler"""
    if not update.message:
        return
    
    keyboard = [
        [InlineKeyboardButton(
            "🚀 Mini App ni ochish", 
            web_app=WebAppInfo(url=WEBAPP_URL)
        )]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    
    await update.message.reply_text(
        "👋 Zamonaviy Telegram Mini App ni ochish uchun quyidagi tugmani bosing:",
        reply_markup=reply_markup
    )

# About komandasi
async def about(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """About komandasi uchun handler"""
    if not update.message:
        return
    about_text = """
ℹ️ Bot haqida:

Bu bot Railway platformasida deploy qilingan Python Telegram boti.

🔧 Texnologiyalar:
• Python 3
• python-telegram-bot
• Flask (Mini App server)
• Railway (deployment platform)
• Telegram Web App API

Bot oddiy komandalarni bajaradi, foydalanuvchi xabarlariga javob beradi va zamonaviy Mini App ni qo'llab-quvvatlaydi.
    """
    await update.message.reply_text(about_text)

# Echo handler - foydalanuvchi xabarlarini qaytarish
async def echo(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Foydalanuvchi xabarlarini qaytarib yuborish"""
    if not update.message or not update.message.text:
        return
    user_message = update.message.text
    await update.message.reply_text(f"📨 Sizning xabaringiz: {user_message}")

# Error handler
async def error_handler(update: Optional[Update], context: ContextTypes.DEFAULT_TYPE):
    """Errorlarni log qilish"""
    logger.error(f"Exception while handling an update: {context.error}", exc_info=context.error)
    
    # Foydalanuvchiga xatolik haqida xabar berish (agar update mavjud bo'lsa)
    if update and update.effective_message:
        try:
            await update.effective_message.reply_text(
                "❌ Xatolik yuz berdi. Iltimos, keyinroq qayta urinib ko'ring."
            )
        except Exception:
            # Agar xabar yuborishda xatolik bo'lsa, log qilamiz
            logger.error("Error sending error message to user")

def main():
    """Botni ishga tushirish"""
    try:
        logger.info("Bot ishga tushmoqda...")
        
        # Flask serverni alohida threadda ishga tushirish
        flask_thread = threading.Thread(target=run_flask_server, daemon=True)
        flask_thread.start()
        port = int(os.environ.get('PORT') or os.environ.get('WEBAPP_PORT', 5000))
        logger.info(f"Flask server {port} portda ishga tushdi (Mini App uchun)")
        
        # Application yaratish
        application = Application.builder().token(BOT_TOKEN).build()
        
        # Command handlerlarni qo'shish
        application.add_handler(CommandHandler("start", start))
        application.add_handler(CommandHandler("help", help_command))
        application.add_handler(CommandHandler("hello", hello))
        application.add_handler(CommandHandler("about", about))
        application.add_handler(CommandHandler("miniapp", miniapp))
        
        # Message handler - barcha text xabarlar uchun
        application.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, echo))
        
        # Error handler
        application.add_error_handler(error_handler)
        
        # Botni ishga tushirish
        logger.info("Bot ishga tushdi va xabarlarni kutmoqda...")
        application.run_polling(allowed_updates=Update.ALL_TYPES, drop_pending_updates=True)
    except Exception as e:
        logger.error(f"Botni ishga tushirishda xatolik: {e}", exc_info=True)
        raise

if __name__ == '__main__':
    main()

