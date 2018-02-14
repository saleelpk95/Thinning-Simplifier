from utils import get_image_data, padded_image, is_border_point, is_line_end_point, is_not_simple_point, get_4_adjacent_neighbours, print_image_data, is_simple_point

if __name__ == '__main__':
	image_data = get_image_data()
	image_data = padded_image(image_data)
	count = 0
	c = 0
	li =[]
	for i in range(len(image_data)):
		for j in range(len(image_data[0])):
			if i!=0 and j!=0 and i!=len(image_data)-1 and j!=len(image_data[0])-1:
				c = c+1
				if i-1==11 and image_data[i][j]==1:
					print 'yes'
				# if image_data[i][j]==1 and (is_line_end_point((i,j), image_data) or is_not_simple_point((i,j), image_data)):
				if image_data[i][j]==1 and not(is_not_simple_point((i,j), image_data)):
					count=count+1
					li.append((i-1,j-1))
	print count,c
	print li
	print is_simple_point((6,3), image_data)
	print not(is_not_simple_point((6,3), image_data))