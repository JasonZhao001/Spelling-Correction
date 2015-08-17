from sys import argv

output_file = open(argv[1], 'r') # this is the output of the spellchecker
correction_file = open(argv[2], 'r') # this is the target correction file

correct = 0.0

#reading both files as lists of lines
lines_o = output_file.readlines()
lines_c = correction_file.readlines()

#if the files are different lengths we exit
if len(lines_o) != len(lines_c):
    print "Your files are not the same length...exiting"
    exit(1)

for line_o in lines_o:
    line_c = lines_c.pop(0).strip()
    # the corrections file may have multiple words so we split
    c_words = line_c.split(', ')
    for word in c_words: #go through each possible correction and compare to output
        # if output matches any of the target words
        if word == line_o.strip():
        	correct += 1
    
print "Accuracy is", correct/len(lines_o)
