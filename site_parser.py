import re
from bs4 import BeautifulSoup
import urllib.request

def get_links():
    html_page = urllib.request.urlopen("http://sphk.ru/raspisanie-zanyatij/")
    soup = BeautifulSoup(html_page, "html.parser")

    for link in soup.findAll('a', attrs={'href': re.compile("^https://docs.google.com/document/d/")}):
        zameni = link.get('href')
    for link in soup.findAll('a', attrs={'href': re.compile("^https://docs.google.com/spreadsheets/d/")}):
        raspisanie = link.get('href')
    
    return zameni, raspisanie

def get_id():
    zameni, raspisanie = get_links()
    zameni = zameni[zameni.find('d/')+2:zameni.find('/edit')]
    raspisanie = raspisanie[raspisanie.find('d/')+2:raspisanie.find('/edit')]
    return zameni, raspisanie

if __name__ == "__main__":
    zameni, raspisanie = get_id()
    print(zameni, raspisanie)