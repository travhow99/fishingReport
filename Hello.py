from flask import Flask, redirect, request, url_for, render_template
from firebase import firebase

from time import gmtime, strftime

app = Flask(__name__)
firebase = \
    firebase.FirebaseApplication("https://co-fishing-report.firebaseio.com/", None)

@app.route('/')
def index():
   return render_template('index.html')

import urllib
from bs4 import BeautifulSoup

#Today's work
class River:
    def __init__(self, name, peteLink, rockyLink, troutsLink):
        self.name = name
        self.peteLink = peteLink
        self.rockyLink = rockyLink
        self.troutsLink = troutsLink

    def getStPete(self):
            url = "https://stpetes.com/blog/river-reports/" + self.peteLink
            html = urllib.urlopen(url).read()
            soup = BeautifulSoup(html, 'html.parser')
            report = soup.select('.post-content p')
            lines = [span.get_text() for span in report]

            stPeteCredit = "<p class='credit'>Report courtesy of <a href='https://stpetes.com/'>St. Peter's Fly Shop</a> in Fort Collins, Colorado.</p>"

            if self.name == "Big Thompson River" or self.name == "Cache La Poudre River" or self.name == "Upper North Platte":
                if self.name == "Cache La Poudre River":
                    self.stPeteReport = lines[3] + lines[4] + lines[5]
                else:
                    self.stPeteReport = lines[1] + lines[2]
            elif self.name == "Encampment River":
                self.stPeteReport = lines[2] + lines[3]
            #elif self.name == "Upper North Platte":
            #    self.stPeteReport = lines[1]
            elif self.name == "Gray Reef River" or self.name == "Rocky Mountain National Park" or self.name == "Laramie":
                if self.name == "Gray Reef River" or self.name == "Rocky Mountain National Park":
                    self.stPeteReport = lines[2] + lines[3] + lines[4]
                else:
                    self.stPeteReport = lines[3] + lines[4]
            elif self.name == "Stillwater":
                self.stPeteReport = lines[0] + lines[1] + lines[2] + lines[3]


    def getRocky(self):
        rockyCredit = "<p class='credit'>Report courtesy of <a href='http://www.rockymtanglers.com/'>Rocky Mountain Anglers</a> in Boulder, Colorado.</p>"

        url = "http://www.rockymtanglers.com/" + self.rockyLink + ".riv"
        html = urllib.urlopen(url).read()
        soup = BeautifulSoup(html, 'html.parser')
        report = soup.find_all('span', {"class":"report"})

        lines = [span.get_text() for span in report]
        self.rockyReport = lines[-1]
        #return render_template('rivers.html', river = riverName, report = lines[0])

    def getTrouts(self):
        troutsCredit = "<p class='credit'>Report courtesy of <a href='https://troutsflyfishing.com/'>Trouts Fly Fishing</a> in Denver, Colorado.</p>"

        url = "https://troutsflyfishing.com/info/fishing-information/" + self.troutsLink
        html = urllib.urlopen(url).read()
        soup = BeautifulSoup(html, 'html.parser')
        report = soup.select('.update_text p')
        lines = [span.get_text() for span in report]

        self.troutsReport = lines[-1]

@app.route('/arkansas_river_msg', methods=['POST'])
def submit_message_ark():
  message = {
    'body': request.form['message'],
    'who': request.form['who']
  }
  firebase.post('/arkansas_river', message)
  return redirect(url_for('arkData'))

ark = River("Arkansas River", "", "Arkansas_River", "lower-arkansas-river")
ark.getRocky()
ark.getTrouts()
@app.route("/arkansas_river")
def arkData():
    result = firebase.get('/arkansas_river', None)
    return render_template('rivers.html', river = ark.name, rockyMtnReport = ark.rockyReport, troutsReport = ark.troutsReport, messages=result)

@app.route('/bear_crk_msg', methods=['POST'])
def submit_message_bear():
  message = {
    'body': request.form['message'],
    'who': request.form['who']
  }
  firebase.post('/bear_creek', message)
  return redirect(url_for('bearData'))

bear = River("Bear Creek", "", "", "bear-creek")
bear.getTrouts()
@app.route("/bear_creek")
def bearData():
    result = firebase.get('/bear_creek', None)
    return render_template('rivers.html', river = bear.name, troutsReport = bear.troutsReport, messages=result)

@app.route('/blue_river_msg', methods=['POST'])
def submit_message_blue():
  message = {
    'body': request.form['message'],
    'who': request.form['who'],
    'time': strftime("%H:%M %m-%d-%Y", gmtime())
  }
  firebase.post('/blue_river', message)
  return redirect(url_for('blueData'))

