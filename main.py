def main():
    book_path = "books/frankenstein.txt"
    
    print (f"--- Begin report of {book_path} ---")

    book_text = get_book_text(book_path)
    words = count_words(book_text)
    
    print (f"There were {words} words found in this document")
    print("")
    
    letters = count_letters(book_text)
    letter_report(letters)
    
    print("--- End report ---")
    

def get_book_text(path):
    with open(path) as contents:
        return contents.read()


def count_words(text):
    words = text.split()
    word_count = 0
    for word in words:
        word_count += 1
    return word_count


def count_letters(text):
    uniform_text = text.lower()
    letter_counts = {}
    for letters in uniform_text:
        if letters.isalpha():
            if letters in letter_counts:
                letter_counts[letters] += 1
            else:
                letter_counts[letters] = 1
        else:
            pass
    return letter_counts

def letter_report(letter_tuple_list):
    letters_list = list(letter_tuple_list.items())
    letters_list.sort(key=lambda a:a[1], reverse=True)
    for i in letters_list:
        print(f"The {i[0]} character was found {i[1]} times")


main()