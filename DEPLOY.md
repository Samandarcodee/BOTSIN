# 🚀 Railway'ga Deploy Qilish - To'liq Ko'rsatma

## Mini App to'liq ishlashi uchun qadamlar:

### 1️⃣ GitHub'ga kod yuklash

```bash
# Git repositoryni tekshiring
git status

# Barcha o'zgarishlarni qo'shing
git add .

# Commit qiling
git commit -m "Add Telegram Mini App"

# GitHub'ga yuklang
git push origin main
```

### 2️⃣ Railway'da loyiha yaratish

1. **Railway'ga kirish:**
   - [railway.app](https://railway.app) ga o'ting
   - "Start a New Project" ni bosing
   - GitHub orqali login qiling

2. **Repository tanlash:**
   - "Deploy from GitHub repo" ni tanlang
   - O'zingizning repositoryingizni tanlang
   - Railway avtomatik deploy qilishni boshlaydi

### 3️⃣ Environment Variables sozlash

**MUHIM:** Railway avtomatik deploy qilgandan keyin:

1. **Public URL ni olish:**
   - Railway dashboard'da loyihangizga o'ting
   - "Settings" tabiga o'ting
   - "Domains" yoki "Networking" bo'limida public URL ni ko'rasiz
   - Yoki "Deployments" tabida "View Logs" ni bosing va URL ni toping
   - Format: `https://your-project-name.railway.app`

2. **Environment Variables qo'shish:**
   - Railway dashboard'da loyihangizga o'ting
   - "Variables" tabiga o'ting
   - Quyidagi variable'larni qo'shing:

   ```
   BOT_TOKEN=your_bot_token_from_botfather
   WEBAPP_URL=https://your-project-name.railway.app
   ```

   **Eslatma:** `WEBAPP_URL` ni Railway sizga bergan to'liq URL bilan almashtiring!

3. **Railway'ni qayta deploy qilish:**
   - Variables qo'shgandan keyin Railway avtomatik qayta deploy qiladi
   - Yoki "Deployments" tabida "Redeploy" ni bosing

### 4️⃣ Tekshirish

1. **Bot ishlayotganini tekshirish:**
   - Telegram'da botingizga `/start` xabarini yuboring
   - "🚀 Mini App ni ochish" tugmasi ko'rinishi kerak

2. **Mini App ni test qilish:**
   - Telegram'da `/miniapp` komandasini yuboring
   - Tugmani bosing
   - Mini App ochilishi va "Salom!" ko'rinishi kerak

3. **Web App URL ni tekshirish:**
   - Brauzerda `https://your-project-name.railway.app` ga o'ting
   - Mini App HTML ko'rinishi kerak

### 5️⃣ Agar ishlamasa

#### Muammo: Mini App ochilmayapti

1. **WEBAPP_URL ni tekshiring:**
   - Railway dashboard'da Variables tabiga o'ting
   - WEBAPP_URL to'g'ri ekanligini tekshiring
   - URL `https://` bilan boshlanishi kerak
   - URL oxirida `/` bo'lmasligi kerak

2. **Railway loglarini tekshiring:**
   - Railway dashboard'da "Deployments" tabiga o'ting
   - "View Logs" ni bosing
   - Flask server ishga tushganini tekshiring
   - Xatoliklar bor-yo'qligini ko'ring

3. **Port muammosi:**
   - Railway avtomatik PORT environment variable ni beradi
   - Kodda Flask server PORT dan foydalanadi
   - Agar muammo bo'lsa, loglarda port xatoliklarini ko'rasiz

#### Muammo: Bot javob bermayapti

1. **BOT_TOKEN ni tekshiring:**
   - BotFather'dan token to'g'ri ekanligini tekshiring
   - Railway Variables'da to'g'ri qo'yilganligini tekshiring

2. **Loglarni tekshiring:**
   - Railway loglarida bot ishga tushganini ko'ring
   - Xatoliklar bor-yo'qligini tekshiring

### 6️⃣ Railway Public URL olish (batafsil)

Railway'da public URL ni olish uchun bir necha usul:

**Usul 1: Settings orqali**
1. Railway dashboard'da loyihangizga o'ting
2. "Settings" tabiga o'ting
3. "Generate Domain" yoki mavjud domain ni ko'ring
4. URL ni nusxalab oling

**Usul 2: Networking orqali**
1. Railway dashboard'da loyihangizga o'ting
2. "Networking" yoki "Settings" → "Networking" ga o'ting
3. Public domain ni ko'ring

**Usul 3: Deploy logs orqali**
1. Railway dashboard'da "Deployments" tabiga o'ting
2. Eng oxirgi deployment ni tanlang
3. "View Logs" ni bosing
4. Loglarda URL ni toping

**Usul 4: Custom domain**
1. Agar custom domain qo'shmoqchi bo'lsangiz
2. Railway Settings → Domains ga o'ting
3. Custom domain qo'shing
4. Bu URL ni WEBAPP_URL ga qo'ying

### 7️⃣ Production uchun optimizatsiya

1. **Railway'da auto-deploy:**
   - GitHub'ga push qilganda Railway avtomatik deploy qiladi
   - Settings → Source → Auto-deploy yoqilganligini tekshiring

2. **Monitoring:**
   - Railway dashboard'da metrics'larni kuzating
   - Loglarni muntazam tekshiring

3. **Backup:**
   - Environment variables'ni yozib oling
   - Bot token'ni xavfsiz joyda saqlang

## ✅ To'liq ishlash uchun tekshiruv ro'yxati:

- [ ] Kod GitHub'ga yuklangan
- [ ] Railway'da loyiha yaratilgan
- [ ] BOT_TOKEN environment variable qo'shilgan
- [ ] WEBAPP_URL environment variable qo'shilgan (Railway URL bilan)
- [ ] Railway deploy qilingan va muvaffaqiyatli ishlamoqda
- [ ] Telegram'da bot javob beradi
- [ ] Mini App tugmasi ko'rinadi
- [ ] Mini App ochiladi va "Salom!" ko'rinadi

## 📞 Yordam kerak bo'lsa

- Railway loglarini tekshiring
- Bot token'ni qayta tekshiring
- WEBAPP_URL ni qayta tekshiring
- GitHub'da kod yangilanganligini tekshiring

