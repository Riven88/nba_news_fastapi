import requests
from bs4 import BeautifulSoup
import sqlite3

def get_feature_news():
    nba_web = "https://tw-nba.udn.com/nba/index"
    response = requests.get(nba_web)
    html_structure = BeautifulSoup(response.text, "html.parser")

    #網站HTML裡新聞標題位於 li class="splide__slide"
    feature_news_section = html_structure.find_all("li", class_="splide__slide") 

    news_list = []

    for section in feature_news_section:
        #標題文字在 /a herf/h1底下
        a_tag = section.find("a")
        h1_tag = section.find("h1")

        if a_tag and h1_tag:
            title = h1_tag.text.strip()
            link = a_tag["href"]
            
            news_list.append((title, link))

    return news_list

def save_to_db(news_list):
    conn = sqlite3.connect("nba_news.db")
    c = conn.cursor()
    c.execute('''
        CREATE TABLE IF NOT EXISTS news (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            title TEXT,
            url TEXT
        )
    ''')

    c.execute("DELETE FROM news")
    c.executemany("INSERT INTO news (title, url) VALUES (?, ?)", news_list)
    conn.commit()
    conn.close()

if __name__ == "__main__":
    news_list = get_feature_news()
    save_to_db(news_list)
    print("news saved into DB")