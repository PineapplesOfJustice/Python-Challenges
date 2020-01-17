'link: http://www.pythonchallenge.com/pc/return/balloons.html'
'authentication: (huge, file)'

import gzip

# title: can you tell the difference?
# hint: it is more obvious that what you might think

'correct solution (step 1):' # go to "brightness.html"
# new hint: maybe consider deltas.gz

with gzip.open("deltas.gz", "r") as file, open("deltas.txt", "w") as content:
    content.write(file.read().decode("utf-8"))

print("jelly")
with open("deltas.txt", "r") as content, open("solution.txt", "w") as solution:
    # data_unformatted = content.read().split("\n")
    # comparison_length = (len(content.readline()) - 3) // 2
    # data = [[], []]
    # for i in range(len(data_unformatted)-3, len(data_unformatted)):
    #     if not data_unformatted[i][:comparison_length].isspace():
    #         data[0].append(data_unformatted[i][:comparison_length])
    #     if not data_unformatted[i][comparison_length + 3:].isspace():
    #         data[1].append(data_unformatted[i][comparison_length + 3:])
    print(content.readline())
    print(len(content.readline()))
    print(comparison_length)
    # print(data[0])
    string = ""
    while len(data[0]) != len(data[1]):
        if data[0][0] == data[1][0]:
            data[0].pop(0)
            data[1].pop(0)
        else:
            if data[0][1] == data[1][0]:
                string += data[0].pop(0) + "\n"
            elif data[0][0] == data[1][1]:
                string += data[1].pop(0) + "\n"
    solution.write(string)

    # comparison_length = (len(content.readline()) - 3) // 2
    # string = ""
    # for line in data:
    #     if line[:comparison_length] != line[comparison_length + 3:]:
    #         for i in range(comparison_length):
    #             if line[i] != line[i + length + 3]:
    #                 string += line[i] + " | " + line[i + length + 3] + "\n"
    # solution.write(string)
