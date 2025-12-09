def get_book_text(book_path):
    with open(book_path) as f:
        book_text = f.read()
    return book_text

def num_of_words(text):
    return len(text.split())


def main():
    book_path = "./books/frankenstein.txt"
    book_text = get_book_text(book_path)
    word_count = num_of_words(book_text)
    print(f"Found {word_count} total words")


main()