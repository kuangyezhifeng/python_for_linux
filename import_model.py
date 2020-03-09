# -*- coding: utf-8 -*-
# 学习导入自己编写的模块
import logging
import getpass
from paramiko_ssh import ssh
from scapy_ping import ping

logging.getLogger("scapy.runtime").setLevel(logging.ERROR)


def ping_and_ssh(ip, username, passwd, port=22):
    ping_result = ping(ip)
    if ping_result[1] == 1:
        print(ping_result[0], 'host active!')
        ssh(ip, username, passwd, port)
    else:
        print(ping_result[0], 'host dead!')


if __name__ == "__main__":
    ipaddress = input('please input connect ip address:')
    port = input('please input connect port:')
    username = input('please input your username:')
    password = getpass.getpass('please input your password:')

    ping_and_ssh(ipaddress, username, password, port)
