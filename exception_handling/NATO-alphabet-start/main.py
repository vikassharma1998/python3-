import pandas as pd



all_data = pd.read_csv('nato_phonetic_alphabet.csv')



# Keyword Method with iterrows()
dictionary = {row.letter: row.code for (index, row) in all_data.iterrows()}

#TODO 1. Create a dictionary in this format:

#TODO 2. Create a list of the phonetic code words from a word that the user inputs.
user_input = input("Enter your Words: ").upper()
result = [dictionary[word] for word in user_input]
print(result)


