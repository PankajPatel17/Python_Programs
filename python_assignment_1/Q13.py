str = input("Enter a sentence: ")

str = str.lower()

translator = str.maketrans('', '', string.punctuation)
clean_sentence = sentence.translate(translator)

#
words = clean_sentence.split()

# Create a dictionary to store word counts
word_count = {}

# Count occurrences of each word
for word in words:
    if word in word_count:
        word_count[word] += 1
    else:
        word_count[word] = 1

# Print the word occurrences in a simple format
for word, count in word_count.items():
    print(f"{word}: {count}")
