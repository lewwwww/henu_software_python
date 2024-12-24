

# word = '字符串'
# sentence = r"这是一个句子。\n"
# paragraph = """这是一个段落，
# 可以由多行组成"""
# print(word)
# print(sentence)
# print(paragraph)

# input("\n\n按下 enter 键后退出。")


# from sys import argv,path  #  导入特定的成员
# print('================python from import===================================')
# print('path:',path) # 因为已经导入path成员，所以此处引用时不需要加sys.path


# class A:
#     pass

# class B(A):
#     pass
# isinstance(A(), A)    # returns True
# type(A()) == A       # returns True
# isinstance(B(), A)    # returns True
# type(B()) == A        # returns False
# # 因为B继承了A，所以B是A的子类，所以B()是A的实例，所以isinstance(B(), A)返回True，
# # type()不会认为子类是一种父类类型。
# # isinstance()会认为子类是一种父类类型。
# issubclass(B, A) # returns True
# issubclass(B, B) # returns False
# issubclass(A, B) # returns False
# issubclass(A, A) # returns True
# # issubclass()会认为子类是一种父类类型。


# def reverseWords(input):
#     inputWords = input.split(" ")
#     print(inputWords)#list
#     inputWords = inputWords[-1::-1]
#     print(inputWords)#list
#     output = ' '.join(inputWords)
#     print(output)#str
#     return output
# print(reverseWords("I like runoob"))




#列表是有序的对象集合，字典是无序的对象集合。两者之间的区别在于：字典当中的元素是通过键来存取的，而不是通过偏移存取。
#键(key)必须使用不可变类型。在同一个字典中，键(key)必须是唯一的。
#构造函数 dict() 可以直接从键值对序列中构建字典如下：
#dict([('Runoob', 1), ('Google', 2), ('Taobao', 3)])
#{'Runoob': 1, 'Google': 2, 'Taobao': 3}
# {x: x**2 for x in (2, 4, 6)}
# {2: 4, 4: 16, 6: 36}字典推导式

#eval() 函数用来执行一个字符串表达式，并返回表达式的值一个新对象。
#eval(expression[, globals[, locals]])
#expression -- 表达式。
#globals -- 变量作用域，全局命名空间，如果被提供，则必须是一个字典对象。
#locals -- 变量作用域，局部命名空间，如果被提供，可以是任何映射对象。


 
# /除以，//整除取小的
# &,|,~,^,<<左移  位运算符
# and 拥有更高优先级
# x is y, 类似 id(x) == id(y) , 如果引用的是同一个对象则返回 True，否则返回 False
# is 用于判断两个变量引���对象是否为同一个， == 用于判断引用变量的值是否相等
# >>>a = [1, 2, 3]
# >>> b = a 
# >>> b is a 
# True
# >>> b == a
# True
# >>> b = a[:] #copy() 函数用于复制列表，类似于 a[:]
# >>> b is a
# False
# >>> b == a
# True
 

# Number
# print(10/2)#5.0
# print(7//2)#3
# print(7.0//2)#3.0


# str
# 内置函数
# str = "this is string Example From Runoob....wow!!!"
# print ("str.capitalize() : ", str.capitalize())# 将字符串的第一个字母变成大写，其他字母变小写
# str.count(sub, start= 0,end=len(string))
# find(str, beg=0, end=len(string)) 检测 str 是否包含在字符串中，如果包含返回开始的索引值，否则返回-1
# index(str, beg=0, end=len(string))跟find()方法一样，只不过如果str不在字符串中会报一个异常
# join(seq)以指定字符串作为分隔符，将 seq 中所有的元素(的字符串表示)合并为一个新的字符串
# s="" ;print(len( s )) #0
# str = "this is string example....wow!!!"
# print (str.split('i',1))   # 以 i 为分隔符 ['th', 's is string example....wow!!!']
# print (str.split('w'))     # 以 w 为分隔符 ['this is string example....', 'o', '!!!']


# list
# 访问
 # list.index(x[, start[, end]])该方法返回查找第一个匹配项的索引位置，如果没有找到对象则抛出异常
  # list.reverse()
#   reverse -- 排序规则，reverse = True 降序， reverse = False 升序（默认）
# 更新 
 # list.append(obj)在列表末尾添加新的对象
 # list.extend(seq)seq -- 元素列表，可以是列表、元组、集合、字典，若为字典,则仅会将键(key)作为元素依次添加至原列表的末尾
# list1 = ['Google', 'Runoob', 'Taobao']
# list2=list(range(5)) # 创建 0-4 的列表
# list1.extend(list2)  # 扩展列表
# print ("扩展后的列表：", list1)
# 删除del list[2]
	# list.pop([index=-1])移除列表中的一个元素（默认最后一个元素），并且返回该元素的值
    	# list.remove(obj)移除列表中某个值的第一个匹配项
# + 号用于组合列表，* 号用于重复列表
# 列表比较，导入 operator 模块
# import operator
# a = [1, 2]
# b = [2, 3]
# c = [2, 3]
# print("operator.eq(a,b): ", operator.eq(a,b))
# print("operator.eq(c,b): ", operator.eq(c,b))


# tuple
# tup='a','b'不加括号也许
# print(type(tup))
# 元组中只包含一个元素时，需要在元素后面添加逗号 ,
# 元组中的元素值是不允许删除的，但我们可以使用del语句来删除整个元组
# 元组的不可变指的是元组所指向的内存中的内容不可变，重新赋值的元组 tup，绑定到新的对象了，不是修改了原来的对��
# tup = ('r', 'u', 'n', 'o', 'o', 'b')
# print(id(tup))     # 查看内存地址
# tup = (1,2,3)
# print(id(tup))
 

