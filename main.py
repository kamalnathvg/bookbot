from stats import get_num_words, count_chars, print_char_count
import sys


def get_book_text(file_path: str) -> str:
    file_contents: str = ""
    with open(file_path) as f:
        file_contents = f.read()
        f.close()
    return file_contents


def main():
    args: [str] = sys.argv
    if len(args) != 2:
        print("UsageL python3 main.py <path_to_book>")
        sys.exit(1)

    file_path: str = args[1]
    text: str = get_book_text(file_path)
    num_words: int = get_num_words(text)
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {file_path}...")
    print("----------- Word Count ----------")
    print(f"Found {num_words} total words")
    char_counts = count_chars(text)
    print_char_count(char_counts)


main()
