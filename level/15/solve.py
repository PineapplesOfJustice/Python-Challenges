# title: whom?
# page source hint: he ain't the youngest, he is the second
# page source hint: todo: buy flowers for tomorrow

import calendar
import requests
import json

# observation: February have 29 days -> leap year
# observation: there is a hole in "screen15.jpg" between 1 and 6 -> year = (1 _ _ 6)
# observation: 26th of January is circled
# observation: 1st of January is Thursday

'correct solution (step 1):' # find the date
years = []
for year in range(1006, 1997, 10): # the year is (1 _ _ 6)
    if calendar.isleap(year) and calendar.weekday(year, 1, 1) == 3: # where 3 is Thursday
        years.append(year)
year = str(years[-2]) # recall: he ain't the youngest, he is the second
# result: 1756
# analysis: the 26th of January is circled and the flowers are meant for "tomorrow"
# conclusion: the date is 1756-01-27
date = year + "-01-27"
print(date)

'correct solution (step 2):' # get information related to the date
data = requests.get("http://history.muffinlabs.com/date/1/27").json() # history API scrapes information from Wikipedia
# filter by year
keys = ["Events", "Births", "Deaths"]
for key in keys:
    if key in data["data"]:
        for i in range(len(data["data"][key])-1, -1, -1):
            if data["data"][key][i]["year"] != year:
                data["data"][key].pop(i)
        if len(data["data"][key]) == 0:
            data["data"].pop(key, None)
with open("solution.txt", "w") as solution:
    solution.write(json.dumps(data, indent=2))
    print("mozart.html")
    # result: "mozart.html"

# credits: wikipedia!
