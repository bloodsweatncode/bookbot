from stats import get_num_words, get_chars_dict, chars_dict_to_sorted_list
def get_book_text(filepath):
    with open(filepath) as f:
        return f.read()
    

def main():
    book_path = 'books/frankenstein.txt'
    book = get_book_text(book_path)
    word_count = get_num_words(book)
    chars_dict = get_chars_dict(book)
    chars_sorted_list = chars_dict_to_sorted_list(chars_dict)
    print_report(book_path, word_count, chars_sorted_list)
    

def print_report(book_path, word_count, chars_sorted_list):
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {book_path}...")
    print("----------- Word Count ----------")
    print(f"Found {word_count} total words")
    print("--------- Character Count -------")
    for item in chars_sorted_list:
        if item["character"].isalpha():
            print(f"{item["character"]}: {item["count"]}")
    print("============= END ===============")


main()