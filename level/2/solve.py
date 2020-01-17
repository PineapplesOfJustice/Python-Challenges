# title: ocr
# hint: recognize the characters. maybe they are in the book, but MAYBE they are in the page source.

'correct solution (step 1):'
# go to the PAGE SOURCE using (ctrl + u) or (command + option + u) for safari
# page source hint: find rare characters in the mess below: (stored as "given.txt")

'correct solution (step 2):' # notice that RARE characters are ALPHANUMERIC characters
with open("given.txt", "r") as data:
    string = data.read()
    newString = ""
    for i in string:
        if i.isalnum():
            newString += i
    # this for loop only append alphanumeric characters to newString
    print(newString + ".html")
# result: "equality.html"
