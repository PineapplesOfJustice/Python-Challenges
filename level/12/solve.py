# title: dealing evil
# file: "evil1.jpg" [image size: 640x480]
# note: there are 5 stacks of cards

from PIL import Image, ImageFile

# realize that "evil1.jpg" implies that there are more "evil_.jpg"
'correct solution (step 1):' # replace url extension "evil.html" with "evil2.jpg"
# new file: "evil2.jpg"
# new hint: not ".jpg" - - ".gfx"

'correct solution (step 2):' # replace url extension "evil.html" with "evil2.gfx"
# new file: "evil2.gfx"

'correct solution (step 3):' # replace url extension "evil.html" with "evil3.jpg"
# new file: "evil3.jpg"
# new hint: no more evils ...

'correct solution (step 4):' # replace url extension "evil.html" with "evil4.jpg"
# new file: "evil4.jpg"
# new hint: nothing?
with open("evil4.jpg", "r") as evil4:
    content = evil4.read()
    print("remember: Bert is evil!")
    # new hint: Bert is evil! go back!
    # reference: "Bert is evil" meme from 1998.
    # see: "bert_is_evil.png"

'correct solution (step 5):' # access "evil2.gfx"
with open("evil2.gfx", "rb") as file:
    data = file.read()
    # extended analysis:
        # len(data) = 67575
        # there are 5 stack of cards
        # title: "dealing evil"
        # trend: "evil" = "image" [ie: "no more evils ..." from step 3]
        # 67575 % 5 = 0
    # conclusion: data will be divided into 5 image files
    # note: this is not an obvious conclusion
    for i in range(5):
        with open("solution_" + str(i+1) + ".jpg" ,"wb") as image:
            image.write(data[i::5])
            # [i::5] mean that the image will receive a byte for every 5 byte
            # literally "dealing evil"
            # result: found in "solution_1.jpg", "solution_2.jpg" ... "solution_5.jpg"

'correct solution (step 6):' # look at new images as a whole
newImage = Image.new('RGB', (1600, 240)) # imageSize: [320*5, 240]
ImageFile.LOAD_TRUNCATED_IMAGES = True # necessary because "solution_4.jpg" is truncated
for i in range(5):
    image = Image.open("solution_" + str(i+1) + ".jpg")
    image = image.resize((320, 240))
    newImage.paste(image, (i*320, 0))
newImage.show()
print("disproportional.html")
newImage.save("solution.jpg")
# result: found in "solution.jpg"
# result: "disproportional.html"
