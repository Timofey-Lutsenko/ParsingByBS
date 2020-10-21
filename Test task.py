from bs4 import BeautifulSoup
import requests as req
from classes import Link
import json

# Константы.
TARGET_URL = "https://www.google.com/search?q=scrapy"
HEADERS = {
    "user-Agent": "Mozilla/5.0 (Windows NT 10.0; \n"
                  "Win64; x64; rv:81.0) Gecko/20100101 Firefox/81.0",
    "accept": "text/html,application/xhtml+xml,app\n"
              "lication/xml;q=0.9,image/webp,*/*;q=0.8"
}
HOST = 'https://'


# Функция GET запроса.
def get_html(url, params=None):
    r = req.get(url, headers=HEADERS, params=params)
    return r


# Функция парсинга страницы, переданной из get_html.
def parse():
    html = get_html(TARGET_URL)
    if html.status_code == 200:
        return get_content(html.text)
    else:
        print("Error")


# Функция создания списка экзепляров класса с заданной страницы.
def get_content(html):
    soup = BeautifulSoup(html, "html.parser")
    g_divs = soup.select('div[class="g"]')
    link_list = []
    for item in g_divs:
        desc = item.find("span", class_="aCOpRe").text
        name = item.find("h3", class_="LC20lb").text
        url = HOST + item.find("div", class_="TbwUpd").text
        link_list.append(Link(name, url, desc))
    return link_list


obj_list = parse()
dict_list = []

# Преобразование списка эезкмпляров класса к списку словарей.
for el in obj_list:
    dict_list.append(el.__dict__)

# Создание JSON файла из списка словарей.
with open("data_file.json", "w", encoding="utf-8") as write_file:
    json.dump(dict_list, write_file, ensure_ascii=False, indent=4)
