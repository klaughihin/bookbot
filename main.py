import sys
import stats


def get_book_text(book_file):
    book_contents = ""

    with open(book_file) as bf:
        book_contents = bf.read()

    return book_contents


if len(sys.argv) < 2:
    print("Usage: python3 main.py <path_to_book>")
    sys.exit(1)

book_loc = sys.argv[1]
book_str = get_book_text(book_loc)
book_word_count = stats.get_num_words(book_str)
book_char_count = stats.count_characters(book_str)
book_chars_ordered = stats.sort_char_counts(book_char_count)
print("============ BOOKBOT ============")
print(f"Analyzing book found at {book_loc}...")
print("----------- Word Count ----------")
print(f"Found {book_word_count} total words")
print("--------- Character Count -------")
# pprint.pprint(book_chars_ordered)
for char_dict in book_chars_ordered:
    print(f"{char_dict['char']}: {char_dict['num']}")
print("============= END ===============")
