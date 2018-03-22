import ipaddress
import sh
import socket

# import pandas as pd 
# from pandas import Series, DataFrame
# import numpy as np


#get network address
s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
s.connect(("8.8.8.8", 80))
networkAddress = s.getsockname()[0] #returns socket's own address
s.close()

first, second, third, fourth = str(networkAddress).split('.')

#modify network address to scan all addresses
addr = str(first) + '.' + str(second) + '.' + str(third) + '.' + '0/24'

network = ipaddress.ip_network(unicode(addr))

for i in network.hosts():
    
    try:
        sh.ping(i, "-c 1")
        print i, "is active"
        data_visualization(addrs)
    except sh.ErrorReturnCode_2:
        print "no response from", i


# def data_visualization(addrs):
#     states ={'IP' :[addr],
#                   'Activity': ['active']}
#     addys = DataFrame(states) # creating a data frame
#     addys

