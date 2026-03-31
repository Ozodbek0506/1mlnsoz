import random
import json
from datetime import datetime

class UzbekCorpusGenerator:
    def __init__(self, target_words=1_000_000):
        self.target_words = target_words
        
        # O'zbek tilidagi asosiy so'zlar
        self.words = [
            "salom", "dunyo", "o'zbekiston", "toshkent", "samarqand", "buxoro",
            "andijon", "namangan", "qarshi", "termiz", "navoiy", "xiva",
            "olma", "anor", "uzum", "tarvuz", "qovun", "shaftoli", "gilos", "olcha",
            "non", "suv", "choy", "shakar", "tuz", "un", "yog'", "go'sht", "baliq",
            "uy", "ko'cha", "shahar", "qishloq", "daryo", "tog'", "dala", "bog'",
            "kitob", "qalam", "daftar", "maktab", "o'qituvchi", "o'quvchi", "talaba",
            "ish", "mehnat", "vaqt", "kun", "oy", "yil", "asr", "soat", "daqiqa",
            "kelajak", "tarix", "ilm", "fan", "texnologiya", "internet", "kompyuter",
            "go'zal", "chiroyli", "katta", "kichik", "yangi", "eski", "yaxshi", "yomon",
            "issiq", "sovuq", "uzoq", "yaqin", "tez", "sekin", "baland", "past",
            "va", "bilan", "uchun", "sari", "haqida", "keyin", "oldin", "doim",
            "ishlamoq", "o'qimoq", "yozmoq", "gapirmoq", "yurmoq", "kelmoq", "ketmoq",
            "qilmoq", "bo'lmoq", "ko'rmoq", "bilmoq", "olmoq", "bermoq", "aytmoq",
            "men", "sen", "u", "biz", "siz", "ular", "bu", "shu"
        ]
        
        # Gap shablonlari
        self.templates = [
            "{word1} {word2} {word3}.",
            "Bugun {word1} {word2} {word3}.",
            "{word1} va {word2} {word3} {word4}.",
            "{word1} {word2} uchun {word3}.",
            "Ertaga {word1} {word2} bo'ladi.",
            "{word1} {word2} da juda {word3}.",
            "Men {word1} {word2} ni {word3}.",
            "U {word1} {word2} bilan {word3}.",
            "Biz {word1} va {word2} {word3}.",
            "Qachon {word1} {word2} {word3}?",
            "{word1} {word2} {word3}mi?",
            "Ha, {word1} {word2} {word3}.",
            "Yo'q, {word1} {word2} emas.",
            "{word1} {word2} {word3} deb o'ylayman.",
            "Mening fikrimcha, {word1} {word2}.",
            "{word1} {word2} {word3} kerak.",
            "{word1} {word2} {word3} mumkin.",
            "Iltimos, {word1} {word2} {word3}.",
            "Kechirasiz, {word1} {word2} {word3}.",
            "Rahmat, {word1} {word2} {word3}."
        ]
    
    def generate_sentence(self):
        """Random gap yaratish"""
        template = random.choice(self.templates)
        word_count = template.count("{word")
        
        words = []
        for i in range(word_count):
            word = random.choice(self.words)
            words.append(word)
        
        sentence = template
        for i, word in enumerate(words, 1):
            sentence = sentence.replace(f"{{word{i}}}", word)
        
        return sentence
    
    def create_corpus(self, output_file="uzbek_corpus.txt"):
        """Korpusni yaratish"""
        print(f"Korpus yaratish boshlandi...")
        print(f"Maqsad: {self.target_words:,} so'z")
        print(f"Fayl: {output_file}")
        print("-" * 40)
        
        total_words = 0
        sentences = []
        batch_size = 1000  # Bir vaqtda 1000 gap yozish
        
        with open(output_file, 'w', encoding='utf-8') as f:
            while total_words < self.target_words:
                sentence = self.generate_sentence()
                sentence_words = len(sentence.split())
                total_words += sentence_words
                sentences.append(sentence)
                
                # Batch bo'lib yozish
                if len(sentences) >= batch_size:
                    f.write('\n'.join(sentences))
                    f.write('\n')
                    sentences = []
                    
                    # Progressni ko'rsatish
                    progress = (total_words / self.target_words) * 100
                    print(f"Yaratildi: {total_words:>10,} so'z ({progress:>5.1f}%)")
            
            # Qolgan gaplarni yozish
            if sentences:
                f.write('\n'.join(sentences))
        
        print("-" * 40)
        print(f"\n✅ Korpus yaratildi!")
        print(f"   Fayl: {output_file}")
        print(f"   Jami so'zlar: {total_words:,}")
        print(f"   Jami gaplar: {total_words // 10:,} (taxminan)")
        
        return total_words

# Foydalanish
if __name__ == "__main__":
    print("=" * 50)
    print("   1 MILLION SO'ZLIK O'ZBEK KORPUSI")
    print("=" * 50)
    
    # Korpusni yaratish
    generator = UzbekCorpusGenerator(target_words=1_000_000)
    generator.create_corpus("uzbek_corpus_1m.txt")
    
    print("\n" + "=" * 50)
    print("Korpus muvaffaqiyatli yaratildi!")
    print("=" * 50)