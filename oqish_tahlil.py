import random
import json
from collections import Counter

# ============ KORPUS GENERATOR SINFI ============
class UzbekCorpusGenerator:
    def __init__(self, target_words=1_000_000):
        self.target_words = target_words
        
        # O'zbek tilidagi asosiy so'zlar
        self.words = [
            "salom", "dunyo", "o'zbekiston", "toshkent", "samarqand", "buxoro",
            "olma", "anor", "uzum", "non", "suv", "choy", "kitob", "maktab",
            "uy", "ish", "vaqt", "kun", "yil", "kelajak", "tarix", "ilm",
            "go'zal", "chiroyli", "katta", "kichik", "yangi", "eski",
            "yaxshi", "yomon", "issiq", "sovuq", "tez", "sekin",
            "va", "bilan", "uchun", "haqida", "keyin", "oldin",
            "ishlamoq", "o'qimoq", "yozmoq", "gapirmoq", "kelmoq", "ketmoq",
            "men", "sen", "u", "biz", "siz", "ular", "bu", "shu"
        ]
        
        # Gap shablonlari
        self.templates = [
            "{word1} {word2} {word3}.",
            "Bugun {word1} {word2} {word3}.",
            "{word1} va {word2} {word3} {word4}.",
            "{word1} {word2} uchun {word3}.",
            "Ertaga {word1} {word2} bo'ladi.",
            "Men {word1} {word2} ni {word3}.",
            "U {word1} {word2} bilan {word3}.",
            "Biz {word1} va {word2} {word3}.",
            "Qachon {word1} {word2} {word3}?",
            "Ha, {word1} {word2} {word3}.",
            "Yo'q, {word1} {word2} emas."
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
        
        total_words = 0
        sentences = []
        batch_size = 1000
        
        with open(output_file, 'w', encoding='utf-8') as f:
            while total_words < self.target_words:
                sentence = self.generate_sentence()
                sentence_words = len(sentence.split())
                total_words += sentence_words
                sentences.append(sentence)
                
                if len(sentences) >= batch_size:
                    f.write('\n'.join(sentences))
                    f.write('\n')
                    sentences = []
                    
                    progress = (total_words / self.target_words) * 100
                    print(f"Yaratildi: {total_words:,} so'z ({progress:.1f}%)")
            
            if sentences:
                f.write('\n'.join(sentences))
        
        print(f"\n✅ Korpus yaratildi!")
        print(f"Fayl: {output_file}")
        print(f"Jami so'zlar: {total_words:,}")
        
        return total_words

# ============ KORPUS ANALYZER SINFI ============
class CorpusAnalyzer:
    def __init__(self, filename):
        self.filename = filename
    
    def read_corpus(self):
        """Korpusni o'qish"""
        try:
            with open(self.filename, 'r', encoding='utf-8') as f:
                return f.read()
        except FileNotFoundError:
            print(f"⚠️ {self.filename} fayli topilmadi!")
            return ""
    
    def get_statistics(self):
        """Korpus statistikasini olish"""
        text = self.read_corpus()
        if not text:
            return {}
        
        words = text.split()
        sentences = [s for s in text.split('\n') if s.strip()]
        
        stats = {
            "total_words": len(words),
            "total_sentences": len(sentences),
            "unique_words": len(set(words)),
            "average_word_length": sum(len(w) for w in words) / len(words) if words else 0,
            "average_sentence_length": len(words) / len(sentences) if sentences else 0
        }
        
        return stats
    
    def get_word_frequency(self, top_n=20):
        """Eng ko'p ishlatilgan so'zlar"""
        text = self.read_corpus()
        if not text:
            return []
        
        words = text.split()
        counter = Counter(words)
        return counter.most_common(top_n)
    
    def search_word(self, word):
        """So'zni qidirish"""
        text = self.read_corpus()
        if not text:
            return []
        
        lines = text.split('\n')
        
        results = []
        for i, line in enumerate(lines):
            if word in line:
                results.append((i+1, line.strip()))
                if len(results) >= 10:
                    break
        
        return results
    
    def export_to_json(self, output_file="corpus_stats.json"):
        """Statistikani JSON formatda saqlash"""
        stats = self.get_statistics()
        if not stats:
            print("Statistika olinmadi!")
            return
        
        freq = self.get_word_frequency(50)
        
        data = {
            "statistics": stats,
            "top_words": freq
        }
        
        with open(output_file, 'w', encoding='utf-8') as f:
            json.dump(data, f, ensure_ascii=False, indent=2)
        
        print(f"✅ Statistika {output_file} fayliga saqlandi")

# ============ ASOSIY DASTUR ============
if __name__ == "__main__":
    print("="*50)
    print("O'ZBEK TILI KORPUS YARATISH VA TAHLIL QILISH")
    print("="*50)
    
    # Korpus hajmini tanlash
    print("\nQanday hajmdagi korpus yaratmoqchisiz?")
    print("1. Kichik (10,000 so'z) - tez sinov")
    print("2. O'rta (100,000 so'z)")
    print("3. Katta (1,000,000 so'z) - tavsiya etilgan")
    
    choice = input("\nTanlang (1-3) [default: 3]: ").strip()
    
    if choice == "1":
        target_words = 10_000
    elif choice == "2":
        target_words = 100_000
    else:
        target_words = 1_000_000
    
    print("\n" + "="*50)
    
    # Korpus yaratish
    print(f"\n📝 KORPUS YARATILMOQDA ({target_words:,} so'z)...")
    generator = UzbekCorpusGenerator(target_words=target_words)
    generator.create_corpus("uzbek_corpus.txt")
    
    # Korpusni tahlil qilish
    print("\n" + "="*50)
    print("📊 KORPUS TAHLIL QILINMOQDA...")
    
    analyzer = CorpusAnalyzer("uzbek_corpus.txt")
    
    # Statistikani olish
    stats = analyzer.get_statistics()
    if stats:
        print("\n📈 STATISTIKA:")
        print(f"   Jami so'zlar: {stats['total_words']:,}")
        print(f"   Jami gaplar: {stats['total_sentences']:,}")
        print(f"   Unikal so'zlar: {stats['unique_words']:,}")
        print(f"   O'rtacha so'z uzunligi: {stats['average_word_length']:.2f} harf")
        print(f"   O'rtacha gap uzunligi: {stats['average_sentence_length']:.2f} so'z")
    
    # Eng ko'p ishlatilgan so'zlar
    print("\n🏆 ENG KO'P ISHLATILGAN 15 SO'Z:")
    for i, (word, count) in enumerate(analyzer.get_word_frequency(15), 1):
        print(f"   {i:2}. {word}: {count} marta")
    
    # JSON formatda saqlash
    analyzer.export_to_json("uzbek_corpus_stats.json")
    
    print("\n" + "="*50)
    print("✅ BARCHA ISHLAR TUGALLANDI!")
    print("="*50)
    print(f"\nYaratilgan fayllar:")
    print(f"  • uzbek_corpus.txt - asosiy korpus fayli")
    print(f"  • uzbek_corpus_stats.json - statistika fayli")