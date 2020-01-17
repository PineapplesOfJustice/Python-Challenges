# title: re (actually a hint to regex or regular expression which is used to find string patterns)
import re
# hint: One small letter, surrounded by EXACTLY three big bodyguards on each of its sides.

'obvious, but wrong solution:' # one small character with three captial characters on each side
with open("given.txt", "r") as data, open("wrong.txt", "w") as wrong:
    string = data.read()
    match = re.findall("[A-Z][A-Z][A-Z][a-z][A-Z][A-Z][A-Z]", string)
    if match:
        newString = ""
        for i in match:
            newString += i[0:3] + " " + i[3] + " " + i[4:7] + "\n"
            # space is added to separate small and capital characters
        wrong.write(newString)
        # result: found in "wrong.txt" (total lines: 477)

'correct solution: (step 1)' # one small character with EXACTLY three capital characters on each side
with open("given.txt", "r") as data, open("solution.txt", "w") as solution:
    string = data.read()
    match = re.findall("[a-z][A-Z][A-Z][A-Z][a-z][A-Z][A-Z][A-Z][a-z]", string)
    if match:
        newString = ""
        for i in match:
            newString += i[0] + " " + i[1:4] + "  |" + i[4] + "|  " + i[5:8] + " " + i[8] + "\n"
            # space is added to separate small and capital characters
        print(newString)
        solution.write(newString)
        # result: found in "solution.txt" (total lines: 10)

'correct solution (step 2):' # notice that there are ten results, the answer is a concatenation of ten small characters
with open("solution.txt", "r") as solution:
    string = ""
    for line in solution:
        string += line[8]
    print(string + ".html")
    # result: "linkedlist.html"
