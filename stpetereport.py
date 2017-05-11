import urllib
from bs4 import BeautifulSoup

riverList = {'Big Thompson River': 'Big-Thompson','Cache La Poudre River': 'cache-la-poudre', 'Upper North Platte': 'upper-north-platte', 'Rocky Mountain National Park': 'rocky-mountain-national-park', 'Gray Reef River': 'gray-reef', 'Encampment River': 'encampment', 'Laramie': 'laramie'}#, 'Stillwaters River': 'stillwaters'}

for riverName, riverLink in riverList.items():
    url = "https://stpetes.com/blog/river-reports/" + riverLink
    html = urllib.urlopen(url).read()
    soup = BeautifulSoup(html, 'html.parser')
    report = soup.select('.post-content p')

    lines = [span.get_text() for span in report]
    print riverName + ": "

    if riverName == "Big Thompson River" or riverName == "Cache La Poudre River":
        if riverName == "Cache La Poudre River":
            print lines[3]
        print lines[4]
        print lines[5]
        if riverName == "Big Thompson River":
            print lines[6]
    elif riverName == "Rocky Mountain National Park" or riverName == "Encampment River" or riverName == "Laramie":
        print lines[2]
    elif riverName == "Upper North Platte":
        print lines[1]
    elif riverName == "Gray Reef River":
        print lines[2]
        print lines[3]
        print lines[4]



#big t: 4 5 6
#poudre: 3 4 5 6
#upper north platte: 1
# rocky : 2
#Gray reef:2 3 4
#encampment: 2
#Laramie: 2
