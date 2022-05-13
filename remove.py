# example.
import sys
import os
from rembg import remove
from PIL import Image

path = sys.argv[1]

input_path = path
basename = os.path.basename(input_path)
new_name = basename.split('.')[0] + '_bg-removed.' + basename.split('.')[1]
output_path = new_name

input = Image.open(input_path)
output = remove(input)
output = output.convert('RGB')
output.save(output_path)
# the end
