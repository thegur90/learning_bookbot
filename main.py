import sys
from stats import count_words
from stats import character_stats
from stats import sort_on
from stats import convert_big_dict_to_dict_list

def get_book_text(n):
    return n.read()


def main():

    if len(sys.argv)<2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    else:
        t = open(f"./{sys.argv[1]}")
        book = (get_book_text(t))
        word_count = count_words(book)
        word_index = character_stats(book)
        # print(f"{word_count} words found in the document")
        m = (convert_big_dict_to_dict_list(word_index))
        print("============ BOOKBOT ============")
        print(f"Analyzing book found at {sys.argv[1]}...")
        print("----------- Word Count ----------")
        print(f"Found {word_count} total words")
        print("--------- Character Count -------")

        for entry in m:
            if entry["name"].isalpha():
                print(f"{entry["name"]}: {entry["count"]}")

        print("============= END ===============")


main()