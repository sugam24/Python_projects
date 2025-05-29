import pandas

data = pandas.read_csv("nato_phonetic_alphabet.csv")

phonetic_dict = {row.letter: row.code for (index, row) in data.iterrows()}


def generate_phonetic():
    word = input("Enter a word.").upper()
    try:
        output_list = [phonetic_dict[letter] for letter in word]
    except KeyError:
        print("Please enter valid alphabet key to get corresponding phonetic alphabet.")
        generate_phonetic()
    else:
        print(output_list)


generate_phonetic()
