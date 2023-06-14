
###########################################################

#  Computer Project #09
#
#
#
#  Algorithm
#           This program imports the string module and uses dictionaries and sets. 
#           The program uses 4 functions and 1 main function. 
#           The docstrings for the various functions have been included in the functions.
#           The Functions:
#                         1. Open_file()
#                         2. Read_file()
#                         3. fill_completions()
#                         4. find_completions()
#           The main function:
#                1. calls the open file function to receive the file pointer 
#                2. calls the read file function and pass on the file pointer as argument and returns a set of words. 
#                3. calls the fill completions function and pass on the set of words as argument and returns a dictionary of words
#                4. Repeatedly ask the user for a prefix:
#                           a) if prefix == "#", program prints a goodbye message and quits. 
#                           b) for any other prefix given:
#                                   1. Program calls the find completions function and pass on the prefix and dictionary of words as 
#                                       arguments. 
#                                   2. if no words are found, print a message
#                                   3. if words are found, print the set of words that complete the prefix sorted alphabetically. 
#
#    
#
###########################################################

import string

def open_file():
    """
    This function returns a file pointer (fp) from opening a file. It uses the UTF-8 encoding for the 
    opening of the file. Displays an error message if no file is found.
    Parameters: No parameter
    returns: a file pointer
    """

    while True:
        f_name = input("\nInput a file name: ")        #Ask the user for a file 
        try:
            fp = open(f_name, "r", encoding='UTF-8')   #try opening a file, if successful return the file pointer 
            return fp
        except FileNotFoundError:
            print("\n[Error]: no such file")           #if not succesful display this message and reprompt for file. 


def read_file(fp):
    """
    This function reads a file and returns a set of words with punctuation removed and
    words containing non-alphabetic characters ignored.
    Parameters:
        fp: file pointer to read from
    Returns:
        set of words
    """
    word_set = set()          #create an empty set to store unique words 

    for line in fp:           #iterate through each line in the file 
        words = line.strip().split()
        for word in words:
            word = word.strip(string.punctuation).lower()  #remove any leading punctions 
            if len(word) > 1 and word.isalpha():           #check for words with only alphabetic characters and length greater than 1 
                word_set.add(word)

    return word_set


def fill_completions(words):
    """
    This function returns a dictionary whose keys are tuples and values sets. 
    The key of the dictionary contains a tuple of the (n, l) with n being the index position of the lowercase character l
    If the key already exists the word is added to the set values for that key.
    
    Parameters: set of words

    Returns: a dictionary 
    """

    word_D = {}                               #create an empty dictionary to store the values 
    for word in words:
        for i, ch in enumerate(word.lower()): #get the index and character of each word 
            key = (i, ch)
            if key not in word_D:
                word_D[key] = set()           #add the key to the set if it is not already in it 
            word_D[key].add(word)             #add the word to the set value if key already exists 

    return word_D


def find_completions(prefix, word_D):
    """
    This function returns a set of words in the dictionary that completes the prefix if any.
    The function returns an empty set if prefix cannot be completed to any vocabulary words.

    Parameters: str, dictionary

    Returns: set of strings
    """

    completions = set()  # initialize an empty set to store words

    #iterate through the whole length of the prefix
    for i in range(len(prefix)):
        key = (i, prefix[i])                                
        if key in word_D:
            if not completions:
                completions = set(word_D[key])  # store the set of words from the key-value pair if key not in the completions
            else:
                completions &= set(word_D[key])  # if already in, check for intersection
        else:
            return set()  # if no words are found return an empty set

    # Check if the words in completions start with prefix exactly
    completions = {word for word in completions if word.startswith(prefix)}

    return completions


def main():    
    fp = open_file()
    words = read_file(fp)
    word_D = fill_completions(words)

    while True:
        prefix = input("\nEnter a prefix (# to quit): ")   #Ask user for a prefix 
        if prefix == "#":
            print("\nBye")
            break 
        complete_words = find_completions(prefix, word_D)
        if len(complete_words) == 0:
            print("\nThere are no completions.")
        else:
            complete_words = list(complete_words)         #convert set into a list 
            output_str = ", ".join(sorted(complete_words))
            print("\nThe words that completes {} are: {}".format(prefix, output_str)) 


if __name__ == '__main__':
    main()



