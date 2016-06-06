#coding:utf-8
import argparse
from scrapy.crawler import CrawlerProcess
from scrapy.utils.project import get_project_settings



process = CrawlerProcess(get_project_settings())

process.crawl('jiandan')

process.start()


'''
微信公共号 : qiye_python

博客:http://www.cnblogs.com/qiyeboy/

CSDN：http://blog.csdn.net/qiye_/

'''
# if __name__=='__main__':
#     parser = argparse.ArgumentParser(description='Spider jiandan -- blog: http://www.cnblogs.com/qiyeboy/')
#     parser.add_argument("-p","-crawl", nargs="+",help="crawl proxy infor. example : python main.py -c 100 200",
#                     type=int)
#     parser.add_argument("-t","-test", help="check proxy infor. command : python main.y -t db",
#                    )
#     args = parser.parse_args()
#
#     if args.c != None and len(args.c)>1:
#         #这个时候启动 爬虫
#         print 'spider beginning ......'
#
#
#         print 'spider end '
#     elif args.t != None:
#         print 'detect begin ...... '
#
#         print 'detect end  '
