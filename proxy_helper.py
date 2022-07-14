# -*- coding:utf-8 -*-
from urllib import request
import requests
import time
import re
from queue import Queue
import threading

class Proxy_helper():
    def __init__(self, ip_que, validip_que,checkoutThreadMount,collectThreadMount):
        self.ip_que = ip_que
        self.validip_que = validip_que
        self.checkoutThreadMount=checkoutThreadMount
        self.collectThreadMount=collectThreadMount

    def run(self):
 
        # inip = 'socks5://wocaonimaheheda_dc_1:lt6Cb6jXsFD8PF1W)@proxyus.rola.info:2000'
        # for index in range(20):
        #     self.ip_que.put(inip)
        #     self.validip_que.put(inip)
       
        self.collectUrl_start()
        # time.sleep(1)
        print(2222)
        self.checkout_start()

    def collectUrl_start(self):
        self.collectUrl(self.ip_que,)


    def checkout_start(self):
        for i in range(self.checkoutThreadMount):
            worker = threading.Thread(target=self.checkout_proxy, args=(self.ip_que,self.validip_que), name="验证IP线程%d" % (i))
            worker.start()
            print("验证IP线程开启%d" % (i))

    def checkout_proxy(self,ip_que,validip_que):
        while not ip_que.empty() :
            print("开始检测")
            inip = ip_que.get()
      
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
                    
                    if ip in con:
                        print(ip)
                        print("有效IP%s" % inip)
                        validip_que.put(inip)
                        print("当前有效IP数量为%d"%(validip_que.qsize()))
                    else:
                        pass
                        # print("无效IP%s" % inip)
                else:
                    pass
                    # print("无效IP%s" % inip)
            except Exception as e:
                pass
                print("无效IP%s" % ip)
            ip_que.task_done()

    def collectUrl(self,ip_que):
        print("代理IP采集线程开启")
        # with open('proxy.txt', 'r') as f:
        #     for line in f.readlines():
        #         inip = line
        #         self.ip_que.put(inip)
        #         # self.validip_que.put(inip)
        apiUrl="https://foortu.com/proxy/1134f1fba496dc78a93017d52bbe46a4"
        if ip_que.qsize() < 100:
            print("开始采集代理IP")
            # headers.txt里的内容为浏览器打开apiUrl的请求头，将该请求头用于发送请求代理IP的接口
            with open('proxy_api_requestHeaders.txt', 'r') as f:
                headerStr=f.read()
                headersArr=headerStr.split('\n')
            headers={}
            for headerItem in headersArr:
                headersItemName=headerItem.split(': ')[0]
                headerItemValue=headerItem.split(': ')[1]
                headers[headersItemName]=headerItemValue
            response = requests.get(apiUrl,headers=headers)
            
            text = response.text
            
            to_one_line = ' '.join(text.split())
            IP_LIST = to_one_line.split(' ')
          
            for ip in IP_LIST[0:50]:
                ip_que.put(ip)
                print(ip)
            print("成功收集代理IP%d条" % (len(IP_LIST)))
            print("当前代理IP个数为%d" % (ip_que.qsize()))
        else:
            
            # print("代理IP数量已达上限，开始休眠")
            time.sleep(1)

def main():
    ip_que=Queue(1200)
    validip_que=Queue(100000)
    proxy_helper=Proxy_helper(ip_que,validip_que,4,6)
    proxy_helper.run()

if __name__=="__main__":
    main()
