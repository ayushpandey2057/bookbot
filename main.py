import sys
from stats import *

def get_book_text(book_path):
    with open(book_path) as f:
        book_text = f.read()
    return book_text

def main():
    if len(sys.argv) < 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)

    book_path = sys.orig_argv[2]
    book_text = get_book_text(book_path)
    word_count = get_num_of_words(book_text)
    character_count = get_character_count(book_text)
   
    # print(character_count)

    char_count_list = char_dict_to_list(character_count)
    char_count_list.sort(key=sort_on, reverse=True)
    
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {book_path}")
    print("----------- Word Count ----------")
    print(f"Found {word_count} total words")
    print("--------- Character Count -------")
    for chars in char_count_list:
        if chars["char"].isalpha():
            print(f"{chars["char"]}: {chars["num"]}")
    print("============= END ===============")


main()