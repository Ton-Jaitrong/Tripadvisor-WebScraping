import requests
from bs4 import BeautifulSoup

# https://www.tripadvisor.com/ShowForum-g293920-i5037-Phuket.html
r = requests.get("https://www.tripadvisor.com/ShowForum-g293920-i5037-Phuket.html")
r.encoding = "utf-8"
# print(r.text)

html_page = BeautifulSoup(r.text, "html.parser")
# print(html_page)
# print(type(html_page))
# print(html_page.prettify())

# Pages
page_selector = 'a.paging.taLnk'
pages = html_page.select(page_selector)
# print(pages)
# print(len(pages))
print(pages[len(pages)-1].text)

# for page in pages:
#    print(page.text)

table_selector = 'table.topics'
tables = html_page.select(table_selector)
# print(tables)

row_selector = 'tr'
rows = tables[0].select(row_selector)
# print(rows)
# print(rows[1])

column_selector = 'td'
columns = rows[1].select(column_selector)
# print(columns)
# print(columns[0].text)

# Forum
# print(columns[1].text.strip())

# Topic
topic_selector = 'a'
topics = columns[2].select(topic_selector)
# print(topics)

topic = topics[0].text.strip()
topic_source = topics[0]["href"].strip()
# print(topic)
# print(topic_source)

createdby = topics[1].text.strip()
createdby_source = topics[1]["href"].strip()
# print(createdby)
# print(createdby_source)

# Replies
# print(columns[3].text.strip())

# Last Post
lastpost_selector = 'a'
lastpost = columns[4].select(lastpost_selector)
lastPostat = lastpost[0].text.strip()
lastPostby = lastpost[1].text.strip()
lastPostby_source = lastpost[1]["href"].strip()
# print(lastPostat)
# print(lastPostby)
# print(lastPostby_source)

# replies page1: https://www.tripadvisor.com/ShowTopic-g293920-i5037-k13481785-Phuket_hotels-Phuket.html
# replies page2: https://www.tripadvisor.com/ShowTopic-g293920-i5037-k13481785-o10-Phuket_hotels-Phuket.html
