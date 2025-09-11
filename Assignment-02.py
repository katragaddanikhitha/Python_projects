
'''
CSCI6651 Introduction to Python Programming
Student Id: 00983208
Student Name: Katragadda Nikhitha
Git Repository: https://github.com/katragaddanikhitha/Python_projects
- User enters a string.
- If it has non-letters, program prints "Good Bye!" and stops.
- If only letters, program shows all possible combinations.
- Also checks which ones could be "possible words".

 '''


# import the itertools module for permutations function
import itertools 

# defined a function to check user input is alpha or not

def is_alpha_(string_input):
    return string_input.isalpha()

# used permutations function from itertools module to get all the permutations of given string

def string_permutations(combinations_input):

# created a new variable perm to store the permutations object

    perm = itertools.permutations(combinations_input)

#converted the permutations object to a list of strings with a new list variable perm_list

    perm_list = [''.join(p) for p in perm]
    
    return perm_list

'''defined a function to check if there is any possible word in the permutations list

A word usually has a vowel between two consonants, so any permutation that follows this can be a possible word.
'''
def any_possible_word(possible_words):

    vowels = "aeiou"
    for i in range(len(possible_words) - 2):
        if (possible_words[i] not in vowels and
            possible_words[i+1] in vowels and
            possible_words[i+2] not in vowels):
            return True
    return False

# defined main function to take input n call functions. 

def main():

# user input

    user_input = input("Enter a string: ")

# checked if the user input is alpha or not

    if not is_alpha_(user_input):
        print("Good Bye!")
        return

#called string_permutations function to get all the permutations from input

    permutations_list = string_permutations(user_input)

    print("Possible Combinations are: " ", ", permutations_list)

#created list to store the possible words from permutations list 

    words = []

    ''' created a loop to check each permutation in the permutations list 
        If any word matches the defined rule, it will be stored in the word list
    '''

    for perm in permutations_list:

        if any_possible_word(perm):

                words.append(perm)

    ''' used If Else condition to print word list if it has any possible words'''

    if words:
        print("Possible words are: ", words)
    else:
        print("No possible words found.")


main()