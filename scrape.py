import urllib
from bs4 import BeautifulSoup

riverList = {'Arkansas River': 'Arkansas_River', 'Big Thompson River': 'Big_Thompson_River', 'Blue River': 'Blue_River', 'Boulder Creek': 'Boulder_Creek', 'Cache La Poudre River': 'Cache_La_Poudre_River', 'Clear Creek': 'Clear_Creek', 'Colorado River': 'Colorado_River', 'Fryingpan River': 'Fryingpan_River', 'Gunnison Taylor River': 'Gunnison_Taylor_River', 'North Platte River': 'North_Platte_River', 'Roaring Fork River': 'Roaring_Fork_River', 'Rocky Mountain National Park': 'Rocky_Mtn_Nat_Park', 'Saint Vrain River': 'Saint_Vrain_River', 'South Boulder Creek': 'South_Boulder_Creek', 'South Platte River': 'South_Platte_River', 'Yampa River': 'Yampa_River'}

for riverName, riverLink in riverList.items():
    url = "http://www.rockymtanglers.com/" + riverLink + ".riv"
    html = urllib.urlopen(url).read()
    soup = BeautifulSoup(html, 'html.parser')
    report = soup.find_all('span', {"class":"report"})

    lines = [span.get_text() for span in report]

    print riverName + ': ' + lines[-1]


#
