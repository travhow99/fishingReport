import requests, bs4
res = requests.get('http://www.rockymtanglers.com/Boulder_Creek.riv?station=1#target')
res.raise_for_status()
noStarchSoup = bs4.BeautifulSoup(res.text)
type(noStarchSoup)
