import string


def mainF():
    # Read the text file
    with open("text.txt", "r", encoding='utf-8') as f:
        text = f.read()

    lines = text.split("\n")
    words = text.split()

    # Identifying words
    print("\n---------------------------------")
    print("Word found:")

    # Finding word frequency
    print("\nWord frequency:")

    # Finding character frequency
    print("\nCharacter frequency:")

    # Statstical informations
    print(f"\nTotal number of lines: {len(lines)}")
    print(f"Total number of words: {len(words)}")
    print(f"Total number of characters: {len(text)}")
    print("-----------------------------------\n")

mainF()
