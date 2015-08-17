from flask import Flask, render_template, request
from spelling_correction import *

app = Flask(__name__)

@app.route('/')
def home():
	"""Displays the main page"""

	return render_template('home.html')


@app.route('/', methods=['POST'])
def get_corrected_text():
	"""Returns the corrected sentence"""

	sentence = request.form.get('sentence').lower()
	sentence = sentence.split()
	correct_sentence = []

	for word in sentence:
		correction = find_match(word)
		correct_sentence.append(correction)

	correct_sentence = ' '.join(correct_sentence)
	correct_sentence = correct_sentence.capitalize() + '!'
	return correct_sentence




if __name__ == '__main__':
	app.run(debug=True)