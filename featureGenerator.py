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
	line = line.replace(",", "")
	
	board_sum = 0

	"Add the number of player1s pieces in the central 3 rows and subtract the number of player2s pieces"
	for x in range(12,30):
		if(line[x] == "1"):
			board_sum = board_sum + 1
		if(line[x] == "2"):
			board_sum = board_sum - 1

	"Positive board_sum means player 1 has more pieces, negative means player2, 0 means same number"
	if(board_sum > 0):
		return 1
	if(board_sum < 0):
		return 2
	return 0

"Generate the value for the third feature"
"line is the board to use to generate the feature"
"This feature is the number of columns that player 1 has at least one piece in"
def generate_feature_3(line):
	
	line = line.replace(",", "")

	num_cols = 0;

	for i in range(0,7):
		player_1_piece = False
		for j in range(0,6):
			if(line[(i*6+j)] == "1"):
				player_1_piece = True
		if(player_1_piece == True):
			num_cols = num_cols + 1

	return num_cols

"Generate the value for the third feature"
"line is the board to use to generate the feature"
"This feature is the total number of spaces surronding player1s pieces"
"Open spaces shared by 2 or more pieces are counted multiple times"
def generate_feature_4(line):

	line = line.replace(",", "")
	
	sum_open_spaces = 0

	for i in range(0,7):
		for j in range(0,6)

			"Ignore any pieces that aren't player1s"
			if(line[i*6+j] != "1"):
				continue

			ignore_left = (i==0)
			ignore_right = (i==6)
			ignore_up = (j==5)
			ignore_down = (j==0)

			"Check all spaces to the left"
			if(not ignore_left):
				if(line[(i-1)*6+1] == "0"):
					sum_open_spaces = sum_open_spaces + 1
				if(not ignore_up):
					if(line[(i-1)*6+2] == "0"):
						sum_open_spaces = sum_open_spaces + 1
				if(not ignore_down):
					if(line[(i-1)*6+0] == "0"):
						sum_open_spaces = sum_open_spaces + 1

			"Check all spaces to the right"
			if(not ignore_right):
				if(line[(i+1)*6+1] == "0"):
					sum_open_spaces = sum_open_spaces + 1
				if(not ignore_up):
					if(line[(i+1)*6+2] == "0"):
						sum_open_spaces = sum_open_spaces + 1
				if(not ignore_down):
					if(line[(i+1)*6+0] == "0"):
						sum_open_spaces = sum_open_spaces + 1

			"Check the space directly above"
			if(not ignore_up):
				if(line[(i)*6+2] == "0"):
					sum_open_spaces = sum_open_spaces + 1

			"Check the space directly below"
			if(not ignore_up):
				if(line[(i)*6+0] == "0"):
					sum_open_spaces = sum_open_spaces + 1

	return sum_open_spaces

"Generate the value for the third feature"
"line is the board to use to generate the feature"
"This feature is the number of pieces player 1 has along the edge of the board"
def generate_feature_5(line):
	line = line.replace(",", "")

	sum_edge_pieces = 0

	"Count the pieces on the left edge of the board, including corners"
	for x in range(0,6):
		if(line[x] == "1"):
			sum_edge_pieces = sum_edge_pieces + 1

	"Count the pieces on the right edge of the board, including corners"
	for x in range(36,42):
		if(line[x] == "1"):
			sum_edge_pieces = sum_edge_pieces + 1

	"Count the pieces on the top edge of the board, not including corners"
	for x in range(1,6):
		if(line[x*6+5] == "1"):
			sum_edge_pieces = sum_edge_pieces + 1
	"Count the pieces on the bottom edge of the board, not including corners"
	for x in range(1,6):
		if(line[x*6] == "1"):
			sum_edge_pieces = sum_edge_pieces + 1

	return sum_edge_pieces

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

