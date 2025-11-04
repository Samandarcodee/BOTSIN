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

### 3. Railway'ga Deploy qilish (Mini App bilan)

#### Variant 1: GitHub orqali (Tavsiya etiladi)

1. **Loyihani GitHub'ga yuklang:**
   ```bash
   git init
   git add .
   git commit -m "Add Mini App support"
   git remote add origin https://github.com/yourusername/your-repo.git
   git push -u origin main
   ```

2. **Railway'da yangi loyiha yarating:**
   - [Railway](https://railway.com/) ga kirib o'ting
   - "New Project" ni bosing
   - "Deploy from GitHub Repo" ni tanlang
   - GitHub repositoryingizni tanlang
   - Railway avtomatik deploy qilishni boshlaydi

3. **Public URL ni olish (MUHIM!):**
   - Railway deploy qilgandan keyin, dashboard'da loyihangizga o'ting
   - **Settings** tabiga o'ting
   - **Networking** yoki **Domains** bo'limiga o'ting
   - Railway sizga bergan public URL ni ko'rasiz (masalan: `https://your-project-name.up.railway.app`)
   - Yoki **Deployments** tabida **View Logs** ni bosing va URL ni toping
   - **URL ni nusxalab oling!**

4. **Environment Variables qo'shish:**
   - Railway dashboard'da loyihangizga o'ting
   - **Variables** tabiga o'ting
   - Quyidagi variable'larni qo'shing:
   
   ```
   BOT_TOKEN=your_bot_token_from_botfather
   WEBAPP_URL=https://your-project-name.up.railway.app
   ```
   
   **MUHIM:** `WEBAPP_URL` ni yuqorida olgan public URL bilan almashtiring!
   - URL `https://` bilan boshlanishi kerak
   - URL oxirida `/` bo'lmasligi kerak
   - Har bir variable ni qo'shgandan keyin "Add" ni bosing

5. **Qayta deploy qilish:**
   - Variables qo'shgandan keyin Railway avtomatik qayta deploy qiladi
   - Yoki **Deployments** tabida **Redeploy** ni bosing
   - Deploy tugaguniga qadar kuting (2-3 minut)

6. **Tekshirish:**
   - Telegram'da botingizga `/start` yuboring
   - "🚀 Mini App ni ochish" tugmasi ko'rinishi kerak
   - Tugmani bosing - Mini App ochilishi va "Salom!" ko'rinishi kerak

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

4. **Public URL ni olish:**
   - Railway dashboard'da loyihangizga o'ting
   - Settings → Networking yoki Domains dan public URL ni oling
   - URL ni nusxalab oling

5. **Environment Variables qo'shish:**
   ```bash
   railway variables set BOT_TOKEN=your_bot_token_here
   railway variables set WEBAPP_URL=https://your-project-name.up.railway.app
   ```
   **MUHIM:** `WEBAPP_URL` ni yuqorida olgan public URL bilan almashtiring!

6. **Deploy qilish:**
   ```bash
   railway up
   ```

7. **Tekshirish:**
   - Telegram'da `/miniapp` komandasini yuboring
   - Mini App tugmasini bosing va test qiling

## 📋 Bot komandalari

- `/start` - Botni boshlash (Mini App button bilan)
- `/help` - Yordam ko'rsatish
- `/hello` - Salomlashish
- `/about` - Bot haqida ma'lumot
- `/miniapp` - Zamonaviy Telegram Mini App ochish

Bot barcha text xabarlarni ham qaytarib yuboradi (echo mode).

## 🚀 Telegram Mini App

Bu bot zamonaviy Telegram Mini App ni qo'llab-quvvatlaydi. Mini App orqali:
- ✨ Zamonaviy gradient dizayn
- 🎨 Animatsiyalar va vizual effektlar
- 👤 Foydalanuvchi ma'lumotlarini ko'rsatish
- 📱 To'liq ekran rejim

Mini App ni ochish uchun `/start` yoki `/miniapp` komandasini bosing va tugmani bosing.

## 🔧 Texnologiyalar

- **Python 3.11**
- **python-telegram-bot** - Telegram Bot API wrapper
- **Flask** - Mini App web server
- **Telegram Web App API** - Mini App integratsiyasi
- **Railway** - Deployment platform

## 📝 Fayl tuzilishi

```
.
├── bot.py              # Asosiy bot kodi (Flask server bilan)
├── webapp.html         # Telegram Mini App HTML fayli
├── requirements.txt    # Python dependencies
├── Procfile           # Railway uchun process file
├── runtime.txt        # Python versiyasi
├── .env.example       # Environment variable template
└── README.md          # Bu fayl
```

## ⚠️ Muhim eslatmalar

1. **BOT_TOKEN ni hech qachon GitHub'ga yuklamang!**
2. Railway'da environment variable sifatida qo'shing
3. **WEBAPP_URL ni Railway deploy qilgandan keyin o'rnating** - Railway sizga public URL beradi
4. **WEBAPP_URL ni to'g'ri sozlash juda muhim!** - Agar to'g'ri sozlanmagan bo'lsa, Mini App ishlamaydi
5. Bot ishlamasa, Railway loglarini tekshiring
6. Bot polling rejimida ishlaydi, shuning uchun doimiy connection kerak
7. Mini App HTTPS orqali ishlaydi, Railway avtomatik HTTPS ta'minlaydi

## 📖 Batafsil Deploy Ko'rsatmasi

To'liq deploy qilish bo'yicha batafsil ko'rsatma uchun [DEPLOY.md](DEPLOY.md) faylini ko'ring.

## 🐛 Muammolarni hal qilish

### Bot ishlamayapti
- Railway loglarini tekshiring
- BOT_TOKEN to'g'ri qo'shilganligini tekshiring
- BotFather'dan botni `/start` qilib ko'ring

### Mini App ochilmayapti
- **WEBAPP_URL ni tekshiring** - Bu eng ko'p uchraydigan muammo!
- Railway dashboard'da Variables tabida WEBAPP_URL to'g'ri ekanligini tekshiring
- URL `https://` bilan boshlanishi kerak
- URL oxirida `/` bo'lmasligi kerak
- Brauzerda URL ni ochib tekshiring - HTML ko'rinishi kerak
- Railway loglarida Flask server ishga tushganini tekshiring
- Agar muammo davom etsa, Railway'ni qayta deploy qiling

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

