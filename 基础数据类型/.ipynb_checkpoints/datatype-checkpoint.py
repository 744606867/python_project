# #python 中所有为空、0的都是false
# while 1:
#     content = input("请输入一个整数：")
#     if content:
#         print(type(content))
#         print("您输入的整数是：", content)
#     else:
#         break


# #字符串格式化
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

# #字符串的常规操作
# str = "hello_world_{}"
# #字符串大小写转换  upper() lower() title() capitalize()  swapcase()
# print(str.upper())  #HELLO WORLD
# print(str.lower())  #hello world     
# print(str.title())  #Hello World
# print(str.capitalize())  #Hello world
# print(str.swapcase())    #HELLO WORLD
# print(str.format("name"))   #hello_world_name
# print(type(str.format("name").split("_"))) #<class 'list'>
# print(str.format("name").split("_"))    #['hello', 'world', 'name']
# print(str.find("world"))    #6
# print("world" in str)   #True
# print(str.replace("world", "python"))   #hello_python_

# #内置函数   len()  max()  min()  ord()  chr()  ascii()  bin()  oct()  hex()  round()  abs()  pow()  divmod()  sum()  sorted()  reversed()  enumerate()  zip()  all()  any()  filter()  map()  reduce()
# print(len(str)) #13 返回字符串的长度        
# print(max(str)) #w 返回字符串中最大的字符
# print(min(str)) #_ 返回字符串中最小的字符       
# print(ord("a"))  #97 返回字符的ASCII码
# print(chr(97))   #a  返回ASCII码对应的字符  
# print(ascii("a"))    #"'a'" 返回ASCII码对应的字符
# print(bin(10))   #0b1010 返回十进制数对应的二进制数
# print(oct(10))   #0o12 返回十进制数对应的八进制数
# print(hex(10))   #0xa 返回十进制数对应的十六进制数

# #列表   列表是有序的集合，可以存储任意类型的数据
# #定义列表   列表的元素可以是任意类型的数据，包括列表
# list1 = [1, 2, 3, 4, 5]    #定义一个包含5个元素的列表
# list2 = list(range(1, 6))   #通过range()函数生成一个包含5个元素的列表       
# list3 = [1, "hello", True, [1, 2, 3]]  #定义一个包含4个元素的列表
# list4 = []  #定义一个空列表
# for i in list3:
#     if type(i) == list:
#         for j in i:
#             print(j)
#     print(i)

# #元组   元组是有序的集合，一旦创建就不能修改
# #定义元组   元组的元素可以是任意类型的数据，包括元组        
# tuple1 = (1, 2, 3, 4, 5)    #定义一个包含5个元素的元组
# tuple2 = tuple(range(1, 6)) #通过range()函数生成一个包含5个元素的元组   
# tuple3 = (1, "hello", True, (1, 2, 3))  #定义一个包含4个元素的元组
# tuple4 = () #定义一个空元组
# for i in tuple3:
#     if type(i) == tuple:
#         for j in i:
#             print(j)
#     print(i)


# #set 集合   集合是无序的，元素不重复的数据集合
# #定义集合   集合的元素可以是任意类型的数据，但是不支持列表和字典        
# set1 = {1, 2, 3, 4, 5}  #定义一个包含5个元素的集合
# set2 = set(range(1, 6)) #通过range()函数生成一个包含5个元素的集合  
# set3 = {1, "hello", True}   #定义一个包含3个元素的集合
# print(len(set3))   #<class 'set'>
# for i in set3:
#     print(i)    #输出集合中的元素   1  hello  True
# # set3.add(2) #向集合中添加元素   {1, 2, 'hello', True}
# # set3.remove(2)  #从集合中删除元素   {1, 'hello', True}          
# # set3.clear()    #清空集合   set()   


# #字典   字典是无序的键值对集合  *********
# #定义字典   字典的键必须是不可变类型，值可以是任意类型的数据
# dict1 = {"name": "张三", "age": 18}  #定义一个包含2个键值对的字典
# dict2 = dict(name="李四", age=20)   #通过dict()函数定义字典
# dict3 = dict([("name", "王五"), ("age", 22)])  #通过列表定义字典    
# print(dict1[age])  #18


# #字符集和编码   字符集是字符的集合，编码是字符集中字符的二进制表示
# #常见的字符集：ASCII、Unicode、UTF-8、GBK
# #ASCII编码：只能表示英文字符，一个字符占一个字节
# #Unicode编码：可以表示全球所有字符，一个字符占两个字节  0-127是ASCII码，128-65535是Unicode码    
# #UTF-8编码：是Unicode的实现方式之一，一个字符占1-4个字节
# #GBK编码：是中国的中文编码，一个字符占2个字节   0-127是ASCII码，128-255是GBK码
# #字符集和编码的转换   encode()  decode()
# str = "hello" #定义一个字符串  hello  
# bytes = str.encode("utf-8") #将字符串转换为字节串  b'hello'
# str1 = bytes.decode("utf-8") #将字节串转换为字符串  hello 
# print(bytes)
    

# #运算符   算术运算符  比较运算符  逻辑运算符  赋值运算符  位运算符  成员运算符  身份运算符
# #算术运算符   +  -  *  /  //  %  ** 
# #比较运算符   ==  !=  >  <  >=  <=
# #逻辑运算符   and  or  not
# #赋值运算符   =  +=  -=  *=  /=  //=  %=  **=
# #位运算符    &  |  ^  ~  <<  >>