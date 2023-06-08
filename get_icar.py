from pickle import NONE
from bs4 import BeautifulSoup
import requests
import requests.exceptions
from urllib.parse import urlsplit
from urllib.parse import urlparse
from collections import deque
from urllib.request import urlopen
import re
import os


makes = ["DS", "GAC", "SERES", "אבארט", "אודי", "אופל", "איווייז", "איווקו", "אינפיניטי", "איסוזו", "אלפא_רומיאו", "אסטון מרטין", "ב.מ.וו", "ביואיק", "בנטלי", "ג'ילי", "גיפ", "ג'נסיס", "גרייט וול", "דאציה", "דודג", "דייהטסו", "האמר", "הונדה", "וולוו", "טויוטה", "טסלה", "יגואר", "יונדאי", "לינקולן", "לנדרובר", "לנציה", "לקסוס", "מאזדה", "מאן", "מזראטי", "מיני", "מיצובישי", "מקסוס", "מרצדס", "ניסאן", "סאאב", "סאיק-MG", "סאנגיונג", "סובארו", "סוזוקי", "סיאט", "סיטרואן", "סמארט", "סקודה", "סקייוול", "פולקסווגן", "פונטיאק", "פורד", "פורשה", "פיאט", "פיג'ו", "פרארי", "קדילאק", "קופרה", "קיה", "קרייזלר", "ראם", "רנו", "שברולט"]
url = 'https://www.icar.co.il/'

icar = 'https://www.icar.co.il/'
scrape = 'https://www.scrapethissite.com'
url = icar
url2 = 'https://data.gov.il/api/3/action/datastore_search?resource_id=142afde2-6228-49f9-8a29-9b6c3a0cbe40'
urls = []
urls.append(icar)
filter = ["Prime", "מבחני", "קטגורית", "ליסינג", "מבצעי", "רכב", "טרייד", "מדריכים", "compare", "Landing", "Terms", "faq", "market", "Adv", "בטיחות", "sections", "מימון", "search", "instagram", "About", "contact","קטגורית_רכב",'קטגורית_רכב_יד_שניה']
def check(link):
    checklist = ["Prime", "מבחני", "קטגורית", "ליסינג", "מבצעי", "רכב", "טרייד", "מדריכים", "compare", "Landing", "car", "Terms", "faq", "market", "Adv", "בטיחות", "sections", "מימון", "search", "instagram", "About", "contact","קטגורית_רכב",'קטגורית_רכב_יד_שניה']
    if link in checklist:
        return True
    else:
        return False
'''file_size = []
file_list = [make + '.txt' for make in makes]

for file in file_list:
    with open (file, 'r') as files:
        file_size.append(os.path.getsize(file))
            
make_dict = dict(zip(makes,file_list))
file_dict = dict(zip(file_list,file_size))'''




def crawl(urls, make):
    filtered_urls = []

    m = 'https://www.icar.co.il/ליסינג/'
    m2 = '/קטגורית_רכב/מכוניות_קטנות/'

    processing_list = []
    # a queue of urls to be crawled next
    new_urls = deque(urls)
    # a set of urls that we have already processed 
    processed_urls = set()

    # a set of domains inside the target website
    local_urls = set()

    # a set of domains outside the target website
    foreign_urls = set()

    # a set of broken urls
    broken_urls = set()


    url_list = []
        

    # process urls one by one until we exhaust the queue
    while len(new_urls):
        # move url from the queue to processed url set
        url = new_urls.popleft()
        if url.find('version') > 0:
            url_list.append(url+'\n')
        
        """  if url.find('version') > 0:
            if url.find('#') < 0:
           
                url_list.append(url) """
        processed_urls.add(url)
        # print the current url
        try:
            response = requests.get(url)
        except(requests.exceptions.MissingSchema, requests.exceptions.ConnectionError, requests.exceptions.InvalidURL, requests.exceptions.InvalidSchema):
            # add broken urls to it’s own set, then continue
            broken_urls.add(url)
            continue
        # extract base url to resolve relative links
        parts = urlsplit(url)
        base = '{0.netloc}'.format(parts)
        strip_base = base.replace('www.', '')
        base_url = '{0.scheme}://{0.netloc}'.format(parts)
        path = url[:url.rfind('/')+1] if '/' in parts.path else url
           
        #Initialize beautiful soup
        soup = BeautifulSoup(response.text, 'lxml')


        for link in soup.find_all('a',{'href':re.compile('/'+ make + '/' + make + '.+/')}): 
            #url in soup.find_all('a')     original
            compiler = '/' + make + '.+/' + make + '.+/'
            s = soup.find_all(['a','href'])
            r = soup.find_all('a',{'href':re.compile('/'+ make + '/' + make + '.+/')})
            a = "/DS/DS_3/"
            a = '/DS+(?=")'
            # extract url url from the anchor
            anchor = link.attrs['href'] if 'href' in link.attrs else ''
            if anchor.startswith('/'):
                local_link = base_url + anchor
                local_urls.add(local_link)
            elif strip_base in anchor:
                local_urls.add(anchor)
            elif not anchor.startswith('http'):
                local_link = path + anchor
                local_urls.add(local_link)
            else:
                foreign_urls.add(anchor)


        for link in local_urls:
            if re.search(make,link): 
                filtered_urls.append(link)
     
        local_urls = set(filtered_urls) 
        for i in local_urls:
            if not i in new_urls and not i in processed_urls:
                new_urls.append(i)
        #url_sets.add(new_urls)

        a = []
        a.append(new_urls)
        
    
        
 

    b=5



    return url_list


#ds = 'https://www.icar.co.il/DS/'
#urls = [ds]
#versions = crawl(urls,"DS/")
#w = open("אלפא רומיאו.txt",'w+',encoding='utf-8')





#makes = ['אלפא רומיאו', 'ב.מ.וו', 'גיפ', 'גרייט וול', 'דאציה', 'דודג']
icar_url = 'https://www.icar.co.il/'    
urls = []        
makes = ["פיג'ו"]

url = 'https://www.icar.co.il/%D7%90%D7%95%D7%A4%D7%9C/'
moo = crawl(url, 'אופל')

for make in makes:
    car_url = [icar_url+make+'/']
    #file_size = os.path.getsize(make_dict[make])
    #if file_size > 0:
    #    pass
    versions = crawl(car_url,make)
    file_name = make + '.txt'
    file = open(make_dict[make],'w',encoding='utf-8')
    file.writelines(versions)
    file.close()
    b=5

    #for line in versions:
    #    file.write(line)
    #file.close()




#step1 = crawl(urls, make)

#step2 = crawl(step1, make)


#step3 = crawl(step2, 'version')





#a = crawl(url, make)







b=5

