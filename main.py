import sys
from stats import count_words, count_characters, dict_to_sorted_list, sort_by_count

def get_book_text(file):
    with open(file) as f:
        return f.read()



def main(path):
    if len(path) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    text = get_book_text(path[1])
    total_words = count_words(text)
    character_counts = count_characters(text)
    sorted_character_counts = dict_to_sorted_list(character_counts)
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {path[1]}...")
    print("----------- Word Count ----------")
    print("Found 75767 total words")
    print("--------- Character Count -------")
    for i in sorted_character_counts:
        if i["letter"].isalpha():
            print(f"{i["letter"]}: {i["count"]}")
    print("============= END ===============")

main(sys.argv)