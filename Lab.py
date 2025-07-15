# Chris Smith
# Chapter 12   Lab 2
# 7/10/2025

import os

# Counts the number of unique words in the file
def count_unique_words(filename):
    unique_words = set()

    # Open the file and read line by line
    with open(filename, 'r') as file:
        for line in file:
            words = line.split()
            for word in words:
                # Remove punctuation and convert to lowercase
                cleaned_word = word.strip(".,!?;:()[]\"").lower()
                if cleaned_word:
                    unique_words.add(cleaned_word)

    # Return number of unique words
    return len(unique_words)

# Main program loop
def main():
    print("Unique Word Counter\n")

    while True:
        filename = input("Enter the name of the file you wish to process or type exit to quit: ")

        if filename.lower() == "exit":
            break

        # Check if the file exists
        if os.path.isfile(filename):
            num_unique = count_unique_words(filename)
            print(f"There are {num_unique} unique words in {filename}.\n")
            break
        else:
            print(f"The file {filename} could not be found!\n")

    print("Thanks for using the program!")

main()

