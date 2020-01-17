# title: peak hell
# hint: pronounce it
# page source hint: peak hell sounds familiar?
# file: banner.p (found in the page source)

import pickle, json

'correct solution (step 1):' # notice: peak hell -> pickle
with open("banner.p", "rb") as pickleFile, open("data.txt", "w") as dataFile:
    # note: pickleFile has to be opened as a non-encoded binary file: "rb"
    # note: pickleFile has to be opened using Unix new lines "LF" rather than "CRLF"; see https://github.com/udacity/ud120-projects/issues/181
    content = pickle.load(pickleFile)
    json.dump(content, dataFile)
    # result: found in "data.txt"

'correct solution (step 2):' # the data is a blueprint for an ASCII art which is the answer
with open("data.txt", "r") as dataFile, open("solution.txt", "w") as solution:
    data = json.load(dataFile)
    string = ""
    for line in data:
        for thing in line:
            string += thing[0] * thing[1]
        string += "\n"
    print(string)
    solution.write(string)
    # result: found in "solution.txt"
    # result: "channel.html"
