from bbc.settings import MIN_ARTICLE_LENGTH
from scrapy.exceptions import DropItem
from textblob import TextBlob
from goose import Goose
import re

class BbcPipeline(object):
    def process_item(self, item, spider):
        return item

class DropShortArticlesPipeline(object):
    def process_item(self, item, spider):
        if len(item["text"]) < MIN_ARTICLE_LENGTH:
            raise DropItem("Article text is too short.")

        return item
    
class ExtractArticlePipeline(object):
    def __init__(self):
        self.goose = Goose()

    def process_item(self, item, spider):
        try:
            article = item["text"]
            item["text"] = article.cleaned_text

        except IndexError:
            raise DropItem("Failed to extract article text")

        return item

class SentimentPipeline(object):
    def process_item(self, item, spider):
        blob = TextBlob(item["text"])
        item["sentiment"] = blob.sentiment.polarity
        return item
