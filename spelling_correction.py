from edit_dist import distance
from random import choice


def find_match(source_word):
	"""Finds the best match for a source word"""

	min_dist = 100
	# min_dist = len(source_word) * 2
	optimal_words = []

	target_file = open('dict.txt', 'r')
	for line in target_file:
		target_word = line.rstrip()

		if distance(source_word, target_word) == min_dist:
			# Add this word to the list
			optimal_words.append(target_word)

		if distance(source_word, target_word) < min_dist:
			min_dist = distance(source_word, target_word)
			# re-initialize the list, with only this word as a possible correction
			optimal_words = [target_word]

	return choice(optimal_words)



def spellcheck_file():
	"""Corrects misspellings in the source file"""

	source_file = open('misspellings.txt', 'r')
	# iterate thru source & target words
	for line in source_file:
		source_word = line.rstrip()
		print find_match(source_word)



if __name__ == '__main__':
	spellcheck_file()