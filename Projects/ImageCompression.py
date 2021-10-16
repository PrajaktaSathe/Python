# pip install Pillow

import os
import sys
from PIL import Image

def compressImage(file):
	
	filepath = os.path.join(os.getcwd(), file)
	
	picture = Image.open(filepath)
  
	picture.save("Compressed_"+file,
				"JPEG",
				optimize = True,
				quality = 10)
	return

if __name__ == "__main__":
  
	cwd = os.getcwd()
  
	formats = ('.jpg', '.jpeg')
  
	for file in os.listdir(cwd):
		if os.path.splitext(file)[1].lower() in formats:
			print('compressing', file)
			compressImage(file)
      
	print("Done")

