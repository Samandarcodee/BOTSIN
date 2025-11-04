# ⚡ Tezkor Deploy - Mini App ishlashi uchun

## Hozir bot ishlayapti, lekin Mini App ishlamayapti?

Quyidagi qadamlar bilan Mini App ni ishga tushiring:

### 1️⃣ Railway Dashboard'ga o'ting

1. [railway.app](https://railway.app) ga kirib o'ting
2. O'zingizning loyihangizni tanlang

### 2️⃣ Public URL ni oling

1. **Settings** tabiga o'ting
2. **Networking** yoki **Domains** bo'limiga o'ting
3. Railway sizga bergan URL ni ko'rasiz (masalan: `https://your-project.up.railway.app`)
4. **URL ni nusxalab oling!**

Yoki:
- **Deployments** tabiga o'ting
- Eng oxirgi deployment ni tanlang
- **View Logs** ni bosing
- Loglarda URL ni toping

### 3️⃣ WEBAPP_URL Environment Variable qo'shing

1. Railway dashboard'da loyihangizga o'ting
2. **Variables** tabiga o'ting
3. **New Variable** ni bosing
4. Quyidagilarni kiriting:
   - **Name:** `WEBAPP_URL`
   - **Value:** Yuqorida olgan URL ni kiriting (masalan: `https://your-project.up.railway.app`)
5. **Add** ni bosing

**MUHIM:**
- URL `https://` bilan boshlanishi kerak
- URL oxirida `/` bo'lmasligi kerak
- To'liq URL ni kiriting

### 4️⃣ Qayta Deploy qiling

1. **Deployments** tabiga o'ting
2. **Redeploy** tugmasini bosing
3. Deploy tugaguniga qadar kuting (2-3 minut)

### 5️⃣ Test qiling

1. Telegram'da botingizga `/start` yuboring
2. "🚀 Mini App ni ochish" tugmasi ko'rinishi kerak
3. Tugmani bosing
4. Mini App ochilishi va "Salom!" ko'rinishi kerak ✅

## ❌ Agar ishlamasa:

### Tekshiruvlar:

1. **WEBAPP_URL to'g'ri ekanligini tekshiring:**
   - Railway Variables tabida
   - URL to'liq va `https://` bilan boshlanishi kerak

2. **Brauzerda URL ni ochib tekshiring:**
   - Railway URL ni brauzerda oching
   - Mini App HTML ko'rinishi kerak
   - Agar xatolik ko'rsatsa, Flask server ishlamayapti

3. **Railway loglarini tekshiring:**
   - Deployments → View Logs
   - Flask server ishga tushganini ko'ring
   - Xatoliklar bor-yo'qligini tekshiring

4. **Qayta deploy qiling:**
   - Deployments → Redeploy
   - 2-3 minut kutib, qayta test qiling

## ✅ Muvaffaqiyatli sozlangan bo'lsa:

- Bot javob beradi ✅
- Mini App tugmasi ko'rinadi ✅
- Mini App ochiladi va "Salom!" ko'rinadi ✅
- Brauzerda Railway URL Mini App HTML ni ko'rsatadi ✅

