
#Return contents of book into a string
def get_book_text(filepath):
    with open(filepath) as f:
        return f.read()

#Counts number of words
def get_num_words(text):
    num_words = text.split()
    return len(num_words)

#Counts the instances of each letter as lowercase
def get_char_dict(text):
    char_dict = {}
    for letters in text:
        char = letters.lower()
        if char not in char_dict:
            char_dict[char] = 1
        else:
            char_dict[char] += 1
    return char_dict

#Sort alphanumeric characters by count
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

