from stats import get_word_count
from stats import get_book_text
from stats import get_character_counts
from stats import get_sorted_dictionary
import sys

def main():
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)

    file_path = sys.argv[1]

    print("============ BOOKBOT ============")
    file_contents = get_book_text(file_path)
    print(f"Analyzing book found at {file_path}...")

    print("----------- Word Count ----------")
    num_words = get_word_count(file_contents)
    print(f"Found {num_words} total words")
    
    print("--------- Character Count -------")

    character_counts = get_character_counts(file_contents)
    sorted_chracters = get_sorted_dictionary(character_counts)

    for count_data in sorted_chracters:
        char = count_data["char"]
        count = count_data["count"]
        if char.isalpha():
            print(f"{char}: {count}")

    print("============= END ===============")

main()