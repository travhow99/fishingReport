from flask import Flask, render_template
app = Flask(__name__)

@app.route('/')
def index():
   return render_template('index.html')

import urllib
from bs4 import BeautifulSoup

#Today's work
class River:
    def __init__(self, name, peteLink, rockyLink):
        self.name = name
        self.peteLink = peteLink
        self.rockyLink = rockyLink

    def getStPete(self):
            url = "https://stpetes.com/blog/river-reports/" + self.peteLink
            html = urllib.urlopen(url).read()
            soup = BeautifulSoup(html, 'html.parser')
            report = soup.select('.post-content p')
            lines = [span.get_text() for span in report]
            #print riverName + ": "
            stPeteCredit = "<p class='credit'>Report courtesy of <a href='https://stpetes.com/'>St. Peter's Fly Shop</a> in Fort Collins, Colorado.</p>"

            if self.name == "Big Thompson River" or self.name == "Cache La Poudre River":
                if self.name == "Cache La Poudre River":
                    self.stPeteReport = self.name + ": " + lines[3] + lines[4] + lines[5] + stPeteCredit
                else:
                    self.stPeteReport = self.name + ": " + lines[4] + lines[5] + lines[6] + stPeteCredit
            elif self.name == "Rocky Mountain National Park" or self.name == "Encampment River" or self.name == "Laramie":
                self.stPeteReport = self.name + ": " + lines[2] + stPeteCredit
            elif self.name == "Upper North Platte":
                self.stPeteReport = self.name + ": " + lines[1] + stPeteCredit
            elif self.name == "Gray Reef River":
                self.stPeteReport = self.name + ": " + lines[2] + lines[3] + lines[4] + stPeteCredit


    def getRocky(self):
        rockyCredit = "<p class='credit'>Report courtesy of <a href='http://www.rockymtanglers.com/'>Rocky Mountain Anglers</a> in Boulder, Colorado.</p>"

        url = "http://www.rockymtanglers.com/" + self.rockyLink + ".riv"
        html = urllib.urlopen(url).read()
        soup = BeautifulSoup(html, 'html.parser')
        report = soup.find_all('span', {"class":"report"})

        lines = [span.get_text() for span in report]
        self.rockyReport = lines[0]
        #return render_template('rivers.html', river = riverName, report = lines[0])
ark = River("Arkansas River", "", "Arkansas_River")
ark.getRocky()
@app.route("/arkansas_river")
def arkData():
    return render_template('rivers.html', river = ark.name, report = ark.rockyReport)


blue = River("Blue River", "", "Blue_River")
blue.getRocky()

boulderCrk = River("Boulder Creek", "", "Boulder_Creek")
boulderCrk.getRocky()

bigT = River("Big Thompson River", "Big-Thompson", "Big_Thompson_River")
bigT.getStPete()
bigT.getRocky()

clearCrk = River("Clear Creek", "", "Clear_Creek")
clearCrk.getRocky()

colorado = River("Colorado River", "", "Colorado_River")
colorado.getRocky()

encampment = River("Encampment River", "encampment", "")
encampment.getStPete()

fryingpan = River("Fryingpan River", "", "Fryingpan_River")
fryingpan.getRocky()

grayReef = River("Gray Reef River", "gray-reef", "")
grayReef.getStPete()

gunnison = River("Gunnison Taylor River", "", "Gunnison_Taylor_River")
gunnison.getRocky()

laramie = River("Laramie", "laramie", "")
laramie.getStPete()

poudre = River("Cache La Poudre River", "cache-la-poudre", "Cache_La_Poudre_River")
poudre.getStPete()
poudre.getRocky()

nPlatte = River("Upper North Platte", "upper-north-platte", "North_Platte_River")
nPlatte.getStPete()
nPlatte.getRocky()

roaringFork = River("Roaring Fork River", "", "Roaring_Fork_River")
roaringFork.getRocky()

rocky = River("Rocky Mountain National Park", "rocky-mountain-national-park", "Rocky_Mtn_Nat_Park")
rocky.getStPete()
rocky.getRocky()

sBoulderCrk = River("South Boulder Creek", "", "South_Boulder_Creek")
sBoulderCrk.getRocky()

sPlatte = River("South Platte River", "", "South_Platte_River")
sPlatte.getRocky()

stillwaters = River("Stillwaters", "stillwaters", "")
stillwaters.getStPete()

yampa = River("Yampa River", "", "Yampa_River")

if __name__ == '__main__':
    app.run(debug = True)
#big t: 4 5 6
#poudre: 3 4 5 6
#upper north platte: 1
# rocky : 2
#Gray reef:2 3 4
#encampment: 2
#Laramie: 2
