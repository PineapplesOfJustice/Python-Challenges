# title: now there are pairs
# page source hint: <html> <!-- <-- zip -->

import zipfile

'obvious, but wrong solution (step 1):' # replace the url extension "channel.html" with "zip.html"
# new hint: yes. find the zip.

'obvious, but wrong solution (step 2):' # replace the url extension "zip.html" with "pants.html"
# new hint: amazing. zoom in

'obvious, but wrong solution (step 3):' # replace the url extension "pants.html" with "zipper.html"
# new hint: [:3] todo: tell everyone that [:n] is to take the first n characters...

'correct solution (step 1):' # replace the url extension "channel.html" with "channel.zip"
# file: "channel.zip"

'correct solution (step 2):' # read "readme.txt" inside "channel.zip"
# hint1: start from 90052
# hint2: answer is inside the zip

'correct solution (step 3):' # it is another nothing chain (similar to level 4)
with zipfile.ZipFile('channel.zip') as zip:
    zipLength = len(zip.namelist())
    attempt = 1
    nothing = "90052"
    string = ""
    while attempt < zipLength:
        with zip.open(nothing + ".txt", "r") as nothingFile:
            content = nothingFile.read().decode("utf-8")
            # print(content)
            string += content + "\n"
            if "Next nothing is " in content:
                nothing = content.split("Next nothing is ")[1]
            else:
                break
        attempt += 1
    with open("solution_1.txt", "w") as solution:
        solution.write(string)
        # result: found in "solution_1.txt"

'correct solution (step 4):' # collect the comments
with zipfile.ZipFile('channel.zip') as zip:
    zipLength = len(zip.namelist())
    attempt = 1
    nothing = "90052"
    string = ""
    while attempt < zipLength:
        with zip.open(nothing + ".txt", "r") as nothingFile:
            content = nothingFile.read().decode("utf-8")
            comment = zip.getinfo(nothing + ".txt").comment.decode("utf-8")
            string += comment
            if "Next nothing is " in content:
                nothing = content.split("Next nothing is ")[1]
            else:
                break
        attempt += 1
    with open("solution_2.txt", "w") as solution:
        print(string)
        solution.write(string)
        # result: found in "solution_2.txt"
        # result: "hockey.html"

'correct solution (step 5):' # replace the url extension "channel.html" with "hockey.html"
# new hint: it's in the air. look at the letters.
# analysis: ASCII word "HOCKEY" is made of O,X,Y,G,E,N
print("look at the letters. -> oxygen.html")
# result: "oxygen.html"
