# -*- coding:utf-8 -*-

import threading
from queue import Queue
import re
import time
import json
import logging
from lxml import etree
from proxy_helper import Proxy_helper
from bs4 import BeautifulSoup
import pymysql
from mysqlConfig import MysqlConfig
from userAgents import userAgents
from urllib.parse import urlparse
import sys
import multiprocessing
from concurrent.futures import ThreadPoolExecutor
import os
import signal
from audible.auth import Authenticator

import httpx
import requests

from requests.cookies import cookiejar_from_dict
import asyncio
import ddddocr

from urllib.parse import urlparse
import audible
REGIONS_URLS = {
    "sg": "https://www.amazon.sg/ap/signin?openid.pape.max_auth_age=0&openid.return_to=https://www.amazon.sg/ref=nav_logo/?_encoding=UTF8&ref_=navm_hdr_signin&openid.identity=http://specs.openid.net/auth/2.0/identifier_select&openid.assoc_handle=anywhere_v2_sg&openid.mode=checkid_setup&openid.claimed_id=http://specs.openid.net/auth/2.0/identifier_select&openid.ns=http://specs.openid.net/auth/2.0&",
    "nl": "https://www.amazon.nl/ap/signin?openid.pape.max_auth_age=0&openid.return_to=https://www.amazon.nl/ref=nav_logo/?_encoding=UTF8&ref_=navm_hdr_signin&openid.identity=http://specs.openid.net/auth/2.0/identifier_select&openid.assoc_handle=anywhere_v2_nl&openid.mode=checkid_setup&openid.claimed_id=http://specs.openid.net/auth/2.0/identifier_select&openid.ns=http://specs.openid.net/auth/2.0&",
    "it": "https://www.amazon.it/ap/signin?openid.pape.max_auth_age=0&openid.return_to=https://www.amazon.it/ref=nav_logo/?_encoding=UTF8&ref_=navm_hdr_signin&openid.identity=http://specs.openid.net/auth/2.0/identifier_select&openid.assoc_handle=anywhere_v2_it&openid.mode=checkid_setup&openid.claimed_id=http://specs.openid.net/auth/2.0/identifier_select&openid.ns=http://specs.openid.net/auth/2.0&",
    "in": "https://www.amazon.in/ap/signin?openid.pape.max_auth_age=0&openid.return_to=https://www.amazon.in/ref=nav_logo/?_encoding=UTF8&ref_=nav_ya_signin&openid.identity=http://specs.openid.net/auth/2.0/identifier_select&openid.assoc_handle=inflex&openid.mode=checkid_setup&openid.claimed_id=http://specs.openid.net/auth/2.0/identifier_select&openid.ns=http://specs.openid.net/auth/2.0&",
    "fr": "https://www.amazon.fr/ap/signin?openid.pape.max_auth_age=0&openid.return_to=https://www.amazon.fr/ref=nav_logo/?_encoding=UTF8&ref_=navm_hdr_signin&openid.identity=http://specs.openid.net/auth/2.0/identifier_select&openid.assoc_handle=anywhere_v2_fr&openid.mode=checkid_setup&openid.claimed_id=http://specs.openid.net/auth/2.0/identifier_select&openid.ns=http://specs.openid.net/auth/2.0&",
    "es": "https://www.amazon.es/ap/signin?openid.pape.max_auth_age=0&openid.return_to=https://www.amazon.es/ref=nav_logo/?_encoding=UTF8&ref_=navm_hdr_signin&openid.identity=http://specs.openid.net/auth/2.0/identifier_select&openid.assoc_handle=anywhere_v2_es&openid.mode=checkid_setup&openid.claimed_id=http://specs.openid.net/auth/2.0/identifier_select&openid.ns=http://specs.openid.net/auth/2.0&",
    "ca": "https://www.amazon.ca/ap/signin?openid.pape.max_auth_age=0&openid.return_to=https://www.amazon.ca/ref=nav_logo/?_encoding=UTF8&ref_=navm_hdr_signin&openid.identity=http://specs.openid.net/auth/2.0/identifier_select&openid.assoc_handle=anywhere_v2_ca&openid.mode=checkid_setup&openid.claimed_id=http://specs.openid.net/auth/2.0/identifier_select&openid.ns=http://specs.openid.net/auth/2.0&",
    "de": "https://www.amazon.de/ap/signin?openid.pape.max_auth_age=0&openid.return_to=https://www.amazon.de/ref=nav_logo/?_encoding=UTF8&ref_=navm_hdr_signin&openid.identity=http://specs.openid.net/auth/2.0/identifier_select&openid.assoc_handle=anywhere_v2_de&openid.mode=checkid_setup&openid.claimed_id=http://specs.openid.net/auth/2.0/identifier_select&openid.ns=http://specs.openid.net/auth/2.0&",
    "ae": "https://www.amazon.ae/ap/signin?openid.pape.max_auth_age=0&openid.return_to=https://www.amazon.ae/ref=nav_logo/?_encoding=UTF8&ref_=navm_hdr_signin&openid.identity=http://specs.openid.net/auth/2.0/identifier_select&openid.assoc_handle=anywhere_v2_ae&openid.mode=checkid_setup&openid.claimed_id=http://specs.openid.net/auth/2.0/identifier_select&openid.ns=http://specs.openid.net/auth/2.0&",
    "us": "https://www.amazon.com/ap/signin?openid.pape.max_auth_age=0&openid.return_to=https://www.amazon.com/ref=nav_logo/?_encoding=UTF8&ref_=nav_ya_signin&openid.identity=http://specs.openid.net/auth/2.0/identifier_select&openid.assoc_handle=usflex&openid.mode=checkid_setup&openid.claimed_id=http://specs.openid.net/auth/2.0/identifier_select&openid.ns=http://specs.openid.net/auth/2.0&",
    "jp": "https://www.amazon.co.jp/ap/signin?_encoding=UTF8&openid.mode=checkid_setup&openid.ns=http://specs.openid.net/auth/2.0&openid.claimed_id=http://specs.openid.net/auth/2.0/identifier_select&openid.pape.max_auth_age=0&ie=UTF8&openid.ns.pape=http://specs.openid.net/extensions/pape/1.0&openid.identity=http://specs.openid.net/auth/2.0/identifier_select&openid.assoc_handle=amzn_lwa_apac&marketPlaceId=A1MA27DB7MMG0L&arb=f5169592-d0d9-44c2-af5a-9d69d39d6e9b&language=ja_JP&openid.return_to=https://apac.account.amazon.com/ap/oa?marketPlaceId=A1MA27DB7MMG0L&arb=f5169592-d0d9-44c2-af5a-9d69d39d6e9b&language=ja_JP&enableGlobalAccountCreation=1&metricIdentifier=amzn1.application.1baefeb23f8c4b85b8a1d4be010dc435&signedMetricIdentifier=A+DgRwQcJwh60Eft5IL1IEt7dtEIkAUptGAlOWIaefo=",
    "uk": "https://www.amazon.co.uk/ap/signin?openid.pape.max_auth_age=0&openid.return_to=https://www.amazon.co.uk/ref=nav_logo/?_encoding=UTF8&ref_=navm_hdr_signin&openid.identity=http://specs.openid.net/auth/2.0/identifier_select&openid.assoc_handle=anywhere_v2_uk&openid.mode=checkid_setup&openid.claimed_id=http://specs.openid.net/auth/2.0/identifier_select&openid.ns=http://specs.openid.net/auth/2.0&",
    "tr": "https://www.amazon.com.tr/ap/signin?openid.pape.max_auth_age=0&openid.return_to=https://www.amazon.com.tr/ref=nav_logo/?_encoding=UTF8&ref_=navm_hdr_signin&openid.identity=http://specs.openid.net/auth/2.0/identifier_select&openid.assoc_handle=anywhere_v2_tr&openid.mode=checkid_setup&openid.claimed_id=http://specs.openid.net/auth/2.0/identifier_select&openid.ns=http://specs.openid.net/auth/2.0&",
    "br": "https://www.amazon.com.br/ap/signin?openid.pape.max_auth_age=0&openid.return_to=https://www.amazon.com.br/ref=nav_logo/?_encoding=UTF8&ref_=nav_ya_signin&openid.identity=http://specs.openid.net/auth/2.0/identifier_select&openid.assoc_handle=brflex&openid.mode=checkid_setup&openid.claimed_id=http://specs.openid.net/auth/2.0/identifier_select&openid.ns=http://specs.openid.net/auth/2.0&",
    "au": "https://www.amazon.com.au/ap/signin?openid.pape.max_auth_age=0&openid.return_to=https://www.amazon.com.au/ref=nav_logo/?_encoding=UTF8&ref_=navm_hdr_signin&openid.identity=http://specs.openid.net/auth/2.0/identifier_select&openid.assoc_handle=anywhere_v2_au&openid.mode=checkid_setup&openid.claimed_id=http://specs.openid.net/auth/2.0/identifier_select&openid.ns=http://specs.openid.net/auth/2.0&",
    "sa": "https://www.amazon.sa/ap/signin?openid.pape.max_auth_age=0&openid.return_to=https://www.amazon.sa/ref=nav_logo/?_encoding=UTF8&ref_=navm_hdr_signin&openid.identity=http://specs.openid.net/auth/2.0/identifier_select&openid.assoc_handle=anywhere_v2_sa&openid.mode=checkid_setup&openid.claimed_id=http://specs.openid.net/auth/2.0/identifier_select&openid.ns=http://specs.openid.net/auth/2.0&",
}
def recognize_text(src):
    code_url = src
    r=requests.get(url=code_url,timeout=5)
    ocr = ddddocr.DdddOcr()
    img_bytes=r.content

    res = ocr.classification(img_bytes)
    return res


