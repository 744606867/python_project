# python 中所有为空、0的都是false
# while 1:
#     content = input("请输入一个整数：")
#     if content:
#         print(type(content))
#         print("您输入的整数是：", content)
#     else:
#         break


# 字符串格式化
# name = "张三"
# age = 18
# content = "姓名：{}，年龄：{}".format(name, age)    #位置参数
# content1 = "姓名：{0}，年龄：{1}".format(name, age)     #位置参数
# content2 = "姓名：{name}，年龄：{age}".format(name=name, age=age)   #关键字参数
# content3 = f"姓名：{name}，年龄：{age}"     #f-string   
# print(content)


# #索引和切片
# #语法：字符串[开始索引:结束索引:步长]
# str1 = "hello world"
# print(str1[0])  #获取第一个字符
# print(str1[-1]) #获取最后一个字符
# print(str1[0:5])    #获取前5个字符
# print(str1[6:])     #获取第6个字符以后的字符 
# print(str1[:5])     #获取前5个字符
# print(str1[::2])    #每隔一个字符获取一个字符
# print(str1[::-1])   #倒序输出
# print(str1[:])      #获取所有字符

#字符串的常规操作
str = "hello_world_{}"
#字符串大小写转换  upper() lower() title() capitalize()  swapcase()
print(str.upper())  #HELLO WORLD
print(str.lower())  #hello world     
print(str.title())  #Hello World
print(str.capitalize())  #Hello world
print(str.swapcase())    #HELLO WORLD
print(str.format("name"))   #hello_world_name
print(type(str.format("name").split("_"))) #<class 'list'>
print(str.format("name").split("_"))    #['hello', 'world', 'name']
print(str.find("world"))    #6
print("world" in str)   #True
print(str.replace("world", "python"))   #hello_python_


    