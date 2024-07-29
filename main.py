def main():
    path = ("books/frankenstein.txt")
    text = get_book_path(path)
    num_words = get_num_words(text)
    num_char = get_num_char(text)
    print(num_words, num_char)


def get_book_path(book):
    with open(book) as f:
        text = f.read()
    return text


def get_num_words(book):
    words = book.split()
    return len(words)


def get_num_char(book):
    char_count = {}

    book = book.lower()
    
    for char in book:
        if char in char_count:
            char_count[char] += 1
        else:
            char_count[char] = 1
    return char_count






main()