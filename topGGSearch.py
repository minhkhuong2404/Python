import requests, webbrowser, bs4, sys

print('Goolging...') #display text while downloading the gg page
res = requests.get('https://google.com/search?q=' + ''.join(sys.argv[1:]))

# open a specific website
# res = 'https://google.com/search?q=' + ''.join(sys.argv[1])
# chrome_path = 'open -a /Applications/Google\ Chrome.app %s'
# webbrowser.get(chrome_path).open(res)

res.raise_for_status()

#retrieve the top search link
soup = bs4.BeautifulSoup(res.text,"lxml")

#open the browser tab for result
linkElems = soup.select('.r a')
numOpen = min(3,len(linkElems))
for i in range(numOpen):
    webbrowser.open('https://google.com' + linkElems[i].get('href'))
