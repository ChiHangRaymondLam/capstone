import requests
from bs4 import BeautifulSoup
import random


def scrape_information(url):
	response = requests.get(url)
	
    # Create a BeautifulSoup objet from the HTML
	soup = BeautifulSoup(response.content, 'html.parser')

	title = soup.find(id="firstHeading")
	print(title.text)

    # Find all the a tags under id is bodyContent
	allLinks = soup.find(id="bodyContent").find_all("a")
	random.shuffle(allLinks)
	link_to_scrape = 0

	for link in allLinks:
		# Scrape the wiki articles only
		if link['href'].find("/wiki/") == -1: 
			continue

		# Use this link to scrape
		link_to_scrape = link
		break

	scrape_information("https://en.wikipedia.org" + link_to_scrape['href'])

scrape_information("https://en.wikipedia.org/wiki/Supply_chain_management")