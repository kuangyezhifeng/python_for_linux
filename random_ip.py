# -*- coding: utf-8 -*-
#author:wildlee
#生成一个随机IP地址
import random

#方法一
select_1=str(random.randint(1,255))+'.'+str(random.randint(1,255))+'.'+str(random.randint(1,255))+'.'+str(random.randint(1,255))
print(select_1)

#方法二
def random_num():
    num=random.randint(1,255)
    return num

ip_addr='{0}.{1}.{2}.{3}'.format(random_num(),random_num(),random_num(),random_num())
print(ip_addr)



#方法三
ip_addr='{0}.{1}.{2}.{3}'.format(random.randint(1,255),random.randint(1,255),random.randint(1,255),random.randint(1,255))
print(ip_addr)

hello