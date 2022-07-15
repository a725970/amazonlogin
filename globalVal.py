
from queue import Queue


global_list = []
ip_que=Queue(120000)
validip_que=Queue(100000)

ipCheckoutThreadMount = 7
ipCollectThreadMount = 2
dataCollectThreadMount = 5