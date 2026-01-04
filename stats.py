def num_words(text):
    words = text.split()
    return len(words)


def char_count(text):
    text = text.lower()
    char_dict = {}
    for char in text:
        if not char.isalpha():
            continue
        if char in char_dict:
            char_dict[char] += 1
        else:
            char_dict[char] = 1
    return char_dict

def sorted_char_count(text):
    char_dict = char_count(text)
    return sorted(char_dict.items(), key=lambda item: item[1], reverse=True)
