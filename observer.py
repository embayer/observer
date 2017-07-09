#!/usr/bin/env python

'''

'''
import json
import requests


class HackerNewsSrc:
    url_topstories = 'https://hacker-news.firebaseio.com/v0/topstories.json'
    url_story = 'https://hacker-news.firebaseio.com/v0/item/{}.json'

    def __init__(self):
        pass

    def get_stories(self):
        item_ids = self.fetch_item_ids()
        stories = self.fetch_items(item_ids)
        return stories

    def fetch_item_ids(self):
        response = requests.get(self.url_topstories)
        item_ids = []
        if response.ok:
            item_ids = response.json()
        return item_ids

    def fetch_items(self, item_ids):
        items = []
        for item_id in item_ids:
            if len(items) > 9:
                break
            item_url = self.url_story.format(item_id)
            print(item_url)
            response = requests.get(item_url)
            if response.ok:
                item = response.json()
                items.append(item)
        return items


if __name__ == '__main__':
    hns = HackerNewsSrc()
    stories = hns.get_stories()
    for story in stories:
        print(json.dumps(story))
