'link: http://www.pythonchallenge.com/pc/return/romance.html'
'authentication: (huge, file)'

# title: eat?
# observation: there is "cookies.jpg"

import requests
import bz2
import urllib.parse
import xmlrpc.client

# observation: there is "chainsaw.jpg" from level 4
# conclusion: follow the cookie chain

'correct solution (step 1):' # go to level 4
request = requests.get("http://www.pythonchallenge.com/pc/def/linkedlist.php")
for cookie in request.cookies:
    print(cookie.name + ": " + cookie.value.replace("+", " "))
    # result: info: you should have followed busynothing ...

'correct solution (step 2):' # follow the busynothing chain
busynothing = "12345"
string_cookie = ""
string = ""
attempt = 0
while attempt < 400:
    request = requests.get("http://www.pythonchallenge.com/pc/def/linkedlist.php", params={"busynothing":busynothing})
    content = request.text
    string += content + "\n"
    for cookie in request.cookies:
        string_cookie += cookie.value.replace("+", " ")
    print(content)
    attempt += 1
    if "next busynothing is " in content:
        busynothing = content.split("next busynothing is ")[1] # parse next busynothing
    else:
        break
with open("busynothing.txt", "w") as file:
    file.write(string)
message = bz2.decompress(urllib.parse.unquote_to_bytes(string_cookie)).decode("utf-8")
print()
print(message)
# result: is it the 26th already? call his father and inform him that "the flowers are on their way". he'll understand.

'correct solution (step 3):' # find Leopold's phone number [Mozart's father]
proxy = xmlrpc.client.ServerProxy("http://www.pythonchallenge.com/pc/phonebook.php") # create a server proxy for "../phonebook.php"
print()
print("phone: " + proxy.phone("Leopold"))
# result: 555-VIOLIN
# result: "violin.html"

'correct solution (step 4):' # replace the url extension "romance.html" with "violin.html"
# new hint: no! i mean yes! but ../stuff/violin.php.

'correct solution (step 5):' # replace the url extension "romance.html" with "../stuff/violin.php"
# title: it's me. what do you want?
request = requests.get("http://www.pythonchallenge.com/pc/stuff/violin.php", cookies={"info":urllib.parse.quote_plus("the flowers are on their way")})
content = request.text
print("Leopold: it's me. what do you want?")
print("Leopold: the flowers are on their way?")
print("Leopold: oh well, don't you dare to forget the balloons.")
print()
print("balloons.html")
# result: oh well, don't you dare to forget the balloons.
# result: "balloons.html"