blue = River("Blue River", "", "Blue_River", "blue-river-at-silverthorne")
blue.getRocky()
blue.getTrouts()
@app.route("/blue_river")
def blueData():
    result = firebase.get('/blue_river', None)
    return render_template('rivers.html', river = blue.name, rockyMtnReport = blue.rockyReport, troutsReport = blue.troutsReport, messages=result)

@app.route('/messages')
def messages():
  result = firebase.get('/messages', None)
  return render_template('list.html', messages=result)

@app.route('/boulder_creek_msg', methods=['POST'])
def submit_message():
  message = {
    'body': request.form['message'],
    'who': request.form['who']
  }
  firebase.post('/boulder_creek', message)
  return redirect(url_for('boulderCrkData'))

boulderCrk = River("Boulder Creek", "", "Boulder_Creek", "")
boulderCrk.getRocky()
@app.route("/boulder_creek")
def boulderCrkData():
    result = firebase.get('/boulder_creek', None)
    return render_template('rivers.html', river = boulderCrk.name, rockyMtnReport = boulderCrk.rockyReport, messages=result)

@app.route('/big_thompson_river_msg', methods=['POST'])
def submit_message_big_t():
  message = {
    'body': request.form['message'],
    'who': request.form['who']
  }
  firebase.post('/big_thompson_river', message)
  return redirect(url_for('bigTData'))

bigT = River("Big Thompson River", "Big-Thompson", "Big_Thompson_River", "")
bigT.getStPete()
bigT.getRocky()
@app.route("/big_thompson_river")
def bigTData():
    result = firebase.get('/big_thompson_river', None)
    return render_template('rivers.html', river = bigT.name, rockyMtnReport = bigT.rockyReport, stPeteReport = bigT.stPeteReport, messages=result)

@app.route('/clear_creek_msg', methods=['POST'])
def submit_message_clear_creek():
  message = {
    'body': request.form['message'],
    'who': request.form['who']
  }
  firebase.post('/clear_creek', message)
  return redirect(url_for('clearCrkData'))

clearCrk = River("Clear Creek", "", "Clear_Creek", "clear-creek")
clearCrk.getRocky()
clearCrk.getTrouts()
@app.route("/clear_creek")
def clearCrkData():
    result = firebase.get('/clear_creek', None)
    return render_template('rivers.html', river = clearCrk.name, rockyMtnReport = clearCrk.rockyReport, troutsReport = clearCrk.troutsReport, messages=result)

@app.route('/colorado_river_msg', methods=['POST'])
def submit_message_colorado():
  message = {
    'body': request.form['message'],
    'who': request.form['who']
  }
  firebase.post('/colorado_river', message)
  return redirect(url_for('coloradoData'))

colorado = River("Colorado River", "", "Colorado_River", "middle-colorado-river")
colorado.getRocky()
colorado.getTrouts()
@app.route("/colorado_river")
def coloradoData():
    result = firebase.get('/colorado_river', None)
    return render_template('rivers.html', river = colorado.name, rockyMtnReport = colorado.rockyReport, troutsReport = colorado.troutsReport, messages=result)

@app.route('/eagle_river_msg', methods=['POST'])
def submit_message_eagle():
  message = {
    'body': request.form['message'],
    'who': request.form['who']
  }
  firebase.post('/eagle_river', message)
  return redirect(url_for('eagleData'))

eagle = River("Eagle River", "", "", "eagle-river")
eagle.getTrouts()
@app.route("/eagle_river")
def eagleData():
    result = firebase.get('/eagle_river', None)
    return render_template('rivers.html', river = eagle.name, troutsReport = eagle.troutsReport, messages=result)

@app.route('/encampment_river_msg', methods=['POST'])
def submit_message_encampment():
  message = {
    'body': request.form['message'],
    'who': request.form['who']
  }
  firebase.post('/encampment_river', message)
  return redirect(url_for('encampmentData'))

encampment = River("Encampment River", "encampment", "", "")
encampment.getStPete()
@app.route("/encampment_river")
def encampmentData():
    result = firebase.get('/encampment_river', None)
    return render_template('rivers.html', river = encampment.name, stPeteReport = encampment.stPeteReport, messages=result)

@app.route('/fraser_river_msg', methods=['POST'])
def submit_message_fraser():
  message = {
    'body': request.form['message'],
    'who': request.form['who']
  }
  firebase.post('/fraser_river', message)
  return redirect(url_for('fraserData'))

