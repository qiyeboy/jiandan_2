#coding:utf-8
#需要安装pillow模块
import scrapy
from jiandan.items import JiandanItem

from scrapy.crawler import CrawlerProcess

class jiandanSpider(scrapy.Spider):
    name = 'jiandan'
    allowed_domains = []
    new_url=None
    start_urls = ["http://jandan.net/ooxx"]
    headers={
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
        'Accept-Language': 'en',
        'Referer':'http://jandan.net/ooxx'

    }


    def parse(self, response):

        item = JiandanItem()
        item['image_urls'] = response.xpath('//img//@src').extract()#提取图片链接
        # print 'image_urls',item['image_urls']
        yield item
        if self.new_url !=None:
            self.headers['Referer']= self.new_url
        self.new_url= response.xpath('//a[@class="previous-comment-page"]//@href').extract_first()#翻页
        print '----new_url---',self.new_url
        if self.new_url:
            yield scrapy.Request(self.new_url,headers=self.headers,callback=self.parse)




