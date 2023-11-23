import imageio
from scipy import datasets
import matplotlib.pyplot as plt
import numpy as np


def calc_samples_per_sec(signal, length_recording):
	###
	# The function has to caclulate the samples per second taken when recording the signal
	#
	# Input parameters: 
	#	signal: a 1 dimensional numpy structure with the recordings of a time series
	#		sampled at regular intervals (voice, music, electrocardiogram, etc)
	#	length_recording: The duration in seconds of the recording
	# 
	# Retruns: the number of samples per second
	###

	samples_per_sec = 0.0
	# Your code below this line



	#Your code above this line
	return samples_per_sec

def chart_signal(signal, samples_per_sec, start_second, end_second):
	###
	# The function saves a file with a plot of a signal within a specified time interval
	#
	# Input parameters: 
	#	signal: a 1 dimensional numpy structure with the recordings of a time series
	#		sampled at regular intervals (voice, music, electrocardiogram, etc)
	#	samples_per_sec: The number of samples per second taken during the recording
	#	start_second: time in seconds at which the plot should start
	#	end_second: time in seconds at which the plot should end
	# 
	# Retruns: the number of samples per second
	###

	x = [1,2,3,4,5]
	y = [1,1,1,1,1]
	# Your code below this line


	#Your code above this line
	plt.plot(x,y)
	plt.savefig('chart_signal.png')

def resize_image(img, hor_factor, ver_factor):
	###
	# The function receives an image and returns a resized version skipping as many pixels per pixel horizontally
	# as specified in hor_factor and vertically as specified in ver_factor.
	#
	# Input parameters: 
	#	img: array representing an image
	#	hor_factor: pixels to skip horizontally. If 1, there will be no horizontal resize, if 2 it will keep 1 every 2 pixels,
	#		if 3 it will keep 1 every 3 pixels, and so on... 
	#	ver_factor: pixels to skip vertically. If 1, there will be no vertical resize, if 2 it will keep 1 every 2 pixels,
	#		if 3 it will keep 1 every 3 pixels, and so on... 
	# 
	# Retruns: the resized image
	###
	rsz_img = img
	# Your code below this line


	#Your code above this line
	return rsz_img

def calculate_comp_ratio(img, comp_img):
	###
	# The function receives an image and a resized version of that image and it needs to calculate the % of storage space 
	# the resized image saves. If the two images are the same it should return 0, if the resized image occupies 90% of the 
	# storage of the first one it should return 10
	#
	# Input parameters: 
	#	img: array representing an image
	#	comp_img: array representing the resized image
	#
	# Retruns: the percentage (just the number) of space saved with the resized image
	###
	comp_ratio = 0.0
	# Your code below this line


	#Your code above this line
	return comp_ratio

def get_img_region(img, center_x, center_y, width, height):
	###
	# The function receives an image and should return a rectangular region of it. The region is specified by passing a center,
	# the total width of the region and the total height of the region.
	#
	# You cn assume the region specified will be inside the image
	#
	# Input parameters: 
	#	img: array representing an image
	#	center_x: horizontal component of the center of the region
	#	center_y: vertical component of the center of the region
	#	width: width of the region
	#	height: height of the region
	#
	# Retruns: returns the image corresponding to the specified region
	###

	img_reg = img
	# Your code below this line


	#Your code above this line
	return img_reg

def add_rectangle(img, center_x, center_y, width, height, thick, red, green, blue):
	###
	# The function receives an image and should add a rectangle to it. The recangle is specified by passing a center,
	# the total width and the total height. The color of the recangle is specified by the red, greem and blue parameters.
	# If the image is grayscale (only one channel) the rectangle should be painted in black (independently of the colors specified)
	#
	# You can ssume the specified rectangle will be within the image. The width / height specify the area inside the rectangle, the 
	# rectangle line, of whatever thickness is painted outside this area.
	#
	# Input parameters: 
	#	img: array representing an image
	#	center_x: horizontal component of the center of the rectangle
	#	center_y: vertical component of the center of the rectangle
	#	width: width of the rectangle
	#	height: height of the rectangle
	#	thick: thicness of the rectangle
	#	red: red component of the rectangle color
	#	green: green component of the rectangle color
	#	blue: blue component of the rectangle color
	#
	# Retruns: returns the image with the rectangle
	###

	img_rect = img.copy()
	# Your code below this line


	#Your code above this line
	return img_rect

def to_gray_scale_loop(img_col):
	###
	# For many ML/AI applications we do not need the 3 channels and it simplifies things a lot having a grayscale image. There are several methods to go from 
	#	RGB to gray scale as described in this link: https://www.baeldung.com/cs/convert-rgb-to-grayscale
	#	Implement a function that accepts a RGB image and returns a grayscale image. It should use the luminosity method described in the previous link.
	# 
	# This function should be implemented with loops, iterating through all the array elements.
	#
	# Input parameters:
	#	img_col: array representing an colored image
	#
	# Returns: returns the grayscale version of the input image (only one channel)
	###

	img_gray = img_col
	# Your code below this line


	#Your code above this line
	return img_gray

def to_gray_scale_vector(img_col):
	###
	# For many ML/AI applications we do not need the 3 channels and it simplifies things a lot having a grayscale image. There are several methods to go from 
	#	RGB to gray scale as described in this link: https://www.baeldung.com/cs/convert-rgb-to-grayscale
	#	Implement a function that accepts a RGB image and returns a grayscale image. It should use the luminosity method described in the previous link.
	# 
	# This function should be implemented with no loops (vectorized).
	#
	# Input parameters:
	#	img_col: array representing an colored image
	#
	# Returns: returns the grayscale version of the input image (only one channel)
	###

	img_gray = img_col
	# Your code below this line


	#Your code above this line
	return img_gray

if __name__ == '__main__':
	ecg = datasets.electrocardiogram()
	rak = datasets.face()
	### Tests ###
	print('--- Tests ---')
	print('Test calc_samples_per_sec')
	print()
	print('Samples per sec are:')
	print(calc_samples_per_sec(ecg, 300))
	print()
	print('Test chart_signal')
	chart_signal(ecg, calc_samples_per_sec(ecg, 300), 140, 142)
	print('Check file chart_signal.png saved to your drive')
	print()
	print('Test resize_image')
	imageio.v3.imwrite('resized_img.png', resize_image(rak, 10, 10))
	print('Check file resized_img.png saved to your drive')
	print()
	print('Test calculate_comp_ratio')
	print('Compression ratio is:')
	print(calculate_comp_ratio(rak, resize_image(rak, 10, 10)))
	print()
	print('Test get_img_region')
	imageio.v3.imwrite('region_img.png', get_img_region(rak, 700, 550, 250, 150))
	print('Check file region_img.png saved to your drive')
	print()
	print('Test add_rectangle')
	imageio.v3.imwrite('rect_img.png', add_rectangle(rak, 643, 315, 225, 90, 10, 255, 49, 99))
	print('Check file rect_img.png saved to your drive')
	print()
	print('Test to_gray_scale_loop')
	ig = to_gray_scale_loop(rak)
	print('Ouptut shape:')
	print(ig.shape)
	plt.imshow(ig, cmap=plt.cm.gray)
	plt.savefig('img_gray_loop.png')
	print('Check file img_gray_loop.png saved to your drive')
	print()
	print('Test to_gray_scale_loop')
	ig = to_gray_scale_vector(rak)
	print('Ouptut shape:')
	print(ig.shape)
	plt.imshow(ig, cmap=plt.cm.gray)
	plt.savefig('img_gray_vect.png')
	print('Check file img_gray_vect.png saved to your drive')


