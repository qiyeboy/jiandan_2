# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html
import os
import urllib
import scrapy
from scrapy.exceptions import DropItem
from scrapy.pipelines.images import ImagesPipeline

from jiandan import settings

class JiandanPipeline(ImagesPipeline):#继承ImagesPipeline这个类，实现这个功能

    def get_media_requests(self, item, info):#重写ImagesPipeline   get_media_requests方法


        '''
        :param item:
        :param info:
        :return:
        在工作流程中可以看到，
        管道会得到文件的URL并从项目中下载。
        为了这么做，你需要重写 get_media_requests() 方法，
        并对各个图片URL返回一个Request:
        '''
        spiderName = self.spiderinfo.spider.name
        if spiderName == 'jiandan':
            for image_url in item['image_urls']:
                yield scrapy.Request(image_url)
        else:
            super(JiandanPipeline, self).get_media_requests(item, info)


    def item_completed(self, results, item, info):
        '''

        :param results:
        :param item:
        :param info:
        :return:
        当一个单独项目中的所有图片请求完成时（要么完成下载，要么因为某种原因下载失败），
         item_completed() 方法将被调用。
        '''
        spiderName = self.spiderinfo.spider.name
        if spiderName == 'jiandan':
            image_paths = [x['path'] for ok, x in results if ok]
            if not image_paths:
                raise DropItem("Item contains no images")
            return item




