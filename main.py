def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    num_letters = get_num_letters(text)
    num_words = get_num_words(text)

    character_list = list(num_letters.items())
    character_list.sort(key=lambda x: x[1], reverse=True)

    print(f"--- Begin report of {book_path} ---")
    print(f"{num_words} words found in the document")
    for char, count in character_list:
        print(f"The '{char}' character was found {count} times")
    print("--- End Report ---")


def get_num_words(text):
    words = text.split()
    return len(words)

def get_num_letters(text):
    result = {}
    text = text.lower() # Convert the text to lowercase
    for char in text: # Iterating over the text
        if char.isalpha(): # Checking if the character is a letter
            if char in result: 
                result[char] += 1 # Increment the count if the character is already in the dictionary
            else: 
                result[char] = 1 # If the character is not in the dictionary, add it
    return result

def get_book_text(path):
    with open(path) as f:
        return f.read()


main()