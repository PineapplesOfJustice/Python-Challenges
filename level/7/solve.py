# title: smarty
# file: "oxygen.png"

from PIL import Image

'correct solution (step 1):'
# observation: there is a spectrum of various shades of gray
# conclusion: each shade represents an ASCII character
# note: this is not an obvious conclusion
oxygen = Image.open("oxygen.png")
spectra = oxygen.convert('RGB')
string = ""
for i in range(87): # there are 87 shades in the spectra
    shade, of, gray = spectra.getpixel((i*7, 47))
    # each shade is 7 pixel wide
    # the spectra is vertically centered: 94/2 = 47.
    string += chr(shade)
print(string)
# new hint: smart guy, you made it. the next level is [105, 110, 116, 101, 103, 114, 105, 116, 121]

'correct solution (step 2):'
key = [105, 110, 116, 101, 103, 114, 105, 116, 121]
string = ""
for i in key:
    string += chr(i)
print(string + ".html")
# result: "integrity.html"
