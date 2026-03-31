# O'zbek Tilidagi Matn Korpusi Generatori

Bu loyiha O'zbek tilidagi tasodifiy matn va korpusni yaratish uchun mo'ljallangan Python dasturidir.

## Xususiyatlari

- 🇺🇿 O'zbek tilidagi so'zlardan foydalanish
- 🔄 Turli xil gap shablonlari
- 📊 Katta hajmdagi matn fayillarini yaratish
- 💾 UTF-8 kodlash bilan ishlash
- 📈 Yaratilish jarayonini kuzatish

## O'rnatish

```bash
git clone https://github.com/khujayorov/birmlnsoz.git
cd birmlnsoz
```

## Ishlatish

```python
from main import UzbekCorpusGenerator

# Generatorni yaratish
generator = UzbekCorpusGenerator(target_words=1_000_000)

# Korpusni yaratish
generator.create_corpus("uzbek_corpus.txt")
```

## Natija

Dastur:
- Belgilangan sondagi so'zlardan iborat O'zbek matnini yaratadi
- Yaratilgan matnni `uzbek_corpus.txt` fayliga saqlaydi
- Yaratilish jarayonini konsolda ko'rsatadi

## Muallif

Khujayorov

## Litsenziya

MIT
