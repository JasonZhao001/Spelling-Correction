from edit_dist import distance
from random import choice


def correct_spelling():
	"""Corrects misspellings in the source file"""

	source_file = open('misspellings.txt', 'r')
	# iterate thru source & target words
	for line in source_file:
		source_word = line.rstrip()
		min_dist = len(source_word) * 2
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

		print choice(optimal_words)

if __name__ == '__main__':
	correct_spelling()