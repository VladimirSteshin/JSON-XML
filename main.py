import json
import collections
from pprint import pprint


def counting_words(path, words_len, top):
    with open(path, encoding='UTF-8') as file:
        work = json.load(file)
        words_list = []
        for news in work['rss']['channel']['items']:
            description = [word for word in news['description'].split() if len(word) > words_len]
            words_list.extend(description)
            top_counter = collections.Counter(words_list)
        pprint(top_counter.most_common(top))


counting_words('newsafr.json', 6, 10)
