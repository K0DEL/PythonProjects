import pandas

student_dict = {
    "student": ["Angela", "James", "Lily"],
    "score": [56, 76, 98]
}

# Looping through dictionaries:
for (key, value) in student_dict.items():
    # Access key and value
    pass

student_data_frame = pandas.DataFrame(student_dict)


# Loop through rows of a data frame
for (index, row) in student_data_frame.iterrows():
    # Access index and row
    # Access row.student or row.score
    pass

nato = {}
nato_data = pandas.read_csv("nato_phonetic_alphabet.csv")
for (index, row) in nato_data.iterrows():
    nato[row.letter] = row.code

is_done = True
while is_done:
    word = input("Enter The word: ").lower()
    try:
        word_list = [nato[item.upper()] for item in word]
    except KeyError:
        print("please Enter a valid Word.")
    else:
        is_done = False
        print(word_list)
# Keyword Method with iterrows()
# {new_key:new_value for (index, row) in df.iterrows()}

# TODO 1. Create a dictionary in this format:
{"A": "Alfa", "B": "Bravo"}

# TODO 2. Create a list of the phonetic code words from a word that the user inputs. # noqa: E501
