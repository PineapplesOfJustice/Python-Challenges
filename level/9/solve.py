# title: connect the dots
# page source hint: first + second = ?
# file: "good.jpg", "first.txt", "second.txt"
# observation: there are square dots in "good.jpg"

import json
from PIL import Image, ImageFont, ImageDraw

# global variables [used to reduce repeated codes]
files = [
    {"name": "first", "color_enum": "red", "color_caption": "red"},
    {"name": "second", "color_enum": "blue", "color_caption": "#1E90FF"},
]
font_enum = ImageFont.truetype("chakraPetch.ttf", 10)
font_caption = ImageFont.truetype("chakraPetch.ttf", 32)

'correct solution (step 1):' # connect the dots using "first.txt" and "second.txt"
for object in files:
    with open(object["name"] + ".txt", "r") as file:
        data = json.load(file)
        image = Image.open("good.jpg")
        draw = ImageDraw.Draw(image) # enable the image to be altered
        for i in range(0, len(data)-2, 2):
            draw.line(data[i:i+4], fill="black", width=2, joint="curve")
            draw.text((data[i], data[i+1]), str(int(i/2 + 1)), font=font_enum, fill=object["color_enum"])
            # note: PIL's line function treats a list of number as [x1, y1, x2, y2, ... and so forth]
            # note: PIL's text function needs the position vector as a tuple: (x, y)
        caption_width, caption_height = draw.textsize(object["name"], font=font_caption, stroke_width=1) # used to center image's caption
        draw.text((508-caption_width/2, 350), object["name"], font=font_caption, fill=object["color_caption"], stroke_width=1, stroke_fill="black")
        image.save("solution_" + object["name"][0] + ".jpg")
# result: "solution_f.jpg" and "solution_s.jpg"

'correct solution (step 2):' # combine result from "solution_f.jpg" and "solution_s.jpg"
image = Image.open("good.jpg")
draw = ImageDraw.Draw(image) # enable the image to be altered
for object in files:
    with open(object["name"] + ".txt", "r") as file:
        data = json.load(file)
        for i in range(0, len(data)-2, 2):
            draw.line(data[i:i+4], fill="black", width=2, joint="curve")
            draw.text((data[i], data[i+1]), str(int(i/2 + 1)), font=font_enum, fill=object["color_enum"])
            # note: PIL's line function treats a list of number as [x1, y1, x2, y2, ... and so forth]
            # note: PIL's text function needs the position vector as a tuple: (x, y)
caption_width, caption_height = draw.textsize("bull", font=font_caption, stroke_width=1) # used to center image's caption
draw.text((508-caption_width/2, 350), "bull", font=font_caption, fill="#AF6E4D", stroke_width=1, stroke_fill="black")
image.show()
image.save("solution.jpg")
print("bull.html")
# result: "solution.jpg"
# result: "bull.html"

'alternate solution ("cow.html"):'
# new hint: "hmm. it's a male."
# result: "bull.html"