fraser = River("Fraser River", "", "", "frasier-river")
fraser.getTrouts()
@app.route("/fraser_river")
def fraserData():
    result = firebase.get('/fraser_river', None)
    return render_template('rivers.html', river = fraser.name, troutsReport = fraser.troutsReport, messages=result)

@app.route('/frying_pan_river_msg', methods=['POST'])
def submit_message_frying_pan():
  message = {
    'body': request.form['message'],
    'who': request.form['who']
  }
  firebase.post('/frying_pan_river', message)
  return redirect(url_for('fryingpanData'))

fryingpan = River("Fryingpan River", "", "Fryingpan_River", "")
fryingpan.getRocky()
@app.route("/frying_pan_river")
def fryingpanData():
    result = firebase.get('/frying_pan_river', None)
    return render_template('rivers.html', river = fryingpan.name, rockyMtnReport = fryingpan.rockyReport, messages=result)

@app.route('/gray_reef_river_msg', methods=['POST'])
def submit_message_gray_reef_river():
  message = {
    'body': request.form['message'],
    'who': request.form['who']
  }
  firebase.post('/gray_reef_river', message)
  return redirect(url_for('grayReefData'))

grayReef = River("Gray Reef River", "gray-reef", "", "")
grayReef.getStPete()
@app.route("/gray_reef_river")
def grayReefData():
    result = firebase.get('/gray_reef_river', None)
    return render_template('rivers.html', river = grayReef.name, stPeteReport = grayReef.stPeteReport, messages=result)

@app.route('/gunnison_taylor_river_msg', methods=['POST'])
def submit_message_gunnison_taylor_river():
  message = {
    'body': request.form['message'],
    'who': request.form['who']
  }
  firebase.post('/gunnison_taylor_river', message)
  return redirect(url_for('gunnisonData'))

gunnison = River("Gunnison Taylor River", "", "Gunnison_Taylor_River", "")
gunnison.getRocky()
@app.route("/gunnison_taylor_river")
def gunnisonData():
    result = firebase.get('/gunnison_taylor_river', None)
    return render_template('rivers.html', river = gunnison.name, rockyMtnReport = gunnison.rockyReport, messages=result)

@app.route('/laramie_river_msg', methods=['POST'])
def submit_message_laramie_river():
  message = {
    'body': request.form['message'],
    'who': request.form['who']
  }
  firebase.post('/laramie_river', message)
  return redirect(url_for('laramieData'))

laramie = River("Laramie", "laramie", "", "")
laramie.getStPete()
@app.route("/laramie_river")
def laramieData():
    result = firebase.get('/laramie_river', None)
    return render_template('rivers.html', river = laramie.name, stPeteReport = laramie.stPeteReport, messages=result)

@app.route('/poudre_river_msg', methods=['POST'])
def submit_message_poudre_river():
  message = {
    'body': request.form['message'],
    'who': request.form['who']
  }
  firebase.post('/poudre_river', message)
  return redirect(url_for('poudreData'))

poudre = River("Cache La Poudre River", "cache-la-poudre", "Cache_La_Poudre_River", "")
poudre.getStPete()
poudre.getRocky()
@app.route("/poudre_river")
def poudreData():
    result = firebase.get('/poudre_river', None)
    return render_template('rivers.html', river = poudre.name, rockyMtnReport = poudre.rockyReport, stPeteReport = poudre.stPeteReport, messages=result)

@app.route('/north_platte_river_msg', methods=['POST'])
def submit_message_north_platte_river():
  message = {
    'body': request.form['message'],
    'who': request.form['who']
  }
  firebase.post('/north_platte_river', message)
  return redirect(url_for('nPlatteData'))

nPlatte = River("Upper North Platte", "upper-north-platte", "North_Platte_River", "")
nPlatte.getStPete()
nPlatte.getRocky()
@app.route("/north_platte_river")
def nPlatteData():
    result = firebase.get('/north_platte_river', None)
    return render_template('rivers.html', river = nPlatte.name, rockyMtnReport = nPlatte.rockyReport, stPeteReport = nPlatte.stPeteReport, messages=result)

@app.route('/roaring_fork_river_msg', methods=['POST'])
def submit_message_roaring_fork_river():
  message = {
    'body': request.form['message'],
    'who': request.form['who']
  }
  firebase.post('/roaring_fork_river', message)
  return redirect(url_for('roaringForkData'))

