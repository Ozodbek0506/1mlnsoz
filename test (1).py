import random
def create_test_corpus(num_words=10000):
    """Kichik test korpusi yaratish"""
    words = [
        "salom", "dunyo", "o'zbek", "python", "dastur", "korpus",
        "til", "ma'lumot", "tahlil", "sun'iy", "intellekt"
    ]
    
    templates = [
        "{} {} {}.",
        "Bugun {} {}.",
        "{} va {} {}.",
        "Men {} {} ni {}."
    ]
    
    with open("test_corpus.txt", 'w', encoding='utf-8') as f:
        total = 0
        while total < num_words:
            template = random.choice(templates)
            words_needed = template.count("{}")
            selected = [random.choice(words) for _ in range(words_needed)]
            sentence = template.format(*selected)
            
            f.write(sentence + "\n")
            total += len(sentence.split())
            
            if total % 1000 == 0:
                print(f"{total} so'z yaratildi...")
    
    print(f"✅ Test korpus yaratildi: {total} so'z")

# Tez sinov uchun
if __name__ == "__main__":
    # Kichik test korpusi (10,000 so'z)
    create_test_corpus(10000)