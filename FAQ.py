# from requests_html import HTMLSession
# session = HTMLSession()

# url = 'https://en.wikipedia.org/wiki/FAQ'

# with session.get(url) as r:

#     paragraph = r.html.find(selector, first=False)

#     text = " ".join([ p.text for p in paragraph])

from bs4 import BeautifulSoup
import requests

page = requests.get("https://community.fiverr.com/forums/forum/28-fiverr-faq/")
page
soup = BeautifulSoup(page.content, 'html.parser')

f = open("demofile2.html", "a")
f.write(soup.prettify())
f.close()

print(soup.prettify())