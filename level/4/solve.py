# title: n/a
# hint: linkedlist.php

import urllib.request

'correct solution (step 1):' # replace the url extension "linkedlist.html" with "linkedlist.php"
# new title: follow the chain
# page source hint: urllib may help. DON'T TRY ALL NOTHINGS, since it will never end. 400 times is more than enough.
# observation: the image have a link tag

'correct solution (step 2):' # click on the chainsaw image. It will add the query parameter "nothing=12345" to the url
# new hint: and the next nothing is 44827

'correct solution (step 3):' # replace the query parameter "nothing=12345" with "nothing="44827"
# new hint: and the next nothing is 45439

'correct solution (step 4):' # replace the query parameter "nothing=44827" with "nothing="45439"
# new hint: Your hands are getting tired and the next nothing is 94485

'correct solution (step 5):' # at this point, it is obvious that this cycle will be repeated
attempt = 0
nothing = "12345"
string = ""
while attempt < 400:
    try: # try to read the URL
        source = urllib.request.urlopen("http://www.pythonchallenge.com/pc/def/linkedlist.php?nothing=" + nothing)
        content = source.read().decode("utf-8")
        print(content)
        string += content + "\n"
        if "next nothing is " in content:
            nothing = content.split("next nothing is ")[1]
        elif "Divide by two" in content: # neccessary because it is asked midway in the nothing chain
            nothing = str(int(nothing) / 2)
        else:
            break
    except Exception as e: # catch the error - if any
        print(str(e))
    attempt += 1
with open("solution.txt", "w") as solution:
    solution.write(string)
    # result: "peak.html"
