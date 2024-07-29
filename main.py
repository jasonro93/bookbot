def main():
    # Pulls and reads book
    with open("books/frankenstein.txt") as f: # Opens the book and treats it as a file
        file_contents = f.read() # Reads the file and converts it into a string
    word_count(file_contents)

def word_count(text):
    # Counts words in text
    words = text.split()
    print(len(words)) # Print word count
    character_count(text) # Call character count
    return len(words)

def character_count(text): 
    # Counts characters
    text = text.lower() # Lowercases the text
    character_count = {} # Empty list

    for char in text: # iterating through every value in the text string
        if char in character_count: 
            character_count[char] += 1 # if this character (key) already appears in the dictionary, increment the value by 1
        else:
            character_count[char] = 1 # otherwise, set the value to 1 and add the key to the dictionary
    print(character_count)
    return character_count
    

main()