# title: working hard?
# hint: where is the missing link?
# page source hint: un (UserName) = 'BZh91AY&SYA\xaf\x82\r\x00\x00\x01\x01\x80\x02\xc0\x02\x00 \x00!\x9ah3M\x07<]\xc9\x14\xe1BA\x06\xbe\x084'
# page source hint: pw (PassWord) = 'BZh91AY&SY\x94$|\x0e\x00\x00\x00\x81\x00\x03$ \x00!\x9ah3M\x13<]\xc9\x14\xe1BBP\x91\xf08'

# observation: "integrity.jpg" links to "../return/good.html" using usemap="#notinsect"
# barrier: a username and password is required to access the content

import bz2

'correct solution:' # decompress the username and password
# since the usemap states "notinsect;" the bee jokes refers to something else (ie: bz2 compression)
# note: this is not an obvious conclusion
given_un = b"BZh91AY&SYA\xaf\x82\r\x00\x00\x01\x01\x80\x02\xc0\x02\x00 \x00!\x9ah3M\x07<]\xc9\x14\xe1BA\x06\xbe\x084"
given_pw = b"BZh91AY&SY\x94$|\x0e\x00\x00\x00\x81\x00\x03$ \x00!\x9ah3M\x13<]\xc9\x14\xe1BBP\x91\xf08"
username = bz2.decompress(given_un).decode("utf-8")
password = bz2.decompress(given_pw).decode("utf-8")
print("username: " + username)
print("password: " + password)
# result: username = "huge"
# result: password = "file"
