import requests as rq
from bs4 import BeautifulSoup

#www.youtube.com is used as unit testing
url = "www.youtube.com"
#the url must contain 'https' or 'http' for rq to function
if ("https" or "http") in url:
    data = rq.get(url)
else:
    data = rq.get("https://" + url)

#parse HTML code obtained
#HTML parsing is basically taking in HTML code
#and extracting relevant information
soup = BeautifulSoup(data.text, "html.parser")
links = []

#find all <a> attribute in HTML code with href attribute
#href attribute specifies the URL of the page the link goes to
for link in soup.find_all("a"):
    links.append(link.get("href"))
    print(link.get("href"))
    
#some people use urllib2.urlopen to replace rq
#in this case, the text 'html.parser' will be removed from line 14
#overall both libraries work the same way
