# title: what about making trans?
# hint: everybody thinks twice before solving this.
'K -> M'
'O -> Q'
'E -> G'

'obvious, but wrong solution:' # only replace k, o, and e
with open("given.txt", "r") as data, open("wrong.txt", "w") as wrong:
    string = data.read()
    newString = string.replace("k", "m").replace("o", "q").replace("e", "q")
    wrong.write(newString)
    # result: found in "wrong.txt"

'correct solution (step 1):' # notice that k -> m, o -> q, and e -> g is an alphabetic shift of 2
def caesarShift(string, shift):
    newString = ""
    for i in range(len(string)):
        if string[i].isalpha():
            string[i] = chr((ord(string[i]) + shift - 96) % 26 + 96)
            # ord returns a number based on the string
            # chr returns a string based on the number
            # both combined allows for string manipulation
        newString += string[i]
    return newString
with open("given.txt", "r") as data, open("solution.txt", "w") as solution:
    string = data.read()
    newString = caesarShift(string, 2)
    print(newString)
    solution.write(newString)
    # result: found in "solution.txt"
    # next step: apply alphabetic shift to the url

'correct solution (step 2):' # apply alphabetic shift to the url
    string = "map"
    newString =
    newString = caesarShift(string, 2)
    print(string + ".html -> " + newString + ".html")
    # result: "ocr.html"
