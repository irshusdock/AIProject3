"irshusdock & arkessler"
"Ian Shusdock & Alexi Kessler"
import argparse

"Generate the value for the first feature"
"line is the board to use to generate the feature"
"This feature is which player has a piece in the bottom left corner of the board"
def generate_feature_1(line):
	return line[0]

"Generate the value for the second feature"
"line is the board to use to generate the feature"
"This feature is which player has more pieces in the center three columns"
def generate_feature_2(line):
	board_sum = 0

	"Add the number of player1s pieces in the central 3 rows and subtract the number of player2s pieces"
	for x in range(12,30):
		if(line[x] == 1):
			board_sum = board_sum + 1
		if(line[x] == 2):
			board_sum = board_sum - 1

	"Positive board_sum means player 1 has more pieces, negative means player2, 0 means same number"
	if(board_sum > 0):
		return 1
	if(board_sum < 0):
		return 2
	return 0

def generate_feature_3(line):
	return 0

def generate_feature_4(line):
	return 0

def generate_feature_5(line):
	return 0

"Main script for the program"
def feature_generator_main():
	
	"Start processing input"
	parser = argparse.ArgumentParser()
	parser.add_argument("input_file_name", help="The input file name")
	parser.add_argument("output_file_name", help="The output file name")
	args = parser.parse_args()

	"Read the input lines"
	with open(args.input_file_name) as f:
		file_content = f.readlines()

	"Remove the first line of the file to be added on later"
	first_line = file_content[0]	
	file_content = file_content[1:]

	"Generate features for each board and generate the corresponding output lines"
	new_file_content = []
	for line in file_content:
		"Remove the new line character"
		new_line = line.replace("\n","")
		feature1 = generate_feature_1(new_line)
		feature2 = generate_feature_2(new_line)
		feature3 = generate_feature_3(new_line)
		feature4 = generate_feature_4(new_line)
		feature5 = generate_feature_5(new_line)
		new_line = new_line + "," + feature1 + "," + feature2 + "," + feature3 + "," + feature4 + "," + feature5 + "\n"
		new_file_content.append(new_line)

	"Write to the output file"
	output_file = open(args.output_file_name, "w")
	
	for line in new_file_content:
		output_file.write(line)

	output_file.close()

