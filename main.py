import sys
from stats import num_words, sorted_char_count

def get_book_text(file_path):
    with open(file_path, encoding="utf-8") as file:
        return file.read()


def main():
    if len(sys.argv) < 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    book_path = sys.argv[1]
    book_text = get_book_text(book_path)

    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {book_path}...")
    print("----------- Word Count ----------")
    print(f"Found {num_words(book_text)} total words")
    print("--------- Character Count -------")
    for char, count in sorted_char_count(book_text):
        print(f"{char}: {count}")
    print("============= END ===============")
    
main()
