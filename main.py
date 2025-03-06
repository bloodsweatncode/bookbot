from stats import num_words

def get_book_text(filepath):
    with open(filepath) as f:
        return f.read()

def main():
    print(f"{num_words(get_book_text('books/frankenstein.txt'))} words found in the document")

main()


