# -*- coding:utf-8 -*-
from urllib import request
import requests
import time
import re
from queue import Queue
import threading
import globalVal
class Proxy_helper():
    def __init__(self, checkoutThreadMount,collectThreadMount):

        self.checkoutThreadMount=checkoutThreadMount
        self.collectThreadMount=collectThreadMount

    def run(self):
 
        # inip = 'socks5://wocaonimaheheda_dc_1:lt6Cb6jXsFD8PF1W)@proxyus.rola.info:2000'
        # for index in range(20):
        #     self.ip_que.put(inip)
        #     self.validip_que.put(inip)
       
        self.collectUrl_start()
        time.sleep(1)
        
        self.checkout_start()

    def collectUrl_start(self):
        for i in range(self.collectThreadMount):
            worker = threading.Thread(target=self.collectUrl, args=(), name="采集IP线程%d" % (i))
            worker.start()
            print("采集IP线程开启%d" % (i))


    def checkout_start(self):
        for i in range(self.checkoutThreadMount):
            worker = threading.Thread(target=self.checkout_proxy, args=(), name="验证IP线程%d" % (i))
            worker.start()
            print("验证IP线程开启%d" % (i))
        # self.checkout_proxy(self.ip_que,self.validip_que)

    def checkout_proxy(self):
       
        while True :
            # print("开始检测")
            inip = globalVal.ip_que.get()
            # print('---------------'+inip)
            # validip_que.put(inip)
           
            ip = {'http': inip,'https': inip}
            proxy = request.ProxyHandler(ip)
            opener = request.build_opener(proxy)
            # ua=FakeUserAgent()
            url = 'http://httpbin.org/ip'
            reqhd = request.Request(url)
            ip = inip.split(':')[0]
            try:
                req = opener.open(reqhd, timeout=2)
                
                if req.code == 200:
                    con = req.read().decode('utf-8')
                    # print(con)
                    # if ip in con:
                    #     print(ip)
                    # print("有效IP%s" % inip)
                    globalVal.validip_que.put(inip)
                    # print("当前有效IP数量为%d"%(globalVal.validip_que.qsize()))
                    # else:
                    #     pass
                        # print("无效IP%s" % inip)
                else:
                    pass
                    # print("无效IP%s" % inip)
            except Exception as e:
                pass
                # print("无效IP%s" % ip)
            globalVal.ip_que.task_done()

    def collectUrl(self):
        # print("代理IP采集线程开启")
        # with open('proxy.txt', 'r') as f:
        #     for line in f.readlines():
        #         inip = line
        #         self.ip_que.put(inip)
                # self.validip_que.put(inip)
        # while True:
        apiUrl="https://foortu.com/proxy/1134f1fba496dc78a93017d52bbe46a4"
        if globalVal.ip_que.qsize() < 10:
            # print("开始采集代理IP")
            # headers.txt里的内容为浏览器打开apiUrl的请求头，将该请求头用于发送请求代理IP的接口
            with open('proxy_api_requestHeaders.txt', 'r') as f:
                headerStr=f.read()
                headersArr=headerStr.split('\n')
            headers={}
            for headerItem in headersArr:
                headersItemName=headerItem.split(': ')[0]
                headerItemValue=headerItem.split(': ')[1]
                headers[headersItemName]=headerItemValue
            response = requests.get(apiUrl,headers=headers,verify=False)
            
            text = response.text
            
            to_one_line = ' '.join(text.split())
            IP_LIST = to_one_line.split(' ')
        
            for ip in IP_LIST[0:800]:
                globalVal.ip_que.put(ip)
            #     print(ip)
            # print("成功收集代理IP%d条" % (len(IP_LIST)))
            # print("当前代理IP个数为%d" % (globalVal.ip_que.qsize()))
            
            # else:
            #     pass
                # print("代理IP数量已达上限，开始休眠")
                # time.sleep(1)

def main():
    proxy_helper=Proxy_helper(4,6)
    proxy_helper.run()

if __name__=="__main__":
    main()
