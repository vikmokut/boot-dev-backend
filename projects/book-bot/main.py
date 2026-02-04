from stats import word_count, get_book_text,\
    character_count_v2, report, display_report
import sys

def main():
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    filepath = sys.argv[1]
    # print(sys.argv)
    text = get_book_text(filepath)
    num_words = word_count(text)
    total_char, num_char = character_count_v2(text)
    display_report(num_char, filepath, total_char, num_words)

if __name__ == "__main__":
    main()
