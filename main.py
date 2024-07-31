def get_book_path(book): # Open and read file
    with open(book) as f:
        text = f.read()
    return text

path = ("books/frankenstein.txt")
text = get_book_path(path)

def main():

    num_words = get_num_words(text)
    num_char = get_num_char(text)
    report = get_report(num_char)
    print(report)


def get_num_words(book): # Word count
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


def get_report(book):
    char_list = list(book.items()) # Convert to list of tuples
    char_list.sort(reverse=True, key=lambda item: item[1]) # Sort tuples based on index 1

    split_char = [{k:v} for k, v in char_list] # Convert back to list of dictionaries

    book_length = get_num_words(text)

    print("--- Begin report of books/frankenstein.txt ---")
    print(f"'{book_length}' words found in the document")
    print()

    for char_dict in split_char: # Iterate through the key of each dictionary, reporting the value if the key is alphabetical
        for key in char_dict:
            if key.isalpha():
                char_count = char_dict[key]
                print(f"The '{key}' character was found {char_count} times.")

    return "--- End report ---"
   
    


main()