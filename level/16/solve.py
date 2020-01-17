# title: let me get this straight
# file: "mozart.gif" [size: 640 x 480]

from PIL import Image, ImageDraw
import numpy

# observation: each "line" in "mozart.gif" have a shorter magenta line with white ends
# observation: each magenta line is the same length

'correct solution (step 1):' # align the magenta lines

mozart = Image.open("mozart.gif").convert("RGB")
# note: because the image is a gif file, convert("RGB") is necessary for conversion to array
wire = list(mozart.getdata()) # get pixel data from "mozart.gif" as one long array
data = [wire[640*y:640*y+640] for y in range(480)] # data[y][x]
for x in range(640):
    if sum(data[0][x]) / 3 > 200: # where [sum(data[0][x]) / 3] is the grayscale value of the pixel
        magenta = data[0][x + 1]
        # in the first line, the first magenta follows the first white
        break # end for loop
for y in range(480):
    index = data[y].index(magenta) # find the index of the first magenta
    difference = (641 - index) % 640
    data[y] = data[y][640-difference:] + data[y][:640-difference]

data = numpy.asarray(data, dtype=numpy.uint8)
# note: the default dtype=numppy.int32, which is not readable by Image.fromarray()
image = Image.fromarray(data)
image.show()
image.save("solution.jpg")
print("romance.html")
# result: "romance.html"
