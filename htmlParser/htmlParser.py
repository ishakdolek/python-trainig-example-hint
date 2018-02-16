import requests
from bs4 import BeautifulSoup

url = "https://www.sorusorcevapbul.com/soru-cevap/hz-muhammed/kainat-hz-muhammedin-asm-hurmetine-mi-yaratildi"

response = requests.get(url)

html_content=response.content

soup=BeautifulSoup(html_content,"html.parser")

# var element_list=soup.find_all("a")

for i in soup.find_all("a"):
    print(i.get("href"))
    print("--------------------------------")
# print(soup.prettify())
