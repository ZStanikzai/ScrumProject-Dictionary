import json
from difflib import get_close_matches

# Loading data from json file
# in python dictionary
data = json.load(open("dictionary.json"))

def translate(word):
	# This function will convert the entered text to lower cases (Group memebers who has taken python might be familier
	#with these built in funcitons of python).
	word = word.lower()

	if word in data:
		return data[word]
	# for getting close matches of word
	elif len(get_close_matches(w, data.keys())) > 0:
		yn = input("Did you mean % s instead? Enter Y if yes, or N if no: " % get_close_matches(word, data.keys())[0])
		yn = yn.lower()
		if yn == "y":
			return data[get_close_matches(word, data.keys())[0]]
		elif yn == "n":
			return "The word doesn't exist. Please double check it."
		else:
			return "We didn't understand your entry."
	else:
		return "The word doesn't exist. Please double check it."

# Driver code
word_input = input("Enter word: ")
output = translate(word_input)

if type(output) == list:
	for item in output:
		print(item)
else:
	print(output)
input('Press ENTER to exit')
