# ParsingByBS
😸 Парсинг страницы и формирование JSON.

# Задачи:
1. Спарсить страницу.
2. Создать объекты из результатов и записать в них:
      Название (только текст, без лишних тегов)
      Ссылку (только урл, ведущий на страницу)
      Описание (текст под ссылкой, без лишних тегов)

3. Сформировать json и записать в файл

Пример:
{
    "Name": "Scrapy | A Fast and Powerful Scraping and Web Crawling ...",
    "Url": "https://scrapy.org/",
    "Description": "pip install scrapy cat > myspider.py <<EOF import scrapy class BlogSpider(scrapy.Spider): name = 'blogspider' start_urls = ['https://blog.scrapinghub.com'] def ..."
}
