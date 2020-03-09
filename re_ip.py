# -*- coding: utf-8 -*-
#正则提取IP地址
import os
import re
ifconfig = os.popen('ifconfig ens33').readlines()
#方法一(match 匹配字符从头开始)
for ip in ifconfig:
    for string in re.split(' ',ip):
        ipaddress = re.match('(\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})', string)
        if ipaddress is not None:
            print(ipaddress.group())
            print(ipaddress.group(1))
            print(ipaddress.groups(1))

print("="*25)


#方法二（search 匹配字符任意位置，保留第一个匹配）
ipaddress = re.search("(\d{1,3}.\d{1,3}.\d{1,3}.\d{1,3})", str(ifconfig))
print(ipaddress.group())
print("="*25)

#方法三 （findall 匹配所有字符）

ipaddress = re.findall("(?:[0-9]{1,3}\.){3}[0-9]{1,3}", str(ifconfig))
print(ipaddress)


print('\n'*2)

print("网络接口ENS33 IP ADDRESS:{0:>30}".format(ipaddress[0]))
print("网络接口ENS33 IP NETMASK:{0:>30}".format(ipaddress[1]))
print("网络接口ENS33 IP BROADCAST:{0:>30}".format(ipaddress[2]))
