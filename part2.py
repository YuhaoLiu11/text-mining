import random
import string
from unicodedata import category

def process_file(filename, skip_header):
    """Makes a histogram that contains the words from a file. """
    hist = {}
    fp = open(filename, encoding='UTF-8')

    if skip_header:
        for line in fp:
            if line.startswith("*** START OF THE PROJECT"):
                break

    strippables = string.punctuation + string.whitespace

    for line in fp:
        if line.startswith('*** END OF THIS PROJECT'):
            break

        for word in line.split():
            word = word.strip(strippables)
            word = word.lower()

            hist[word] = hist.get(word, 0) + 1
    return hist

def total_words(hist):
    """Returns the total of the frequencies in a histogram."""
    return sum(hist.values())

def different_words(hist):
    """Returns the number of different words in a histogram."""
    return len(hist)

def most_common(hist, excluding_stopwords=True):
    """Makes a list of word-freq pairs(tuples) in descending order of frequency.
    """
    d = []

    stopwords = process_file('data/stopwords.txt', False)

    stopwords = list(stopwords.keys())

    for word, freq in hist.items():
        if excluding_stopwords:
            if word in stopwords:
                continue

        d.append((freq, word))

    d.sort(reverse=True)
    return d

def print_most_common(hist, num=10):
    """Prints the most commons words in a histgram and their frequencies.
    hist: histogram (map from word to frequency)
    num: number of words to print
    """
    t = most_common(hist)
    print('The most common words are:')
    for freq, word in t[:num]:
        print(word, '\t', freq) 

def subtract(d1, d2):
    """Returns a dictionary with all keys that appear in d1 but not d2.
    d1, d2: dictionaries
    """
    result = {}
    for key in d1:
        if key not in d2:
            result[key] = None
    return result

def random_word(hist):
    """Chooses a random word from a histogram.
    The probability of each word is proportional to its frequency.
    """
    t = []
    for word, freq in hist.items():
        t.extend([word] * freq)

    return random.choice(t)

def main():
    hist = process_file('data/tgg1.txt', skip_header=True)
    print('Total number of words:', total_words(hist)) 
    print('Number of different words:', different_words(hist))

    t = most_common(hist, False)

    print('The most common words are:')
    for freq, word in t[0:20]:
        print(word, '\t', freq)
    print_most_common(hist, 10)

    words = process_file('data/word.txt', skip_header=False)

    diff = subtract(hist, words)
    print(f"The words in the book that aren't in the word list are: ")
    for word in diff.keys():
        print(word, end=' ')

    print(f"\n\nHere are some random words from the book ")
    for i in range(100):
        print(random_word(hist), end=' ')


if __name__ == '__main__':
    main()