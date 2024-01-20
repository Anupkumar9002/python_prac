import requests
from bs4 import BeautifulSoup
response=requests.get("https://www.youtube.com/watch?v=Nsb3bLIlO4w&list=PLu0W_9lII9agwh1XjRt242xIpHhPT2llg&index=89")
#print(response.text)
soup=BeautifulSoup(response.text,"html.parser")
#print(soup.prettify())
for heading in soup.find_all("head"):
    print(heading.text)

