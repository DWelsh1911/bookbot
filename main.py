
import sys
from stats import get_book_text, get_num_words, get_char_dict, sort_char_dict

def main():
    input = sys.argv[1]
    text = get_book_text(input)
    num_words = get_num_words(text)
    char_dict = get_char_dict(text)
    sorted_chars = sort_char_dict(char_dict)

    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {input}...")
    print("----------- Word Count ----------")
    print(f"Found {num_words} total words")
    print("--------- Character Count -------")
    for entry in sorted_chars:
        print(f"{entry["char"]}: {entry["num"]}")
    print("============= END ===============")

if len(sys.argv) < 2:
    print("Usage: python3 main.py <path_to_book>")
    sys.exit(1)
else:
    main()