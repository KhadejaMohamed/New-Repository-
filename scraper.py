import requests
from bs4 import BeautifulSoup
import random



def scrapeWikiArtcile(url):


    response = requests.get(
    url = url,
    )

    soup = BeautifulSoup(response.content, 'html.parser')

    title = soup.find(id="firstHeading")

    print(title.string)

    #get all the links

    allLinks = soup.find(id="bodyContent").find_all('a')
    random.shuffle(allLinks)
    linktoScrape = 0

    for link in allLinks:
        #we are only interested in other wiki articles
        if link['href'].find("/wiki/") == -1:
            continue

        # use this link to scrape
        linktoScrape = link
        break

    print(linktoScrape)

    scrapeWikiArtcile("https://en.wikipedia.org" + linktoScrape['href'])

scrapeWikiArtcile("https://en.wikipedia.org/wiki/Web_scraping")

