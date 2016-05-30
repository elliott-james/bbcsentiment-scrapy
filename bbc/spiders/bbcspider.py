from scrapy.selector import Selector
from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors.sgml import SgmlLinkExtractor
from bbc.items import BbcItem
import re

class BbcSpider (CrawlSpider) :
  handle_httpstatus_list = [302]
  name = "bbcs"
  allowed_domains = ["bbc.com"]
  start_urls = ['http://www.bbc.com/news/']

  rules = (
        Rule(SgmlLinkExtractor(allow="bbc.com/news"), callback="parse_item", follow=True),)
  
  def parse_item(self, response) :
    sel = Selector (response)
    item = BbcItem ()
    item['URL'] = response.request.url
    print response.request.url
    item['text'] = sel.xpath('//div[@class="story-body__inner"]/p/text()').extract()
    item['heading'] = sel.xpath('//h1[@class="story-body__h1"]/text()').extract()
    item['image'] = sel.xpath('//div[@class="js-delayed-image-load"]/@data-src').extract()
    item['link_external'] = sel.xpath('//a[@class="story-body__link-external"]/@href').extract()
    item['link_internal'] = sel.xpath('//a[@class="story-body__link"]/@href').extract()
    return item