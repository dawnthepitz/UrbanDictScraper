import requests

from bs4 import BeautifulSoup   

def urbanscrape(word):
    r =         requests.get("http://www.urbandictionary.com/define.php?term={}".format(word))

    soup = BeautifulSoup(r.content)
    print("<h1>",format(word),
    "</h1>\n")
    
    for definition in soup.find_all("div",attrs={"class":"meaning"}):
        print("<p class=\"",format(word),"\">",definition.text,"</p>")