# dict
# 删除
# del tinydict['Name'] # 删除键 'Name'
# tinydict.clear()     # 清空字典
# del tinydict         # 删除字典
# pop() 方法删除字典 key（键）所对应的值，返回被删除的值
# 如果 key 存在 - 删除字典中对应的元素
# 如果 key 不存在 - 返回设置指定的默认值 default
# 如果 key 不存在且默认值 default 没有指定 - 触发 KeyError 异常
# 创建
# dict.fromkeys(seq[, value])seq -- 字典键值列表，value -- 可选参数, 设置键序列（seq）对应的值，默认为 None
# 索引
# get(key) 方法在 key（键）不在字典中时，可以返回默认值 None 或者设置的默认值。
# dict[key] 在 key（键）不在字典中时，会触发 KeyError 异常
# 更新
#dict.update(dict2)  update() 函数把字典参数 dict2 的 key/value(键/值) 对更新到字典 dict 里


# set
#创建一个空集合必须用 set() 而不是 { }，因为 { } 是用来创建一个空字典
#集合中的元素不会重复
# 添加（加上后仍然有序）
# s.add( x )将元素 x 添加到集合 s 中，如果元素已存在，则不进行任何操作
# s.update( x )参数可以是列表，元组，字典等
# 删除
# s.remove( x )将元素 x 从集合 s 中移除，如果元素不存在，则会发生错误。
# s.discard( x )如果元素不存在，不会发生错误
# s.pop() 会对集合进行无序的排列，然后将这个无序排列集合的左面第一个元素进行删除

# 在 Python 中没有 do..while 循环
# if None:
#     print("q")
# for i in [1, 0]:
#     print(i+1)


# >>> print('{}网址： "{}!"'.format('菜鸟教程', 'www.runoob.com'))
# 菜鸟教程网址： "www.runoob.com!"
# print('{0} 和 {1}'.format('Google', 'Runoob'))
# Google 和 Runoob
# print('{name}网址： {site}'.format(name='菜鸟教程', site='www.runoob.com'))
# 菜鸟教程网址： www.runoob.com
# import math
# print('常量 PI 的值近似为 {0:.3f}。'.format(math.pi))
# 常量 PI 的值近似为 3.142。


# 为了读取一个文件的内容，调用 f.read(size), 这将读取一定数目的数据, 然后作为字符串或字节对象返回。
# f.readline() 会从文件中读取单独的一行。换行符为 '\n'。f.readline() 如果返回一个空字符串, 说明已经已经读取到最后一行
# f.readlines() 将返回该文件中包含的所有行。
# f.write(string) 将 string 写入到文件中, 然后返回写入的字符数
# f.tell() 用于返回文件当前的读/写位置（即文件指针的位置）。文件指针表示从文件开头开始的字节数偏移量。f.tell() 返回一个整数，表示文件指针的当前位置
# f.seek(offset, whence) 用于移动文件指针到指定位置。
# offset 表示相对于 whence 参数的偏移量，from_what 的值, 如果是 0 表示开头, 如果是 1 表示当前位置, 2 表示文件的结尾，例如：
# seek(x,0) ： 从起始位置即文件首行首字符开始移动 x 个字符
# seek(x,1) ： 表示从当前位置往后移动x个字符
# seek(-x,2)：表示从文件的结尾往前移动x个字符
# from_what 值为默认为0，即文件开头
# 当处理一个文件对象时, 使用 with 关键字是非常好的方式。在结束后, 它会帮你正确的关闭文件。



#  try 语句可能包含多个except子句，分别来处理不同的特定的异常。最多只有一个分支会被执行
# 一个except子句可以同时处理多个异常，这些异常将被放在一个括号里成为一个元组
# 使用 raise 语句抛出一个指定的异常，raise 唯一的一个参数指定了要被抛出的异常。它必须是一个异常的实例或者是异常的类（也就是 Exception 的子类
# 创建一个新的异常类来拥有自己的异常。异常类继承自 Exception 类，可以直接继承，或者间接继承，
# 
# 
# 测试
a = 2   # 赋值 不需要var a=1
# def add():
# for i in range(3):循环
def f(): pass
print(type(f()))#返回None

# import keyword
# print(keyword.kwlist)

#python的变量要先声明再使用吗
#随时命名，随时赋值，随时使用
# Python 是动态类型语言，这意味着变量的类型是在运行时确定的，而不是在编译时。你可以在程序中随时为变量赋值，而不需要事先声明其类型。

# print(type(eval('45')))
# <class 'int'>

s1 = "企鹅"
s2 = "超级游泳健将"
print("{0:^4}:{1:!<9}".format(s1, s2))
# {0:^4}：将 s1 居中对齐，宽度为 4。
# {1:!<9}：将 s2 左对齐，宽度为 9，使用 ! 填充。
s = '百花齐放'
formatted_string = "{0:3}".format(s)  # 右对齐，宽度为3
print(formatted_string)
# "{0:3}".format(s)：使用 format() 方法将字符串 s 插入到格式化字符串中。这里的 :3 表示希望字符串的宽度为 3，但由于 s 的长度大于 3，所以它会完整显示 s 的内容。


result = 'a' + str(1)  # 结果为 'a1'
print(result)
# print('a'+1)错误

# 三引号之间的内容是多行字符串，而不是注释。虽然它们可以用作文档字符串，但它们仍然是字符串类型。
# 在 UTF-8 编码中，一个汉字通常需要占用 3 个字节。

# 正则表达式模块match()方法是从字符串的开始匹配特定模式,而search()方法是整个字符串中寻找模式,这两个方法如果匹配成功则返回match对象,匹配失败则返回空值None
# 使用正则表达式可以方便地对字符串进行分割，并且可以指定多个分隔符，而字符串对象的 split() 方法只能使用单一的分隔符。


















