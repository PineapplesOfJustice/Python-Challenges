# title: what are you looking at?
# hint: len(a[30]) = ?
# file: "sequence.txt"

'correct solution (step 1):' # based on "look and say" sequence
# a = ["1"] + ["one 1"] + ["two 1"] + ["one 2" + "one 1"] + ["one 1" + "one 2" + "two 1"]
# note: this conclusion can be drawn from 1) being an auditory based person, or 2) awareness of run length encoding
# note: this is a recursive sequence
sequence = ["1"]
string = "a = [\n\t" + sequence[0] + ",\n"
print(sequence[0])
while len(sequence) < 31:
    encoder = {"digit": sequence[-1][0], "quantiy": 0}
    substring = ""
    for digit in sequence[-1]: # where sequence[-1] is the last string in the sequence
        if digit == encoder["digit"]:
            encoder["quantity"] += 1
        else:
            substring += str(encoder["quantity"]) + encoder["digit"]
            encoder = {"digit": digit, "quantiy": 1}
    substring += str(encoder["quantity"]) + encoder["digit"]
    print(substring)
    string += "\t" + substring + ",\n"
    sequence.append(substring)
string += "]\n"
with open("solution.txt", "w") as solution:
    solution.write(string)
    # result: found in "solution.txt"

'correct solution (step 2):'
print(str(len(sequence[30])) + ".html")
# result: "5808.html"