roaringFork = River("Roaring Fork River", "", "Roaring_Fork_River", "roaring-fork-river")
roaringFork.getRocky()
roaringFork.getTrouts()
@app.route("/roaring_fork_river")
def roaringForkData():
    result = firebase.get('/roaring_fork_river', None)
    return render_template('rivers.html', river = roaringFork.name, rockyMtnReport = roaringFork.rockyReport, troutsReport = roaringFork.troutsReport, messages=result)

@app.route('/rocky_mtn_nat_park_msg', methods=['POST'])
def submit_message_rocky_mtn_nat_park():
  message = {
    'body': request.form['message'],
    'who': request.form['who']
  }
  firebase.post('/rocky_mtn_nat_park', message)
  return redirect(url_for('rockyData'))

rocky = River("Rocky Mountain National Park", "rocky-mountain-national-park", "Rocky_Mtn_Nat_Park", "")
rocky.getStPete()
rocky.getRocky()
@app.route("/rocky_mtn_nat_park")
def rockyData():
    result = firebase.get('/rocky_mtn_nat_park', None)
    return render_template('rivers.html', river = rocky.name, rockyMtnReport = rocky.rockyReport, stPeteReport = rocky.stPeteReport, messages=result)

@app.route('/saint_vrain_river_msg', methods=['POST'])
def submit_message_saint_vrain_river():
  message = {
    'body': request.form['message'],
    'who': request.form['who']
  }
  firebase.post('/saint_vrain_river', message)
  return redirect(url_for('stVrainData'))

stVrain = River("Saint Vrain River", "", "Saint_Vrain_River", "")
stVrain.getRocky()
@app.route("/saint_vrain_river")
def stVrainData():
    result = firebase.get('/saint_vrain_river', None)
    return render_template('rivers.html', river = stVrain.name, rockyMtnReport = stVrain.rockyReport, messages=result)

@app.route('/south_boulder_creek_msg', methods=['POST'])
def submit_message_south_boulder_creek():
  message = {
    'body': request.form['message'],
    'who': request.form['who']
  }
  firebase.post('/south_boulder_creek', message)
  return redirect(url_for('sBoulderCrkData'))

sBoulderCrk = River("South Boulder Creek", "", "South_Boulder_Creek", "")
sBoulderCrk.getRocky()
@app.route("/south_boulder_creek")
def sBoulderCrkData():
    result = firebase.get('/south_boulder_creek', None)
    return render_template('rivers.html', river = sBoulderCrk.name, rockyMtnReport = sBoulderCrk.rockyReport, messages=result)

@app.route('/south_platte_river_msg', methods=['POST'])
def submit_message_south_platte_river():
  message = {
    'body': request.form['message'],
    'who': request.form['who']
  }
  firebase.post('/south_platte_river', message)
  return redirect(url_for('sPlatteData'))

sPlatte = River("South Platte River", "", "South_Platte_River", "south-platte-river-dream-stream")
sPlatte.getRocky()
sPlatte.getTrouts()
@app.route("/south_platte_river")
def sPlatteData():
    result = firebase.get('/south_platte_river', None)
    return render_template('rivers.html', river = sPlatte.name, rockyMtnReport = sPlatte.rockyReport, troutsReport = sPlatte.troutsReport, messages=result)

@app.route('/stillwater_msg', methods=['POST'])
def submit_message_stillwater():
  message = {
    'body': request.form['message'],
    'who': request.form['who']
  }
  firebase.post('/stillwater', message)
  return redirect(url_for('stillwaterData'))

stillwater = River("Stillwater", "stillwaters", "", "")
stillwater.getStPete()
@app.route("/stillwater")
def stillwaterData():
    result = firebase.get('/stillwater', None)
    return render_template('rivers.html', river = stillwater.name, stPeteReport = stillwater.stPeteReport, messages=result)

@app.route('/yampa_river_msg', methods=['POST'])
def submit_message_yampa_river():
  message = {
    'body': request.form['message'],
    'who': request.form['who']
  }
  firebase.post('/yampa_river', message)
  return redirect(url_for('yampaData'))

yampa = River("Yampa River", "", "Yampa_River", "")
yampa.getRocky()
@app.route("/yampa_river")
def yampaData():
    result = firebase.get('/yampa_river', None)
    return render_template('rivers.html', river = yampa.name, rockyMtnReport = yampa.rockyReport, messages=result)

# dynamic route
@app.route("/test/<search_query>")
def search(search_query):
    return search_query

if __name__ == '__main__':
    app.run(host="0.0.0.0", debug = True, port=5000)


#big t: 4 5 6
#poudre: 3 4 5 6
#upper north platte: 1
# rocky : 2
#Gray reef:2 3 4
#encampment: 2
#Laramie: 2
