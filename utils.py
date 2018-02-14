from graph import Graph

def get_4_adjacent_neighbours(point):
	x = point[0]
	y = point[1]
	return [(x+1,y), (x-1,y), (x,y+1), (x,y-1)]

def get_8_adjacent_neighbours(point):
	x = point[0]
	y = point[1]
	return [(x+1,y), (x-1,y), (x,y+1), (x,y-1), (x+1,y+1), (x-1,y-1), (x-1,y-1), (x+1,y-1)]

def get_sub_graph(point, image_data):
	x = point[0]
	y = point[1]
	return [[image_data[x-1][y-1],image_data[x][y-1],image_data[x+1][y-1]],[image_data[x-1][y],0,image_data[x+1][y]],[image_data[x-1][y+1],image_data[x][y+1],image_data[x+1][y+1]]]

def get_8_adjacent_black_neighbours(point, image_data):
	x = point[0]
	y = point[1]
	neighbour_list = []
	if image_data[x+1][y] != 0:
		neighbour_list.append((x+1,y))
	if image_data[x-1][y] != 0:
		neighbour_list.append((x-1,y))
	if image_data[x+1][y+1] != 0:
		neighbour_list.append((x+1,y+1))
	if image_data[x-1][y-1] != 0:
		neighbour_list.append((x-1,y-1))
	if image_data[x][y+1] != 0:
		neighbour_list.append((x,y+1))
	if image_data[x][y-1] != 0:
		neighbour_list.append((x,y-1))
	if image_data[x+1][y-1] != 0:
		neighbour_list.append((x+1,y-1))
	if image_data[x-1][y-1] != 0:
		neighbour_list.append((x-1,y-1))

	return neighbour_list

def is_not_simple_point(point, image_data):
	count = 0
	neighbour_list = get_4_adjacent_neighbours(point)
	for point in neighbour_list:
		if image_data[point[0]][point[1]] == 1 or image_data[point[0]][point[1]] == 3 or image_data[point[0]][point[1]] == 2:
			count = count + 1
	if count == 4:
		return True
	graph = get_sub_graph(point, image_data)
	row = len(graph)
	col = len(graph[0])
	 
	g= Graph(row, col, graph)
	if g.countComponents() > 1:
		# print "not simple point"
		return True
	return False

def is_simple_point(point, image_data):
	if matches_template_1(point, image_data) or matches_template_2(point, image_data) or matches_template_3(point, image_data) or matches_template_4(point, image_data):
		return True
	return False

def matches_template_1(point, image_data):
	if image_data[point[0]-1][point[1]-1] != 0:
		if image_data[point[0]-1][point[1]+1] == 0 and image_data[point[0]+1][point[1]+1] == 0 and image_data[point[0]+1][point[1]-1] == 0:
			return True

	if image_data[point[0]-1][point[1]+1] != 0:
		if image_data[point[0]-1][point[1]-1] == 0 and image_data[point[0]+1][point[1]+1] == 0 and image_data[point[0]+1][point[1]-1] == 0:
			return True

	if image_data[point[0]+1][point[1]-1] != 0:
		if image_data[point[0]-1][point[1]+1] == 0 and image_data[point[0]+1][point[1]+1] == 0 and image_data[point[0]-1][point[1]-1] == 0:
			return True

	if image_data[point[0]+1][point[1]+1] != 0:
		if image_data[point[0]-1][point[1]+1] == 0 and image_data[point[0]-1][point[1]-1] == 0 and image_data[point[0]+1][point[1]-1] == 0:
			return True

	return False

