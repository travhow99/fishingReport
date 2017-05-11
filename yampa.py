import urllib
from bs4 import BeautifulSoup

url = "http://www.rockymtanglers.com/Yampa_River.riv"
html = urllib.urlopen(url).read()
soup = BeautifulSoup(html, 'html.parser')

# kill all script and style elements
for script in soup(["script", "style"]):
    script.extract()    # rip it out

# get text
text = soup.get_text()

# break into lines and remove leading and trailing space on each
lines = (line.strip() for line in text.splitlines())
# break multi-headlines into a line each
chunks = (phrase.strip() for line in lines for phrase in line.split("  "))
# drop blank lines
text = '\n'.join(chunk for chunk in chunks if chunk)

#print(text)

#soup.select("#flex_1_scrollwrapper")
divList = soup.findAll('title')
div = soup.findAll('div', attrs={'id': 'flex__1_contentwrapper'})
#print div
#print str(div)
#for row in soup.find_all('div', attrs={'id': 'flex__1_contentwrapper'}):
#    print row.text

report = soup.find_all('span', {"class":"report"})

lines = [span.get_text() for span in report]

print lines[-1]
