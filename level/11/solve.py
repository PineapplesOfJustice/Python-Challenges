# title: odd even
# file: "cave.jpg" [image size: 640x480]

from PIL import Image, ImageDraw, ImageEnhance

'correct solution:' # filter image based on pixel positions
even = []
odd = []
for x in range(640):
    for y in range(480):
        if (x + y) % 2 == 0:
            even += [x, y]
        else:
            odd += [x, y]
# even image:
image = Image.open("cave.jpg")
draw = ImageDraw.Draw(image) # enable the image to be altered
draw.point(even, fill="black")
image.save("solution_even.jpg")
# result: found in "solution_even.jpg"
# odd image:
image = Image.open("cave.jpg")
draw = ImageDraw.Draw(image) # enable the image to be altered
draw.point(odd, fill="black")
enhancer = ImageEnhance.Sharpness(image)
enhanced = enhancer.enhance(5) # store an enhanced version of the image [greater contrast]
enhanced.show()
enhanced.save("solution_odd.jpg")
print("evil.html")
# result: found in "solution_odd.jpg"
# result: "evil.html"
