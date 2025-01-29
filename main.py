def count_characters():
    # Create dictionary,  
    character_counter = {}

    # Add alphabet list,
    alphabet = [chr(i) for i in range(97,123)]
    
    # Set letters to dict key
    for i in alphabet:
        character_counter[i] = 0
    
    # Add counter for whitespace
    # character_counter[" "] = 0
    
    # Book Selection
    with open("books/frankenstein.txt") as f:
        # Convert to lowercase letters.
        file_contents = f.read().lower()
        for character in file_contents:
            if character in character_counter:
                character_counter[character] +=1
    return character_counter
            
def sort_order():
    char_counts = count_characters()

    sorted_characters = sorted(char_counts.items(), key=lambda item: item[1], reverse=True)

    for char, count in sorted_characters:
        print(f"The '{char}' character was found {count} times")
 

def word_count():
    with open("books/frankenstein.txt") as f:
        file_contents = f.read()
        words = len(file_contents.split())
        print(f"{words} words found in the document")

def main():
    print("--- Begin report of books/frankenstein.txt ---")
    word_count()
    sort_order()
    print("--- End report ---")


main()