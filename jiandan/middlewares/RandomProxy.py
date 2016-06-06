#coding:utf-8
import random
from jiandan import settings
from jiandan.db.db_helper import DB_Helper

'''
这个类主要用于产生随机代理
'''
class RandomProxy(object):


    def __init__(self):#初始化一下数据库连接
        self.db_helper = DB_Helper()
        self.count =self.db_helper.proxys.count()

    def process_request(self, request, spider):
        '''
        在请求上添加代理
        :param request:
        :param spider:
        :return:
        '''
        # idList = range(1,self.count+1)
        # id = random.choice(idList)
        # result = self.db_helper.findOneResult({'proxyId':id})
        request.meta['proxy'] =settings.HTTP_PROXY

