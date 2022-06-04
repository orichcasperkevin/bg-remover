# example.
import sys
import os
from rembg import remove
from PIL import Image

def remove_bg(path):
	input_path = path
	basename = os.path.basename(input_path)
	new_name = basename.split('.')[0] + '_bg-removed.png'
	output_path = new_name

	input = Image.open(input_path)
	output = remove(input)
	output = output.convert('RGBA')
	output.save(output_path)
	# the end
