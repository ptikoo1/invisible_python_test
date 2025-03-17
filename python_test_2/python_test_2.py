import string
from collections import Counter

def word_frequency_counter(text):
    """
    Counts the frequency of each word in a string of text and 
    displays the words in descending order of their frequency.

    Args:
        text: The input string of text.
    """

    # 1. Clean and Tokenize the text
    text = text.lower()  # Convert to lowercase
    text = text.translate(str.maketrans('', '', string.punctuation))  # Remove punctuation
    words = text.split()  # Split the text into words

    # 2. Count word frequencies
    word_counts = Counter(words)  # Count the frequency of each word

    # 3. Sort words by frequency (descending order)
    sorted_word_counts = word_counts.most_common()

    # 4. Display the word frequencies
    print("Word Frequencies:")
    for word, count in sorted_word_counts:
        print(f"{word}: {count}")
