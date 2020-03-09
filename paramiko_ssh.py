# -*- coding: utf-8 -*-
# paramiko 实现一个SSH连接并执行输入的指令
# PE8规则：1.#号后面的注释与#要有空格 2.参数用逗号分格，逗号后面应有空格隔开 3.类与上面的代码行应该有两个空白行
# 当函数内部生成一个实例的时候，如果想使用可以使用return将实例返回。

import paramiko
import getpass


# 连接一个主机
def ssh(ip, username, passwd, port=22):
    print(ip, username, passwd, port)
    # 实例化一个对象
    host_ssh = paramiko.SSHClient()
    host_ssh.load_system_host_keys()
    host_ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    try:
        host_ssh.connect(ip, port=port, username=username, password=passwd, timeout=5, compress=True)
        print('host connect ok!', '\n'*2)
        return host_ssh
    # 执行连接不成功的异常捕获
    except Exception as e:
        print('host connect failure!', e)


# 操作SSH实例对象
def term():
    terminal = host_info()
    # 实现简易SSH终端输入指令
    while True:
        command = input('input <command> or <quit>:')
        if command != "quit":
            stdin, stdout, stderr = terminal.exec_command(command)
            print(stdout.read().decode())
        else:
            break


# 获取用户输入信息
def host_info():
    ipaddress = input('please input connect ip address:')
    port = input('please input connect port:')
    username = input('please input your username:')
    password = getpass.getpass('please input your password:')
    terminal = ssh(ipaddress, username, password, port)
    return terminal


if __name__ == "__main__":
    term()
