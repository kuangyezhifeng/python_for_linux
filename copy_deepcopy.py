# -*- coding: utf-8 -*-
#python浅复制与深度复制

from copy import *

list1 = [1,2,3]   #主列表
list2 = [4,5,6]   #子列表
list1.append(list2)

#复制,共享索引同一个内存数据
list_new = list1
list_new.append('new')
print("赋值引用变量LIST_NEW:{0}"'\n'"原变量LIST1:{1}".format(list_new,list1))
list1.pop(0) #指定索引值
print("赋值引用变量LIST_NEW改变:{0}"'\n'"原变量LIST1改变:{1}".format(list_new,list1))

print('\n',"*"*100,'\n')

#浅复制，复制深度为1，嵌套的列表引用内存索引地址
list_copy=list1.copy()
list_copy.append('copy')
print("浅复制引用变量LIST_NEW:{0}"'\n'"原变量LIST1:{1}".format(list_copy,list1))

list1.pop() #LIST1列表1层元素发生改变,浅复制的列表不改变
print("浅复制引用变量LIST_NEW:{0}"'\n'"原变量LIST1发生改变:{1}".format(list_copy,list1))

list2.append(7) #子列表发生改变,浅复制的子列表为引用地址发生改变
print("浅复制引用变量LIST_NEW:{0}"'\n'"原变量LIST1的子列表改变:{1}".format(list_copy,list1))


print('\n',"*"*100,'\n')

# #深度复制，为每个数据申请内存单独存放数据
list_deepcopy = deepcopy(list1)
print("深复制引用变量LIST_NEW:{0}"'\n'"原变量LIST1:{1}".format(list_deepcopy,list1))

del(list_deepcopy[2][3])
list2.remove(4) #remove移除指定元素的值，非索引号
print("深复制引用变量改变LIST_NEW:{0}"'\n'"原变量LIST1改变:{1}".format(list_deepcopy,list1)) #发生改变后互不影响
