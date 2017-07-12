import urllib
from bs4 import BeautifulSoup

url = "https://troutsflyfishing.com/info/fishing-information/frasier-river"
html = urllib.urlopen(url).read()
soup = BeautifulSoup(html, 'html.parser')
report = soup.select('.update_text p')
lines = [span.get_text() for span in report]

print lines[-1]
