# title: call him
# hint: phone that evil
# observation: "disprop.jpg" links to "../phonebook.php" using usemap="#evil"
# file: "phonebook.xml"

import xmlrpc.client

# observation: "phonebook.xml" is the xml response: "faultCode 105 faultString XML error: Invalid document end at line 1, column 1"
# analysis: this error occurs because an xml post request was not made
# solution: send an xml post request

'correct solution (step 1):' # send an xml post request
proxy = xmlrpc.client.ServerProxy("http://www.pythonchallenge.com/pc/phonebook.php") # create a server proxy for "../phonebook.php"
'print(proxy.system.listMethods())' # list proxy's listMethods
# result: ['phone', 'system.listMethods', 'system.methodHelp', 'system.methodSignature', 'system.multicall', 'system.getCapabilities']
'print(proxy.system.methodHelp("phone"))' # get flavor text for "phone" method
# result: Returns the phone of a person
'print(proxy.phone("Nadav Samet"))'
# result: He is not the evil
# recall: "Bert is evil" from [level 12]
# conclusion: Bert is the argument
print(proxy.phone("Leopold"))
print(proxy.phone("Bert"))
# result: 555-ITALY

'obvious, but wrong solution (step 2):' # convert "555-ITALY" to pure number
alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
telephone = "22233344455566677778889999"
translation = str.maketrans(alphabet, telephone)
string = "555-ITALY"
newString = str.translate(string, translation)
'print(newString + ".html")'
# result: "555-48259.html"

'correct solution (step 2):' # ignore: "555-" from "555-ITALY"
print("italy.html")
# result: "italy.html"
