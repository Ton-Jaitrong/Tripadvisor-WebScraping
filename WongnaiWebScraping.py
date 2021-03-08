import requests
from bs4 import BeautifulSoup

r = requests.get("https://www.wongnai.com/restaurants/sushimasa")
r.encoding = "utf-8"
# print(r.text)

html_page = BeautifulSoup(r.text, "html.parser")
# print(html_page)
# print(type(html_page))
# print(html_page.prettify())

selector = 'span.sc-1kh6w3g-1.ghCbHF'
price = html_page.select_one(selector)
# print(type(price))
# print(price.text)

picture_selector = 'img.epawmp-0.cWzaZM'
pic = html_page.select(picture_selector)
print(pic)

for image in pic:
    print(image["src"]) #src = source