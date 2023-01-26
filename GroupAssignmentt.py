import string

def remove_punctuation(text):
    # Remove all punctuation from the text
    text = text.translate(text.maketrans("", "", string.punctuation))
    return text
def word_found(text):
    
    d = {}
    for word in text.split():
        if word in d:
           d[word] += 1
        else:
           d[word] = 1
    for key in list(d.keys()):
        print(key, end=",")

def wordOccurence(text):
    # Compute word frequency and display in decreasing order
    word_counts = {}
    for word in text.split():
        if word in word_counts:
            word_counts[word] += 1
        else:
            word_counts[word] = 1
    sorted_words = sorted(word_counts.items(), key=lambda x: x[1], reverse=True)
    for word, count in sorted_words:
        print(f"{word}: {count}")

def characterOccurence(text):
    # Compute character frequency and display the first five most frequent
    char_counts = {}
    for char in text:
        if char==" ":
            continue
        if char in char_counts:
            char_counts[char] += 1
        else:
            char_counts[char] = 1
    sorted_chars = sorted(char_counts.items(), key=lambda x: x[1], reverse=True)
    for i in range(5):
        print(f"{sorted_chars[i][0]}: {sorted_chars[i][1]}")

def mainF():
    # Read the text file
    with open("text.txt", "r", encoding='utf-8') as f:
        text = f.read()
    text = remove_punctuation(text)
    
    lines = text.split("\n")
    words = text.split()

    # Identifying words
    print("\n---------------------------------")
    print("Word found:")
    word_found(text)

    # Finding word frequency
    print("\n\nWord frequency:")
    wordOccurence(text)

    # Finding character frequency
    print("\nCharacter frequency:")
    characterOccurence(text)

    # Statstical informations
    print(f"\nTotal number of lines: {len(lines)}")
    print(f"Total number of words: {len(words)}")
    print(f"Total number of characters: {len(text)}")
    print("-----------------------------------\n")

mainF()