def quit(signum, frame):
    print('*'*30)
    print('??????-----------------')
    sys.exit()

ISPORTY = False
logging.basicConfig(filename='log.txt',
                    filemode='a',
                    format='%(asctime)s,%(msecs)d %(name)s %(levelname)s %(message)s',
                    datefmt='%H:%M:%S',
                    level=logging.DEBUG)
class Spider():

    def __init__(self, threadName, url_queue, proxys,mainurl,cookies,userAgent,local):
        self.mysqlConfig=MysqlConfig
        self.url_queue = url_queue
        self.proxys = proxys
        self.userAgents =userAgent
        self.mainPageURL = mainurl
        self.cookies = cookies
        self.local = local
        self.productPageRequestCount=0
        self.count = 0

    def runSpider(self):

        # logging.info("%s????????????" % (self.name))
        self.connectMysql()
        # ??????cookie
        # self.initializeMysql()
        while not self.url_queue.empty():
            urlinfo = self.url_queue.get()
            urlinfo = urlinfo.split('||')
            url = urlinfo[0]
            account = urlinfo[1]
            self.sqlSelectUser(account,self.local)
            logging.info(url)

            self.getListHtml(url,account)
            self.url_queue.task_done()
            logging.info(self.url_queue.empty())

    def connectMysql(self):
        try:
            self.mysqlClient = pymysql.connect(
                host=self.mysqlConfig.host,
                port=self.mysqlConfig.port,
                user=self.mysqlConfig.user,
                passwd=self.mysqlConfig.password,
                database=self.mysqlConfig.database,
                use_unicode=True
            )
           
            logging.info("?????????????????????")
        except Exception as e:
            logging.info("?????????????????????")

    def initializeMysql(self):
        with open("initialize.sql", 'r', encoding='utf-8') as fd:
            sqlStr=fd.read()
            sqlCommands = sqlStr.split(';')
            for command in sqlCommands:
                if command!="":
                    try:
                        self.mysqlClient.cursor().execute(command)
                        logging.info("??????????????????sql??????")
                        
                    except Exception as msg:
                        pass
                        # logging.info(msg)
            logging.info("????????????????????????!")
    def getSession(self,url):
        # ????????????
        headers = {
            "Accept": "text/html,application/xhtml+xmmysqlClientl,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8",
            "Accept-Encoding": "gzip, deflate, br",
            "Accept-Language": "zh-CN,zh;q=0.9,en;q=0.8",
            "Cache-Control": "max-age=0",
            "Connection": "keep-alive",
            "Referer": "%s" % (url),
            "Upgrade-Insecure-Requests": "1",
            "User-Agent": "%s" % (self.userAgents)
        }
        session = requests.session()
        session.headers = headers
        cookies = self.cookies
        requests.utils.add_dict_to_cookiejar(session.cookies, cookies)
        return session,headers
    def getListHtml(self,url,account,headers='',repeat_count=0):
       
        validip = self.proxys

        proxy = {'https': validip,'http': validip}
        print(url)
        # try:
        session,headers = self.getSession(url)
        if ISPORTY == True:
            response = session.get(url, proxies=proxy, timeout=5, verify=False)
        else:
            response = session.get(url, timeout=5, verify=False)
        if response.status_code == 200:
            
            # response.encoding = "euc-kr"

            soup = BeautifulSoup(response.text, "html.parser")
            if 'yourpayments/wallet' in url:
                logging.info(account+'_'+'yourpayments/wallet.html')
                # with open(account+'_'+'wallet.html', 'w', encoding='utf-8') as f:
                #     f.write(response.text)
                    
                self.getWalletHtml(account,soup)
                logging.info('yourpayments/wallet')
            elif 'addresses' in url:
                # with open(account+'_'+'addresses.html', 'w', encoding='utf-8') as f:
                #     f.write(response.text)
                logging.info('addresses')
                self.getAddressHtml(account,soup)  
            elif 'order-history' in url:
                # with open(account+'_'+'order-history.html', 'w', encoding='utf-8') as f:
                #     f.write(response.text)
                logging.info('order-history')
                # host = 'www.amazon.co.jp'
                host = urlparse(url).hostname
                logging.info(host)
                self.getOrderHistoryHtml(account,soup,session,host) 
            elif 'balance' in url:
                # with open(account+'_'+'balance.html', 'w', encoding='utf-8') as f:
                #     f.write(response.text)
                  
                self.getBalanceHtml(account,soup)  
                logging.info('balance')
            elif 'review-your-purchases' in url:
                # with open(account+'_'+'review-your-purchases', 'w', encoding='utf-8') as f:
                #     f.write(response.text)
                  
                self.getReviewPurchasesHtml(account,soup)  
                logging.info('getReviewPurchasesHtml')
            
        else:
            repeat_count += 1
            if repeat_count < 4:
                logging.info("%s???????????????????????????????????????%d???????????????!" % (url, repeat_count))
                self.getListHtml(url,account,headers,repeat_count)
            else:
                logging.info("%s?????????????????????" % (url))
                self.sqlInsertFailedListUrl(url)

    def getWalletHtml(self,account,soup):
        dom = etree.HTML(str(soup))
        titles = dom.xpath('//div[contains(@class, "a-row apx-wallet-tab-pm-name")]//text()')
        wallet = []
        if titles != None:
            descs = dom.xpath('//div[contains(@class, "a-row apx-wallet-tab-pm-description")]//text()')
            expirs = dom.xpath('//div[contains(@class, "a-fixed-left-grid apx-wallet-tab-pm-icon-label")]//text()')
            for index in range(len(titles)):
        
                title = titles[index]
                desc = descs[index]
                expir = None
                if len(expirs) > index:
                    expir = expirs[index]
                logging.info(title)
                logging.info(desc)
                logging.info(expir)
                wallet.append({'title':title,'desc':desc,'expir':expir})
            self.sqlInsertReviewWallet(account,wallet)
    def getOrderHistoryHtml(self,account,soup,session,host):
        dom = etree.HTML(str(soup))  
        selectdowns = dom.xpath('//select[contains(@class, "a-native-dropdown")]/option')
        if selectdowns != []:
            first = ''
            end = ''
            lenlist =len(selectdowns)
            # ???????????????????????????
            try:
                url = "https://"+host+'/gp/your-account/order-history?opt=ab&digitalOrders=1&unifiedOrders=1&returnTo=&__mk_ja_JP=%E3%82%AB%E3%82%BF%E3%82%AB%E3%83%8A&orderFilter=last30'
                # ???????????? ??????
                validip = self.proxys

                proxy = {'https': validip,'http': validip}
        
                # try:
                session,headers = self.getSession(url)
                
                if ISPORTY == True:
                    response = session.get(url, proxies=proxy, timeout=5)
                else:
                    response = session.get(url, timeout=5)
                
                if response.status_code == 200:
                    
                   
                    soup = BeautifulSoup(response.text, "html.parser")
                    dom = etree.HTML(str(soup))
               
                orders = dom.xpath('//*[contains(@class, "a-form-label num-orders-for-orders-by-date aok-inline-block a-text-normal")]//text()')
                if len(orders) > 0: 
                    msg = '??????????????? ?????????|'
                else:
                    msg = '??????????????? ?????????|'    
            except:
                msg = '??????????????? ?????????|except'   
            for index in range(lenlist):
                if index > 1:
                    first = selectdowns[index].attrib['value']
                    url = "https://"+host+"/gp/your-account/order-history?opt=ab&digitalOrders=1&unifiedOrders=1&returnTo=&__mk_ja_JP=%E3%82%AB%E3%82%BF%E3%82%AB%E3%83%8A&orderFilter="+str(first)
                    # ???????????? ??????
                    validip = self.proxys

                    proxy = {'https': validip,'http': validip}
            
                    # try:
                    session,headers = self.getSession(url)
                    
                    if ISPORTY == True:
                        response = session.get(url, proxies=proxy, timeout=5)
                    else:
                        response = session.get(url, timeout=5)
                    
                    if response.status_code == 200:
                        
                        # response.encoding = "euc-kr"

                        soup = BeautifulSoup(response.text, "html.parser")
                        dom = etree.HTML(str(soup))
                        orders = dom.xpath('//*[contains(@class, "a-form-label num-orders-for-orders-by-date aok-inline-block a-text-normal")]//text()')
                        if len(orders) > 0: 
                            first = first.replace("year-","")
                            break
                        else:
                            first = ''
            for index in range(lenlist):
                if lenlist-index > 1:
                    end = selectdowns[(lenlist-index)-1].attrib['value']
                    url = "https://"+host+"/gp/your-account/order-history?opt=ab&digitalOrders=1&unifiedOrders=1&returnTo=&__mk_ja_JP=%E3%82%AB%E3%82%BF%E3%82%AB%E3%83%8A&orderFilter="+str(first)
                    # ???????????? ??????
                    validip = self.proxys

                    proxy = {'https': validip,'http': validip}
            
                    # try:
                    session,headers = self.getSession(url)
                    
                    if ISPORTY == True:
                        response = session.get(url, proxies=proxy, timeout=5)
                    else:
                        response = session.get(url, timeout=5)
                    
                    if response.status_code == 200:
                        
                        # response.encoding = "euc-kr"

                        soup = BeautifulSoup(response.text, "html.parser")
                        dom = etree.HTML(str(soup))
                        orders = dom.xpath('//*[contains(@class, "a-form-label num-orders-for-orders-by-date aok-inline-block a-text-normal")]//text()')
                        if len(orders) > 0: 
                            end = end.replace("year-","")
                            break
                        else:
                            end = ''             
            logging.info('------------------------')
        
            if first == '' and end == '':
                msg += '?????????'
            else:
                msg += end+ '-'+ first
            self.sqlInsertReviewOrderList(account,msg)  
            print(msg)
    def getBalanceHtml(self,account,soup):
        dom = etree.HTML(str(soup))
        titles = dom.xpath('//*[@id="gc-ui-balance-gc-balance-value"]//text()')
        if titles != []:   
            balance = titles[0].replace("\n","").replace(" ","")
            logging.info(balance)
            self.sqlInsertReviewBalance(account,balance)
    def getAddressHtml(self,account,soup):
        dom = etree.HTML(str(soup))
        address = []
        for index in range(100):
            try:
                titles = dom.xpath('//*[@id="ya-myab-display-address-block-'+str(index)+'"]/div/div/div/ul//text()')
                if titles == []:
                    break
                address.append(titles)
                logging.info(titles)
            except:
                break
        self.sqlInsertReviewAddress(account,address)
    def getReviewPurchasesHtml(self,account,soup):
        dom = etree.HTML(str(soup))
        msg = ''
        try:
            # ??? bug ???????????????????????????

            titles = dom.xpath('//button[contains(@class, "ryp__star__button)]')
            
            if titles != None and titles != []:
             
                msg = '????????????'
            else:
                msg = '???????????????'
        except:
            msg = '???????????????'
        self.sqlInsertReviewPurchases(account,msg)
    def getArticleHtml(self, arc_url,list_url,repeat_count=0):
        headers={
            "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8",
            "Accept-Encoding": "gzip, deflate",
            "Accept-Language": "zh-CN,zh;q=0.9,en;q=0.8",
            "Cache-Control": "no-cache",
            "Connection": "keep-alive",
            "Host": "cellbank.snu.ac.kr",
            "Pragma": "no-cache",
            "Referer": list_url,
            "Upgrade-Insecure-Requests": "1",
            "User-Agent": "%s" % (self.userAgents)
        }

    def sqlInsertReviewPurchases(self, account,purchases):
        global sql
        sql = """
        UPDATE `userinfo` SET `purchases`='%s' WHERE account ='%s'
        """ %(purchases,account)
        if self.mysqlClient.cursor().execute(sql):
            self.mysqlClient.commit()
            logging.info("???????????????????????? sqlInsertReviewPurchases")
        else:
            logging.info("?????????????????? sqlInsertReviewPurchases")
            self.sqlInsertFailedArcUrl(purchases)

    def sqlInsertReviewAddress(self, account,address):
        address = str(address)
        global sql
        sql = """
        UPDATE `userinfo` SET `address`="%s" WHERE account ='%s'
        """ %(address.replace('\'','').replace(',','???').replace('[','{').replace(']','}'),account)

        if self.mysqlClient.cursor().execute(sql):
            self.mysqlClient.commit()
            logging.info("???????????????????????? sqlInsertReviewAddress")
        else:
            logging.info("?????????????????? sqlInsertReviewAddress")
            self.sqlInsertFailedArcUrl(address)

    def sqlInsertReviewBalance(self, account,balance):
        global sql
        sql = """
        UPDATE `userinfo` SET `balance`="%s" WHERE account ='%s'
        """ %(balance,account)

        if self.mysqlClient.cursor().execute(sql):
            self.mysqlClient.commit()
            logging.info("???????????????????????? sqlInsertReviewBalance")
        else:
            logging.info("?????????????????? sqlInsertReviewBalance")
            self.sqlInsertFailedArcUrl(balance)

    def sqlInsertReviewOrderList(self, account,orderinfo):
        global sql
        sql = """
        UPDATE `userinfo` SET `orderinfo`="%s" WHERE account ='%s'
        """ %(orderinfo,account)
 
        if self.mysqlClient.cursor().execute(sql):
            self.mysqlClient.commit()
            logging.info("???????????????????????? sqlInsertReviewOrderList")
        else:
            logging.info("?????????????????? sqlInsertReviewOrderList")
            self.sqlInsertFailedArcUrl(orderinfo)

    def sqlInsertUserList(self, account,cookie,host,password,region,ip,ua):
        
        global sql
        sql = """
        INSERT INTO `spider`.`userlist` (`account`, `cookie`, `status`, `host`, `password`, `region`, `ip`, `ua`) VALUES ("%s", '%s', "%s", "%s", "%s", "%s", "%s", "%s")
        """ %(account,cookie,'1',host,password,region,ip,ua)
 
        if self.mysqlClient.cursor().execute(sql):
            self.mysqlClient.commit()
            logging.info("???????????????????????? sqlInsertReviewWallet")
        else:
            logging.info("?????????????????? sqlInsertReviewWallet")
            

    def sqlInsertReviewWallet(self, account,wallet):
        wallet = str(wallet)
        global sql
        sql = """
        UPDATE `userinfo` SET `wallet`="%s" WHERE account ='%s'
        """ %(wallet.replace('\'','').replace(',','|').replace('[','{').replace(']','}'),account)
 
        if self.mysqlClient.cursor().execute(sql):
            self.mysqlClient.commit()
            logging.info("???????????????????????? sqlInsertReviewWallet")
        else:
            logging.info("?????????????????? sqlInsertReviewWallet")
            self.sqlInsertFailedArcUrl(wallet)
    def sqlSelectUser(self, account,country):
        global sql
        sql = """
        INSERT IGNORE INTO `userinfo`(`account`, `country`) VALUES('%s', '%s')
        """ %(account,country)

        if self.mysqlClient.cursor().execute(sql):
            self.mysqlClient.commit()
            logging.info("???????????????????????? sqlSelectUser")
        else:
            logging.info("?????????????????? sqlSelectUser")
            
    def sqlInsertFailedListUrl(self, url):
        global sql
        sql = """INSERT IGNORE INTO cellbank_failed_arc_url(url) VALUES ('{}')""".format(url)
        # logging.info(sql)
        self.mysqlClient.cursor().execute(sql)
        self.mysqlClient.commit()
        logging.info("????????????????????????:%s" % (url))

    def sqlInsertFailedArcUrl(self, url):
        global sql
 
    def SelectUserList(self):
        global sql
        sql = """SELECT * From userlist WHERE status = 0"""
        logging.info(sql)
        self.mysqlClient.cursor().execute(sql)
        self.mysqlClient.commit()
        logging.info("????????????????????????")

    def addPoidList(self, poiId_list_string):
        global sql
        sql = """INSERT IGNORE INTO meituan_poId_list(poiId_list_string) VALUES ("{}")""".format(poiId_list_string)
        self.mysqlClient.cursor().execute(sql)
        self.mysqlClient.commit()
        logging.info("????????????poiId????????????")

