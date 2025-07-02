from stats import count_words

from stats import count_characters

from stats import sort

import sys


def main():
    sys_argv()

    book_path = sys.argv[1]
    text = get_book_text(book_path)
    number_of_words = count_words(text)
    num_char = count_characters(text)
    sorted_list = sort(num_char)
    print_report(book_path, number_of_words, sorted_list)
    


def get_book_text(bookpath):
    with open(bookpath) as f:
        return f.read()

def print_report(book_path, number_of_words, sorted_list):
    print ("============ BOOKBOT ============")
    print (f"Analyzing book found at {book_path}...")
    print ("----------- Word Count ----------")
    print (f"Found {number_of_words} total words")
    print ("--------- Character Count -------")

    for c in sorted_list:
        char = c['char']
        count = c['count']
        if char.isalpha():
            print (f"{char}: {count}")

    print ("============= END ===============")

def sys_argv():
    if len(sys.argv) != 2:
        print ("Usage: python3 main.py <path_to_book>")
        sys.exit(1)

main()