def matches_template_2(point, image_data):
	if image_data[point[0]][point[1]-1] != 0:
		if image_data[point[0]-1][point[1]] == 0 and image_data[point[0]-1][point[1]+1] == 0 and image_data[point[0]][point[1]+1] == 0 and image_data[point[0]+1][point[1]+1] == 0 and image_data[point[0]+1][point[1]] == 0:
			return True

	if image_data[point[0]-1][point[1]] != 0:
		if image_data[point[0]][point[1]+1] == 0 and image_data[point[0]][point[1]-1] == 0 and image_data[point[0]+1][point[1]] == 0 and image_data[point[0]+1][point[1]+1] == 0 and image_data[point[0]+1][point[1]-1] == 0:
			return True

	if image_data[point[0]][point[1]+1] != 0:
		if image_data[point[0]-1][point[1]] == 0 and image_data[point[0]+1][point[1]] == 0 and image_data[point[0]][point[1]-1] == 0 and image_data[point[0]-1][point[1]-1] == 0 and image_data[point[0]+1][point[1]-1] == 0:
			return True

	if image_data[point[0]+1][point[1]] != 0:
		if image_data[point[0]][point[1]+1] == 0 and image_data[point[0]][point[1]-1] == 0 and image_data[point[0]-1][point[1]] == 0 and image_data[point[0]-1][point[1]+1] == 0 and image_data[point[0]-1][point[1]-1] == 0:
			return True

	return False

def matches_template_3(point, image_data):
	if image_data[point[0]-1][point[1]] != 0 and image_data[point[0]][point[1]-1] != 0:
		if image_data[point[0]][point[1]+1] == 0 and image_data[point[0]+1][point[1]+1] == 0 and image_data[point[0]+1][point[1]] == 0:
			return True

	if image_data[point[0]-1][point[1]] != 0 and image_data[point[0]][point[1]+1] != 0:
		if image_data[point[0]][point[1]-1] == 0 and image_data[point[0]+1][point[1]-1] == 0 and image_data[point[0]+1][point[1]] == 0:
			return True

	if image_data[point[0]+1][point[1]] != 0 and image_data[point[0]][point[1]-1] != 0:
		if image_data[point[0]-1][point[1]] == 0 and image_data[point[0]][point[1]+1] == 0 and image_data[point[0]-1][point[1]+1] == 0:
			return True

	if image_data[point[0]+1][point[1]] != 0 and image_data[point[0]][point[1]+1] != 0:
		if image_data[point[0]-1][point[1]] == 0 and image_data[point[0]-1][point[1]-1] == 0 and image_data[point[0]][point[1]-1] == 0:
			return True

	return False

def matches_template_4(point, image_data):
	neighbour_list = get_4_adjacent_neighbours(point)
	count = 0
	for neighbour in neighbour_list:
		if image_data[neighbour[0]][neighbour[1]] != 0:
			count = count+1
	if count == 3:
		return True
	return False

def is_line_end_point(point, image_data):
	x = point[0]
	y = point[1]
	count = 0
	if image_data[x+1][y] == 0:
		count = count + 1
	if image_data[x-1][y] == 0:
		count = count + 1
	if image_data[x+1][y+1] == 0:
		count = count + 1
	if image_data[x-1][y-1] == 0:
		count = count + 1
	if image_data[x][y+1] == 0:
		count = count + 1
	if image_data[x][y-1] == 0:
		count = count + 1
	if image_data[x+1][y-1] == 0:
		count = count + 1
	if image_data[x-1][y+1] == 0:
		count = count + 1

	if count == 7:
		# print "is line endpoint"
		return True
	return False

def is_border_point(point, image_data):
	x = point[0]
	y = point[1]
	if not(image_data[x+1][y] == 1 and image_data[x-1][y] == 1 and image_data[x][y+1] == 1 and image_data[x][y-1] == 1):
		return True
	return False
def padded_image(image_data):
	# print "image_data in padding",image_data
	for row in image_data:
		row.insert(0,0)
		row.append(0)
	image_data.insert(0,[0]*len(image_data[0]))
	image_data.append([0]*len(image_data[0]))
	# print image_data
	return image_data

def print_image_data(image_data, filename):
	file = open(filename+'.py', 'w+')
	for row in image_data:
		file.write('\n') 
		file.write(str(row)) 

def get_image_data():
	image_data = [
['000000000000000'],
['011000001010010'],
['011100010001100'],
['001110100010000'],
['000111111111100'],
['011111000111110'],
['000111100011100'],
['011111110111100'],
['011011101111100'],
['010001100111010'],
['010010100010010'],
['000100100001000'],
['000000000000000']
]

	converted_image = []
	for row in image_data:
		print row
		row = list(str(row[0]))
		# print row
		for col in row:
			if col=='0':
				row[row.index(col)] = 0
			else:
				row[row.index(col)] = 1
		converted_image.append(row)

	# print image_data
	return converted_image