# os.environ['TESSDATA_PREFIX'] = "C:\\Program Files (x86)\\Tesseract-OCR\tessdata/tessdata/eng.traineddata"

def custom_approval_callback():
    print('-----------')
    return True
    # You can let python check for the received Amazon mail and 

def custom_captcha_callback(captcha_url: str) -> str:
    """Opens captcha image with eog, or default webbrowser as fallback"""
    # src = cv.imread(captcha_url)
    start = time.time()
   
    val = recognize_text(captcha_url)

    end = time.time()
    print('Running time: %s Seconds' % (end-start))

    return val
async def main(auth,locale,account,proxys,userAgent):
    async with audible.AsyncClient(auth) as client:
        print(repr(client))
    
        with httpx.Client(cookies=auth.website_cookies) as session:
            scheme, netloc, path, _, _, _ = urlparse(REGIONS_URLS[locale])
            url = 'https://'+netloc+'/'
            # resp=session.get(url)
       
            cookies = {}
            for key,value in session.cookies.items():
                cookies[key] = value


            print(cookies)
            cookies2 = []
            expires = time.time() + (60*60*24*30) # expires in 30 days
            # for i in range(len(session.cookies.items())):
            index = 1
            for key,value in session.cookies.items():
                cookie = {}
                cookie.update(domain=netloc,expirationDate=expires,hostOnly=True,httpOnly=False,
                name=key,path="/",sameSite='unspecified',secure=True,session=False,storeId="0",value=value,id=str(index))
                index =+ 1
                cookies2.append(cookie)
               
     
            print(json.dumps(cookies2))
            url_list = [
            'https://'+netloc+'/a/addresses||'+account,
            'https://'+netloc+'/gp/css/gc/balance?ref_=ya_d_c_gc||'+account,
            # 'https://'+host+'/gp/css/order-history?ref_=nav_orders_first||'+account,
            'https://'+netloc+'/cpe/yourpayments/wallet?ref_=ya_d_c_pmt_mpo||'+account,
            'https://'+netloc+'/review/review-your-purchases/listing||'+account
            ]
           
            url_que = Queue(300)
            
            for arc_url in url_list:
                url_que.put(arc_url)
            mainurl = 'https://'+netloc+'/'
            worker = Spider("??????????????????%d" % (1), url_que, proxys,mainurl,cookies,userAgent,locale)
            worker.runSpider()
            # ??????cookie
            # try:
            worker.sqlInsertUserList(account,json.dumps(cookies2),netloc,'',locale,proxys,userAgent)
            # except:
            #     pass
            print("??????????????????%d??????" % (1))


