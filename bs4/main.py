from bs4 import BeautifulSoup
import requests

response = requests.get("https://www.geeksforgeeks.org")
print(response.status_code)
yc_web_page = response.text
print(yc_web_page)

soup = BeautifulSoup(yc_web_page, "html.parser")
article_tag = soup.find(name="div", class_="ant-col")
print(article_tag)





















# with open("website.html", "r", encoding="utf-8") as file:
#     contents = file.read()
#
# soup = BeautifulSoup(contents, "html.parser")
# print(soup.p)
