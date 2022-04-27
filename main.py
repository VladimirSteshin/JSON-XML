import json
import xml.etree.ElementTree as ET
import collections
from pprint import pprint


def counting_words_json(path, words_len, top):
    with open(path, encoding='UTF-8') as file:
        work = json.load(file)
        words_list = []
        for news in work['rss']['channel']['items']:
            description = [word for word in news['description'].split() if len(word) > words_len]
            words_list.extend(description)
            top_counter = collections.Counter(words_list)
        pprint(top_counter.most_common(top))


def counting_words_xml(path, words_len, top):
    parser = ET.XMLParser(encoding='UTF-8')
    work = ET.parse(path, parser)
    root = work.getroot()
    items = root.findall('channel/item')
    news_list = []
    for news in items:
        text = news.find('description').text.split()
        merge = [word for word in text if len(word) > words_len]
        news_list.extend(merge)
    counter = collections.Counter(news_list)
    pprint(counter.most_common(top))


counting_words_json('newsafr.json', 6, 10)
counting_words_xml('newsafr.xml', 6, 10)
