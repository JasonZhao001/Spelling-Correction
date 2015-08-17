
##############################################################
# Helper functions

def ins_cost(letter):
	if letter == 'e':
		return 0
	else:
	    return 1

def sub_cost(letter1, letter2):
    if letter1 == letter2:
        return 0
    else:
        return 2

def del_cost(letter):
    return 1

##############################################################
# Calculating Edit Distance

def distance(source, target):
	"""Returns the minimum edit distance between two strings

	>>> distance('string', 'strung')
	2

	>>> distance('string', 'strin')
	1

	>>> distance('string', 'strings')
	1

	"""

	n = len(target)
	m = len(source)

	distance_table = [[0 for x in range(n+1)] for x in range(m+1)]
	distance_table[0][0] = 0

	for i in range(1, m+1):
		distance_table[i][0] = distance_table[i-1][0] + ins_cost(source[i-1])

	for j in range(1, n+1):
		distance_table[0][j] = distance_table[0][j-1] + del_cost(target[j-1])

	for i in range(1, m+1):
		for j in range(1, n+1):
			distance_table[i][j] = min(distance_table[i-1][j] + ins_cost(source[i-1]),
									   distance_table[i-1][j-1] + sub_cost(target[j-1], source[i-1]),
									   distance_table[i][j-1] + del_cost(target[j-1]))

	distance = distance_table[m][n]

	return distance