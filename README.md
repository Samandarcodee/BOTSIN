# BOTSIN

# Telegram Bot - Railway Deployment

Bu loyiha Railway platformasida deploy qilingan oddiy Telegram bot.

## 🚀 Tezkor boshlash

### 1. Bot Token olish

1. Telegram'da [@BotFather](https://t.me/BotFather) ga yozing
2. `/newbot` komandasini yuboring
3. Bot nomini va username'ni kiriting
4. BotFather sizga `BOT_TOKEN` beradi

### 2. Lokal test qilish

```bash
# Virtual environment yaratish
python -m venv venv

# Virtual environmentni aktivlashtirish
# Windows:
venv\Scripts\activate
# Linux/Mac:
source venv/bin/activate

# Dependencies o'rnatish
pip install -r requirements.txt

# .env fayl yaratish va BOT_TOKEN ni qo'yish
copy .env.example .env
# Yoki .env faylni ochib BOT_TOKEN ni qo'ying

# Botni ishga tushirish
python bot.py
```

### 3. Railway'ga Deploy qilish

#### Variant 1: GitHub orqali (Tavsiya etiladi)

1. **Loyihani GitHub'ga yuklang:**
   ```bash
   git init
   git add .
   git commit -m "Initial commit"
   git remote add origin https://github.com/yourusername/your-repo.git
   git push -u origin main
   ```

2. **Railway'da yangi loyiha yarating:**
   - [Railway](https://railway.com/) ga kirib o'ting
   - "New Project" ni bosing
   - "Deploy from GitHub Repo" ni tanlang
   - GitHub repositoryingizni tanlang

3. **Environment Variable qo'shing:**
   - Railway dashboard'da "Variables" tabiga o'ting
   - `BOT_TOKEN` ni qo'shing va BotFather'dan olgan tokeningizni qo'ying
   - "Add" ni bosing

4. **Deploy:**
   - Railway avtomatik ravishda deploy qiladi
   - Loglarni "Deploy Logs" dan ko'rishingiz mumkin

#### Variant 2: Railway CLI orqali

1. **Railway CLI o'rnatish:**
   ```bash
   npm i -g @railway/cli
   ```

2. **Railway'ga kirish:**
   ```bash
   railway login
   ```

3. **Yangi loyiha yaratish:**
   ```bash
   railway init
   ```

4. **Environment Variable qo'shish:**
   ```bash
   railway variables set BOT_TOKEN=your_bot_token_here
   ```

5. **Deploy qilish:**
   ```bash
   railway up
   ```

## 📋 Bot komandalari

- `/start` - Botni boshlash
- `/help` - Yordam ko'rsatish
- `/hello` - Salomlashish
- `/about` - Bot haqida ma'lumot

Bot barcha text xabarlarni ham qaytarib yuboradi (echo mode).

## 🔧 Texnologiyalar

- **Python 3.11**
- **python-telegram-bot** - Telegram Bot API wrapper
- **Railway** - Deployment platform

## 📝 Fayl tuzilishi

```
.
├── bot.py              # Asosiy bot kodi
├── requirements.txt    # Python dependencies
├── Procfile           # Railway uchun process file
├── runtime.txt        # Python versiyasi
├── .env.example       # Environment variable template
└── README.md          # Bu fayl
```

## ⚠️ Muhim eslatmalar

1. **BOT_TOKEN ni hech qachon GitHub'ga yuklamang!**
2. Railway'da environment variable sifatida qo'shing
3. Bot ishlamasa, Railway loglarini tekshiring
4. Bot polling rejimida ishlaydi, shuning uchun doimiy connection kerak

## 🐛 Muammolarni hal qilish

### Bot ishlamayapti
- Railway loglarini tekshiring
- BOT_TOKEN to'g'ri qo'shilganligini tekshiring
- BotFather'dan botni `/start` qilib ko'ring

### Deployment xatosi
- `requirements.txt` da barcha dependencies borligini tekshiring
- Python versiyasi `runtime.txt` da to'g'ri ekanligini tekshiring
- Railway'da "Build Logs" ni ko'rib chiqing

## 📚 Qo'shimcha ma'lumot

- [python-telegram-bot documentation](https://python-telegram-bot.org/)
- [Railway documentation](https://docs.railway.app/)
- [Telegram Bot API](https://core.telegram.org/bots/api)

## 📄 License

Bu loyiha ochiq manba loyiha sifatida foydalanish mumkin.

