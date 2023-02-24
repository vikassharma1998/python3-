import pandas as pd

all_data = pd.read_csv('nato_phonetic_alphabet.csv')

dict = {row.letter: row.code for (index, row) in all_data.iterrows()}


def generate_phonetic():
    user_input = input("Enter your Word:").upper()
    try:
        result = [dict[letter] for letter in user_input]
    except:
        print('sorry ,only letters in the alphabet please')
        generate_phonetic()
    else:
        print(result)

generate_phonetic()