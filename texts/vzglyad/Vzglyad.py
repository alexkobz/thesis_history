#!/usr/bin/env python
# This Python file uses the following encoding: utf-8
import json
import re
import pandas as pd
from time import sleep
from bs4 import BeautifulSoup
from texts.API import API
from texts.KnownUrls import KnownUrls


class Vzglyad(API):

    def save_urls(self):
        self.mkdir()
        known_urls = KnownUrls(self._url).get_urls()
        pattern = re.compile(r'\S+opinions/\d{4}/\d+/\d+/\d+.html$')
        with open(f'{self._basefolder}\\{self._basefolder}_urls.txt', 'a+') as f:
            for url in known_urls:
                url = url.replace('%20', '').replace('\n', '')
                if pattern.match(url):
                    f.write(url + '\n')
            sleep(1)

    def parse_html(self, sql):
        for file in self.filename():
            with (open(file, encoding='utf-8') as f):
                try:
                    html = f.read()
                    soup = BeautifulSoup(html)
                    author = soup.find(class_="author").img.attrs['title'].replace("'", '`') if soup.find(
                        class_="author") else ''
                    date = soup.find(class_="header").span.text if soup.find(class_="header") else ''
                    url = soup.find(property="og:url").attrs['content'].replace("'", '`') if soup.find(
                        property="og:url") else ''
                    header = soup.find(property="og:title").attrs['content'].replace("'", '`')
                    section = soup.find(property="og:type").attrs['content'].replace("'", '`')
                    text = soup.find(class_="news_text").text
                    sql.execute(
                        f"""INSERT INTO TRANSCRIPTS 
                        (AUTHOR, DDATE, URL, HEADER, SECTION, FILENAME, TRANSCRIPT, SOURCE) 
                        VALUES('{author}', '{date}', '{url}', '{header}', '{section}', '{file}', '{text}', '{10}');"""
                    )
                except:
                    pass

    def cast_date(self, sql):
        df = pd.read_sql("SELECT * FROM TRANSCRIPTS WHERE SOURCE = 10", sql.__CONNECTION)
        df["DDATE"] = pd.to_datetime(df["DDATE"]).dt.tz_localize(None)
        return df
