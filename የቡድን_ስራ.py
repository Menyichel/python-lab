import string

def ስርአት_ነጥብ_ማስወገጃ(ፋይል):
    # Remove all punctuation from the text
    ፋይል = ፋይል.translate(ፋይል.maketrans("", "", string.punctuation))
    return ፋይል
    
def ቃሎች_መዘርዘሪያ(ፋይል):
    # Compute identification of words and display them
    ዲ = {}
    for ቃል in ፋይል.split():
        if ቃል in ዲ:
           ዲ[ቃል] += 1
        else:
           ዲ[ቃል] = 1
    for key in list(ዲ.keys()):
        print(key, end=",")
        
# find word frequency and display in decreasing order
def wordOccurence(text):
    word_counts = {}
    for word in text.split():
        if word in word_counts:
            word_counts[word] += 1
        else:
            word_counts[word] = 1
    sorted_words = sorted(word_counts.items(), key=lambda x: x[1], reverse=True)
    for word, count in sorted_words:
        print(f"{word}: {count}")

# Compute character frequency and display the first five most frequently occured characters
def characterOccurence(text):
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

def ዋና():
    # Read the text file
    with open("text.txt", "r", encoding='utf-8') as ፋ:
        ፋይል = ፋ.read()
    ፋይል = ስርአት_ነጥብ_ማስወገጃ(ፋይል)

    # Output statistical information
    መስመር = ፋይል.split("\n")
    ቃላት = ፋይል.split()

    # Compute word word identified
    print("\nየዚህ ፋይል ቃላት:")
    ቃሎች_መዘርዘሪያ(ፋይል)

    # Compute word frequency
    print("\n\nየቃላት ድግግሞሽ:")
    ቃላት_ድግግሞሽ_መቁጠሪያ(ፋይል)

    # Compute character frequency
    print("\nየሆሄያት ድግግሞሽ:")
    የፊደላት_ድግግሞሽ_መቁጠሪያ(ፋይል)

    # Statstical data
    print(f"\nየዚህ ፋይል የመስመር ብዛት: {len(መስመር)}")
    print(f"የዚህ ፋይል የቃላት ብዛት: {len(ቃላት)}")
    print(f"የዚህ ፋይል የሆሄያት ብዛት: {len(ፋይል)}\n")

ዋና()