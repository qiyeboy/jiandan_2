#coding:utf-8
import socket
import urllib

'''
这个类主要是用来检测代理的可用性
'''
class Detect_Proxy(object):

    url = 'http://ip.chinaz.com/getip.aspx'
    def __init__(self,db_helper):
        self.db_helper = db_helper
        socket.setdefaulttimeout(3)


    def detect(self):
        '''
        http://ip.chinaz.com/getip.aspx  作为检测目标
        :return:
        '''
        proxys = self.db_helper.proxys.find()
        badNum = 0
        goodNum = 0
        for proxy in proxys:
            ip = proxy['ip']
            port = proxy['port']
            try:
                proxy_host ="http://ha:ha@"+ip+':'+port #随便添加了账户名和密码，只是为了防止填写账户名密码暂停的情况
                response = urllib.urlopen(self.url,proxies={"http":proxy_host})
                if response.getcode()!=200:
                    self.db_helper.delete({'ip':ip,'port':port})
                    badNum += 1
                    print proxy_host,'bad proxy'
                else:
                    goodNum += 1
                    print proxy_host,'success proxy'

            except Exception,e:
                print proxy_host,'bad proxy'
                self.db_helper.delete({'ip':ip,'port':port})
                badNum += 1
                continue

        print 'success proxy num : ',goodNum
        print 'bad proxy num : ',badNum











