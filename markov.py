"""Generate Markov text from text files."""

import random

def open_and_read_file(file_path):
    """Take file path as string; return text as string.

    Takes a string that is a file path, opens the file, and turns
    the file's contents as one string of text.
    """

    contents = open(file_path).read()

    return contents 


def make_chains(text_string):
    """Take input text as string; return dictionary of Markov chains.

    A chain will be a key that consists of a tuple of (word1, word2)
    and the value would be a list of the word(s) that follow those two
    words in the input text.

    For example:

        >>> chains = make_chains('hi there mary hi there juanita')

    Each bigram (except the last) will be a key in chains:

        >>> sorted(chains.keys())
        [('hi', 'there'), ('mary', 'hi'), ('there', 'mary')]

    Each item in chains is a list of all possible following words:

        >>> chains[('hi', 'there')]
        ['mary', 'juanita']

        >>> chains[('there','juanita')]
        [None]
    """
    words = text_string.split()
    
    chains = {}

    for i in range(len(words) - 1):
        
        chains[(words[i], words[i + 1])] = []
        
        if (i + 2) == (len(words) - 1):
            break

    for i in range(len(words) - 1):
        
        chains[(words[i], words[i + 1])].append(words[i + 2)  

        if (i + 2) == (len(words) - 1):
            break            
    
    return chains


def make_text(chains):
    """Return text from chains."""

    words = []

    current_key = random.choice(sorted(chains))

    while True:
        
        chosen_word = random.choice(chains[current_key])

        words.append(chosen_word)
    
        new_key = (current_key[1], chosen_word)

        current_key = new_key

        if current_key not in chains:
            break
    return ' '.join(words)


# Pseudocode
# first_key = random.choice(sorted(chains))
        # will give us a tuple
# since the first_key is assigned, I can index into first_key[1] and get the second word of the tuple
# new_key_first_word = first_key[1]
# chosen_word = random.choice(chains[first_key]) will give us random item from that list
# words.append(chosen_word)
# new_tuple = (new_key_first_word, chosen_word)




input_path = 'green-eggs.txt'

# Open the file and turn it into one long string
input_text = open_and_read_file(input_path)

# Get a Markov chain
chains = make_chains(input_text)

# Produce random text
random_text = make_text(chains)

print(random_text)

