import requests
from bs4 import BeautifulSoup
import mysql.connector

def replace_special_characters(msg):
    replaced = msg
    replaced = replaced.replace('\'', '')
    return replaced

conn = mysql.connector.connect(user='root', password='',host='127.0.0.1',database='forums')

comm = "SELECT url FROM topic WHERE is_replies=0"
cursor = conn.cursor()
cursor.execute(comm)
data = cursor.fetchall()
conn.commit()
conn.close()

for r in data:
    url = "https://www.tripadvisor.com" + r[0]
    # print(url)

    r = requests.get(url)
    r.encoding = "utf-8"
    html_page = BeautifulSoup(r.text, "html.parser")

    # Find No. Of Pages
    selector = 'a.paging.taLnk'
    pages = html_page.select(selector)
    pages = int(len(pages)/2)

    url_list = list()
    url_list.append(url)

    if pages >= 1:
        for i in range(1, pages+1):
            url_split = url.split("-")
            url_page = url_split[0]+"-"+url_split[1]+"-"+url_split[2]+"-"+url_split[3]+"-o"+str(i*10)+"-"+url_split[4]+"-"+url_split[5]
            url_list.append(url_page)

    print(url_list)

        