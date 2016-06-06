# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class JiandanItem(scrapy.Item):
    # define the fields for your item here like:
    image_urls = scrapy.Field()#图片的链接
    images = scrapy.Field()



class ProxyItem(scrapy.Item):
    ip = scrapy.Field()#ip
    port = scrapy.Field()#端口


