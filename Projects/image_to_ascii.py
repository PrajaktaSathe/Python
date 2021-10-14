import sys
from PIL import Image

i_path = sys.argv[1]
img = Image.open(i_path)
width, height = img.size
aspect_ratio = height/width
nwidth = 120
nheight = aspect_ratio * nwidth * 0.55
img = img.resize((nwidth, int(nheight)))
# converts image to greyscale
img = img.convert('L')
pixels = img.getdata()
# replace pixels according to how dark they are
chars = ["B","S","#","&","@","$","%","*","!",":","."]
npixels = [chars[pixel//25] for pixel in pixels]
npixels = ''.join(npixels)
npixels_count = len(npixels)
ascii_image = [npixels[index:index + nwidth] for index in range(0, npixels_count, nwidth)]
ascii_image = "\n".join(ascii_image)
print(ascii_image)
with open("ascii_image.txt", "w") as f:
 f.write(ascii_image)