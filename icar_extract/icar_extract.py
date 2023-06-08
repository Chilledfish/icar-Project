from bs4 import BeautifulSoup
import requests
import requests.exceptions
from urllib.parse import urlsplit
from urllib.parse import urlparse
from collections import deque

processing_list = []

a = ['a']
url = "https://www.scrapethissite.com"
c = 'moo'
a.clear()
#url = url_list

a.append['d']


# a queue of urls to be crawled next
new_urls = deque(url)

# a set of urls that we have already processed 
processed_urls = set()

# a set of domains inside the target website
local_urls = set()

# a set of domains outside the target website
foreign_urls = set()

# a set of broken urls
broken_urls = set()

# process urls one by one until we exhaust the queue
while len(new_urls):
    # move url from the queue to processed url set
    url = new_urls.popleft()
    processed_urls.add(url)
    # print the current url
    #processing_list.append(“Processing %s” % url)

