# -*- coding: utf-8 -*-
# 类的学习
# 类的定义首字符或全部大写,中间不要出现下划线
# 类的定义与实例化类头部要空两行

from scapy.all import *


class PingPkt:

    def __init__(self, dstip, srcip=None):
        self.srcip = srcip
        self.dstip = dstip
        self.length = 100

    def ping_pkt(self):
        package = IP(dst=self.dstip, src=self.srcip)/ICMP()/(b'v' * self.length)
        result = sr1(package, timeout=2, verbose=False)
        if result:
            return result
        else:
            return 0

    def ping_one(self):
        result = self.ping_pkt()
        if result:
            print('A package has been seed!')
        else:
            print('A package has been seed!,but host noresponse! ')

    def size_pkt(self, length):
        self.length = length
        result = self.ping_pkt()
        if result:
            print('A {0}byte package has been seed!'.format(self.length))
        else:
            print('A package has been seed!,but host noresponse! ')

    def src_ip(self, srcip):
        self.srcip = srcip
        result = self.ping_pkt()
        if result:
            print('A src ip {0} package has been seed!'.format(srcip))
        else:
            print('A package has been seed!,but host noresponse! ')

    def ping(self):
        for i in range(5):
            result = self.ping_pkt()
            if result:
                print('!', end='', flush=True)
            else:
                print('.', end='', flush=True)

    # 自定义打印实例返回值,而不是返回一个内存地址
    def __str__(self):
        if not self.srcip:
            return '<dstip: {0}, size: {1}>'.format(self.dstip, self.length)
        else:
            return '<srcip: {0}, dstip: {1}, size: {2}>'.format(self.srcip, self.dstip, self.length)
# 实例化


test = PingPkt('192.168.1.75')


# 打印实例信息
print(test)

# 测试实例方法
# test.src_ip('8.8.8.8')
# test.ping_one()
test.size_pkt(1000)
# test.ping()

