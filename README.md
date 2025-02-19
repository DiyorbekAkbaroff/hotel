# Mehmonxona Boshqaruv Sayti

Bu loyiha **Python (Flask)** va **MySQL** yordamida yaratilgan oddiy mehmonxona boshqaruv tizimidir. Loyiha backend uchun Flask, front uchun Jinja va ma’lumotlar bazasi uchun MySQL-dan foydalanadi.

---

## Talablar

Loyihani ishga tushirish uchun quyidagilar o‘rnatilgan bo‘lishi kerak:

- **Python**: 3.12 yoki undan yuqori versiya
- **Flask**: Web-framework
- **MySQL Connector**: `mysql-connector-python`
- **Jinja**: Flask ichida o‘rnatilgan template dvigatel

---

## O‘rnatish va Sozlash

### 1-qadam: Repozitoriyani yuklab olish
```bash
git clone <repository-url>
cd <project-folder>
```

### 2-qadam: Virtual muhit yaratish va faollashtirish
```bash
python3.12 -m venv venv
source venv/bin/activate    # Linux/Mac uchun
venv\Scripts\activate       # Windows uchun
```

### 3-qadam: Zaruriy kutubxonalarni o‘rnatish
```bash
pip install flask mysql-connector-python
```

---

## Ma'lumotlar Bazasi Sozlamalari

1. **MySQL Bazasi Yaratish**:
   - MySQL mijozingizni (masalan, MySQL Workbench yoki CLI) oching.
   - Ma'lumotlar bazasini yarating:
     ```sql
     CREATE DATABASE hotel_management;
     ```

2. **Konfiguratsiyani Yangilash**:
   - Loyiha papkasida `config.py` faylini oching va ma'lumotlar bazasi sozlamalarini yangilang:
     ```python
     DB_CONFIG = {
         "host": "localhost",
         "user": "foydalanuvchi_nomi",
         "password": "foydalanuvchi_paroli",
         "database": "hotel_management"
     }
     ```

---

## Loyihani Ishga Tushirish

1. Flask serverini ishga tushirish:
   ```bash
   flask run
   ```

2. Brauzerda quyidagi manzilni oching:
   ```
   http://127.0.0.1:5000
   ```

---

## Loyiha Tuzilishi

```
project-folder/
│
├── templates/        # HTML shablonlar
├── static/           # CSS, JS, Rasmlar va boshqa fayllar
├── app.py            # Asosiy ilova fayli
├── config.py         # Sozlamalar (masalan, ma'lumotlar bazasi)
├── models.py         # Ma'lumotlar bazasi modellari
├── routes.py         # Ilova yo‘nalishlari (routes)
└── README.md         # Loyiha haqida ma'lumot
```

---

## Funksiyalar

- **Xonalarni Band Qilish**: Mavjud bo‘lgan xonalarni band qilish imkoniyati.
- **Mijozlarni Boshqarish**: Mijozlar ma’lumotlarini boshqarish.
- **Xonalarni Boshqarish**: Xona ma’lumotlarini qo‘shish, yangilash yoki o‘chirish.
- **Dinamik Sahifalar**: Jinja shablonlari yordamida dinamik HTML yaratish.

---

## Kelajakdagi Yaxshilanishlar

- Foydalanuvchilar va administratorlar uchun autentifikatsiya qo‘shish.
- To‘lov tizimini integratsiya qilish.
- UI dizaynini yaxshilash uchun oldingi frameworklardan foydalanish (Bootstrap yoki Tailwind).

---

