import numpy as np
import matplotlib.pyplot as plt
from scipy.misc import imread, imsave
from PIL import Image 
from utils import get_image_data, padded_image, is_border_point, is_line_end_point, is_not_simple_point, get_4_adjacent_neighbours, print_image_data, is_simple_point

if __name__ == '__main__':
	image_data = get_image_data()
	image_data = padded_image(image_data)
	print image_data
	# print "length of image_data \n", len(image_data)," * ",len(image_data[0])

	border_list = [(ind,i) for ind,row in enumerate(image_data) for i,col in enumerate(row) if col == 1 and ind != 0 and i != 0 and ind != len(image_data)-1 and i != len(image_data[0])-1]
	print border_list
	border_list = [point for point in border_list if is_border_point(point,image_data)]
	for border_point in border_list:
		image_data[border_point[0]][border_point[1]] = 2

	num_deleted_points = -1
	print_image_data(image_data, "image_data")
	i=0
	while num_deleted_points != 0:
		num_deleted_points = 0
		# print "entered. ",num_deleted_points
		temp_border_list = list(border_list)
		for border_point in border_list:
			# print i
			if is_line_end_point(border_point, image_data) or not(is_simple_point(border_point, image_data)):
				# print "skeleton point",border_point
				image_data[border_point[0]][border_point[1]] = 3
				temp_border_list.remove(border_point)
				# print_image_data(image_data,"elements of skeleton"+str(i))
			elif is_simple_point(border_point, image_data):
				# print "simple point",border_point
				image_data[border_point[0]][border_point[1]] = 0
				temp_border_list.remove(border_point)
				num_deleted_points = num_deleted_points + 1
				adjacent_points = get_4_adjacent_neighbours(border_point)
				for point in adjacent_points:
					if image_data[point[0]][point[1]] == 1:
						image_data[point[0]][point[1]] = 2
						temp_border_list.append(point)
		border_list = list(temp_border_list)
		print_image_data(image_data,"delete and update"+str(i))
		i=i+1
		# print "leaving. ",num_deleted_points
		# print "image_data \n",image_data
	# print image_data
