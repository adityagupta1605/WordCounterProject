from count_words import count_words
from find_longest import find_longest_word

try:
    with open("sample.txt", "r") as f:
        content = f.read()
    total = count_words(content)
    longest, length = find_longest_word(content)
    print("📘 WORD COUNTER RESULTS 📘")
    print("----------------------------")
    print(f"Total words: {total}")
    print(f"Longest word: {longest} ({length} letters)")
    print("----------------------------")
except FileNotFoundError:
    print("❌ sample.txt not found")
