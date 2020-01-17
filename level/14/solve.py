# title: walk around
# page source hint: remember: 100*100 = (100+99+99+98) + (...
# file: "wire.png" [size: 10000 x 1]

from PIL import Image, ImageDraw

'correct solution (step 1):' # contruct a 100 x 100 image using "wire.png"
wire = Image.open("wire.png")
data = wire.getdata() # get an array of pixel values
image = Image.new('RGB', (100, 100))
draw = ImageDraw.Draw(image) # enable the image to be altered
dx, dy = [1, 0, -1, 0], [0, 1, 0, -1] # determine the direction in which image is drawn [ie: rotation]
x, y = 0, 1 # initial location
pixel = 0
for i in range(199): # (2*100 - 1)
    for j in range((200 - i) // 2):
        # note: [(200 - i) // 2]  ->  [100, 99, 99, 98 ...]
        x += dx[i % 4]
        y += dy[i % 4]
        draw.point((x, y), data[pixel])
        pixel += 1
image.show()
image.save("solution.png")
# result: "cat.html"

'correct solution (step 2):' # replace url extension "italy.html" with "cat.html"
# new hint: and its name is uzi. you'll hear from him later.
# new file: "uzi.jpg"
print("remember: uzi the cat")
print("uzi.html")
