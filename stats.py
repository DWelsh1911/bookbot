
def get_num_words(text):
    num_words = text.split()
    return len(num_words)

# Counts the instances of each letter
def get_char_dict(text):
    char_dict = {}
    for letters in text:
        char = letters.lower()
        if char not in char_dict:
            char_dict[char] = 1
        else:
            char_dict[char] += 1
    return char_dict

def sort_on(item):
    return item["num"]

def sort_char_dict(char_dict):
    sorted_list = [
        {"char": char, "num": count}
        for char, count in char_dict.items()
        if char.isalpha()
    ]
    sorted_list.sort(reverse=True, key=sort_on)
    return sorted_list

