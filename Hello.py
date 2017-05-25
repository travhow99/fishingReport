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
                    self.stPeteReport = lines[3] + lines[4] + lines[5]
                else:
                    self.stPeteReport = lines[4] + lines[5] + lines[6]
            elif self.name == "Rocky Mountain National Park" or self.name == "Encampment River" or self.name == "Laramie":
                self.stPeteReport = lines[2]
            elif self.name == "Upper North Platte":
                self.stPeteReport = lines[1]
            elif self.name == "Gray Reef River":
                self.stPeteReport = lines[2] + lines[3] + lines[4]


    def getRocky(self):
        rockyCredit = "<p class='credit'>Report courtesy of <a href='http://www.rockymtanglers.com/'>Rocky Mountain Anglers</a> in Boulder, Colorado.</p>"

        url = "http://www.rockymtanglers.com/" + self.rockyLink + ".riv"
        html = urllib.urlopen(url).read()
        soup = BeautifulSoup(html, 'html.parser')
        report = soup.find_all('span', {"class":"report"})

        lines = [span.get_text() for span in report]
        self.rockyReport = lines[-1]
        #return render_template('rivers.html', river = riverName, report = lines[0])
ark = River("Arkansas River", "", "Arkansas_River")
ark.getRocky()
@app.route("/arkansas_river")
def arkData():
    return render_template('rivers.html', river = ark.name, rockyMtnReport = ark.rockyReport)


blue = River("Blue River", "", "Blue_River")
blue.getRocky()
@app.route("/blue_river")
def blueData():
    return render_template('rivers.html', river = blue.name, rockyMtnReport = blue.rockyReport)

boulderCrk = River("Boulder Creek", "", "Boulder_Creek")
boulderCrk.getRocky()
@app.route("/boulder_creek")
def boulderCrkData():
    return render_template('rivers.html', river = boulderCrk.name, rockyMtnReport = boulderCrk.rockyReport)

bigT = River("Big Thompson River", "Big-Thompson", "Big_Thompson_River")
bigT.getStPete()
bigT.getRocky()
@app.route("/big_thompson_river")
def bigTData():
    return render_template('rivers.html', river = bigT.name, rockyMtnReport = bigT.rockyReport, stPeteReport = bigT.stPeteReport)

clearCrk = River("Clear Creek", "", "Clear_Creek")
clearCrk.getRocky()
@app.route("/clear_creek")
def clearCrkData():
    return render_template('rivers.html', river = clearCrk.name, rockyMtnReport = clearCrk.rockyReport)

colorado = River("Colorado River", "", "Colorado_River")
colorado.getRocky()
@app.route("/colorado_river")
def coloradoData():
    return render_template('rivers.html', river = colorado.name, rockyMtnReport = colorado.rockyReport)

encampment = River("Encampment River", "encampment", "")
encampment.getStPete()
@app.route("/encampment_river")
def encampmentData():
    return render_template('rivers.html', river = encampment.name, stPeteReport = encampment.stPeteReport)

fryingpan = River("Fryingpan River", "", "Fryingpan_River")
fryingpan.getRocky()
@app.route("/frying_pan_river")
def fryingpanData():
    return render_template('rivers.html', river = fryingpan.name, rockyMtnReport = fryingpan.rockyReport)

grayReef = River("Gray Reef River", "gray-reef", "")
grayReef.getStPete()
@app.route("/gray_reef_river")
def grayReefData():
    return render_template('rivers.html', river = grayReef.name, stPeteReport = grayReef.stPeteReport)

gunnison = River("Gunnison Taylor River", "", "Gunnison_Taylor_River")
gunnison.getRocky()
@app.route("/gunnison_taylor_river")
def gunnisonData():
    return render_template('rivers.html', river = gunnison.name, rockyMtnReport = gunnison.rockyReport)

laramie = River("Laramie", "laramie", "")
laramie.getStPete()
@app.route("/laramie_river")
def laramieData():
    return render_template('rivers.html', river = laramie.name, stPeteReport = laramie.stPeteReport)

poudre = River("Cache La Poudre River", "cache-la-poudre", "Cache_La_Poudre_River")
poudre.getStPete()
poudre.getRocky()
@app.route("/poudre_river")
def poudreData():
    return render_template('rivers.html', river = poudre.name, rockyMtnReport = poudre.rockyReport, stPeteReport = poudre.stPeteReport)

nPlatte = River("Upper North Platte", "upper-north-platte", "North_Platte_River")
nPlatte.getStPete()
nPlatte.getRocky()
@app.route("/north_platte_river")
def nPlatteData():
    return render_template('rivers.html', river = nPlatte.name, rockyMtnReport = nPlatte.rockyReport, stPeteReport = nPlatte.stPeteReport)

roaringFork = River("Roaring Fork River", "", "Roaring_Fork_River")
roaringFork.getRocky()
@app.route("/roaring_fork_river")
def roaringForkData():
    return render_template('rivers.html', river = roaringFork.name, rockyMtnReport = roaringFork.rockyReport)

rocky = River("Rocky Mountain National Park", "rocky-mountain-national-park", "Rocky_Mtn_Nat_Park")
rocky.getStPete()
rocky.getRocky()
@app.route("/rocky_mtn_nat_park")
def rockyData():
    return render_template('rivers.html', river = rocky.name, rockyMtnReport = rocky.rockyReport, stPeteReport = rocky.stPeteReport)

stVrain = River("Saint Vrain River", "Saint_Vrain_River", "")
stVrain.getStPete()
@app.route("/saint_vrain_river")
def stVrainData():
    return render_template('rivers.html', river = stVrain.name, stPeteReport = stVrain.stPeteReport)

sBoulderCrk = River("South Boulder Creek", "", "South_Boulder_Creek")
sBoulderCrk.getRocky()
@app.route("/south_boulder_creek")
def sBoulderCrkData():
    return render_template('rivers.html', river = sBoulderCrk.name, rockyMtnReport = sBoulderCrk.rockyReport)

sPlatte = River("South Platte River", "", "South_Platte_River")
sPlatte.getRocky()
@app.route("/south_platte_river")
def sPlatteData():
    return render_template('rivers.html', river = sPlatte.name, rockyMtnReport = sPlatte.rockyReport)

stillwater = River("Stillwater", "stillwater", "")
stillwater.getStPete()
@app.route("/stillwater")
def stillwaterData():
    return render_template('rivers.html', river = stillwater.name, stPeteReport = stillwater.stPeteReport)

yampa = River("Yampa River", "", "Yampa_River")
yampa.getRocky()
@app.route("/yampa_river")
def yampaData():
    return render_template('rivers.html', river = yampa.name, rockyMtnReport = yampa.rockyReport)

if __name__ == '__main__':
    app.run(debug = True)
#big t: 4 5 6
#poudre: 3 4 5 6
#upper north platte: 1
# rocky : 2
#Gray reef:2 3 4
#encampment: 2
#Laramie: 2