def authlogin(locale,user,password,myproxy,userAgent):
    auth = Authenticator.from_login(
        username=user,
        proxys=myproxy,
        userAgent=userAgent,
        password=password,
        locale=locale,
        captcha_callback=custom_captcha_callback,
    )
    loop = asyncio.get_event_loop()
    loop.run_until_complete(main(auth,locale,user,myproxy,userAgent))          
        
        
if __name__ == "__main__":
    import time

    start = time.time()
    
    ip_que = Queue(1200)
    validip_que = Queue(1200)
    ipCheckoutThreadMount = 7
    ipCollectThreadMount = 2
    dataCollectThreadMount = 5
    proxy_helper = Proxy_helper(ip_que, validip_que, ipCheckoutThreadMount, ipCollectThreadMount)
        # ?????? ?????????
    signal.signal(signal.SIGINT, quit)                                
    signal.signal(signal.SIGTERM, quit)
    proxy_helper.run()
    
    with open('amazon.txt', 'r') as f:
        for line in f.readlines():
            userinfo = line.split('|')
            user = userinfo[0]
            password = userinfo[1]
            locale = userinfo[2].replace('\n', '')

            validip = validip_que.get()
            userAgent =  userAgents.getUA()
            myproxy=validip

          
            t = threading.Thread(target=authlogin(), args=(locale,user,password,myproxy,userAgent), daemon=True)
            threads.append(t)

            print("??????????????????%d??????" % (1))

            ThinkTime = 0.1#??????????????????
            for t in threads:
                time.sleep(ThinkTime) 
                #print "thread %s" %t #????????????
                # t.setDaemon(True)
                print("??????--------??????%d??????" % (1))
                t.start()
            t.join()
   
           
    end = time.time()
    print ("????????????: %f s" % (end - start))#
    # deregister device
    # auth.deregister_device()