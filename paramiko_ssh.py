# -*- coding: utf-8 -*-
#paramiko 实现一个SSH连接并执行输入的指令

import paramiko

def ssh(ip, username, passwd, port=22):
    print(ip, username, passwd, port)
    # 实例化一个对象
    host_ssh = paramiko.SSHClient()
    host_ssh.load_system_host_keys()
    host_ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())

    # 连接一个主机
    try:
        host_ssh.connect(ip, port=port, username=username, password=passwd, timeout=5, compress=True)
        print('host connect ok!')

        # 实现简易SSH终端输入指令
        while True:
            command = input('input <command> or <quit>:')
            if command != "quit":
                stdin, stdout, stderr = host_ssh.exec_command(command)
                print(stdout.read().decode())
            else:
                break
    # 执行连接不成功的异常捕获
    except Exception as e:
        print('host connect failure!', e)


if __name__ == "__main__":
    ssh('192.168.1.90', 'root', '*********')
