def find_longest_word(text):
    words = text.split()
    if not words:
        return None, 0
    longest = max(words, key=len)
    return longest, len(longest)
