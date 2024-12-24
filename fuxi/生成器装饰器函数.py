# # 列表推导式
# multiples = [i for i in range(30) if i % 3 == 0]
# print(multiples)
# # 字典推导式
# listdemo = ['Google','Runoob', 'Taobao']
# newdict = {key:len(key) for key in listdemo}
# print(newdict)
# #集合推导式
# a = {x for x in 'abracadabra' if x not in 'abc'}
# print(a)
# # 元组推导式(生成器表达式), 返回的结果是一个生成器对象。
# a= (x for x in range(1,10))
# print(a)
# print(tuple(a))

#迭代器
# 迭代器有两个基本的方法：iter() 和 next()
# list=[1,2,3,4]
# it = iter(list)    # 创建迭代器对象
# print (next(it))   # 输出迭代器的下一个元素
# print (next(it))
# 把一个类作为一个迭代器使用需要在类中实现两个方法 __iter__() 与 __next__() 
# class MyNumbers:
#   def __iter__(self):
#     self.a = 1
#     return self
#   def __next__(self):
#     if self.a <= 10:
#       x = self.a
#       self.a += 1
#       return x
#     else:
#       raise StopIteration
# myclass = MyNumbers()
# myiter = iter(myclass)
# for x in myiter:
#   print(x)


# 生成器
# 使用了 yield 的函数被称为生成器
#!/usr/bin/python3
# import sys
# def fibonacci(n): # 生成器函数 - 斐波那契
#     a, b, counter = 0, 1, 0
#     while True:
#         if (counter > n): 
#             return
#         yield a
#         a, b = b, a + b
#         counter += 1
# f = fibonacci(10) # f 是一个迭代器，由生成器返回生成
# while True:
#     try:
#         print (next(f), end=" ")
#     except StopIteration:
#         sys.exit()


# 函数
# 类型属于对象，对象有不同类型的区分，变量是没有类型的
# 不可变类型：类似 C++ 的值传递，如整数、字符串、元组。
# 如 fun(a)，传递的只是 a 的值，没有影响 a 对象本身。如果在 fun(a) 内部修改 a 的值，则是新生成一个 a 的对象。
# def change(a):
#     print(id(a))   # 指向的是同一个对象
#     a=10
#     print(id(a))   # 一个新对象
 
# a=1
# print(id(a))
# change(a)
# # 可变类型：类似 C++ 的引用传递，如 列表，字典。
# # 如 fun(la)，则是将 la 真正的传过去，修改后 fun 外部的 la 也会受影响
# # python 中一切都是对象，我们应该说传不可变对象和传可变对象。
# # 可变函数说明
# def changeme( mylist ):
#    "修改传入的列表"
#    mylist.append([1,2,3,4])
#    print ("函数内取值: ", mylist)
#    return
# # 调用changeme函数
# mylist = [10,20,30]
# changeme( mylist )
# print ("函数外取值: ", mylist)
# # 内外取值一样

# # 必需参数须以正确的顺序传入函数。调用时的数量必须和声明时的一样
# def printme( str ):
#    "打印任何传入的字符串"
#    print (str)
#    return
# # 调用 printme 函数，不加参数会报错
# printme()
# # 使用关键字参数允许函数调用时参数的顺序与声明时不一致
# def printme( str ):
#    "打印任何传入的字符串"
#    print (str)
#    return
# printme( str = "菜鸟教程")
# # 调用函数时，如果没有传递参数，则会使用默认参数
# def printinfo( name, age = 35 ):
#    "打印任何传入的字符串"
#    print ("名字: ", name)
#    print ("年龄: ", age)
#    return
# printinfo( name="runoob" )

# # 加了星号 * 的参数会以元组(tuple)的形式导入，存放所有未命名的变量参数
# # 可写函数说明
# def printinfo( arg1, *vartuple ):
#    "打印任何传入的参数"
#    print ("输出: ")
#    print (arg1)
#    print (vartuple)
# printinfo( 70, 60, 50 )
# # 加了两个星号 ** 的参数会以字典的形式导入
# def printinfo( arg1, **vardict ):
#    "打印任何传入的参数"
#    print ("输出: ")
#    print (arg1)
#    print (vardict)
# printinfo(1, a=2,b=3)

# lambda 来创建匿名函数。不再使用 def 语句这样标准的形式定义一个函数
# 可以将匿名函数封装在一个函数内，这样可以使用同样的代码来创建多个匿名函数
# def myfunc(n):
#   return lambda a : a * n
# mydoubler = myfunc(2)
# mytripler = myfunc(3)
# print(mydoubler(11))
# print(mytripler(11))
# 不带参数值的 return 语句返回 None
# f = lambda: "Hello, world!"
# print(f())  # 输出: Hello, world!
# lambda 函数通常与内置函数如 map()、filter() 和 reduce() 一起使用，以便在集合上执行操作

# map() 会根据提供的函数对指定序列做映射。
# 第一个参数 function 以参数序列中的每一个元素调用 function 函数，返回包含每次 function 函数返回值的迭代器
# numbers = [1, 2, 3, 4, 5]
# squared = list(map(lambda x: x**2, numbers))
# print(squared)  # 输出: [1, 4, 9, 16, 25]

# filter(function, iterable) 
# numbers = [1, 2, 3, 4, 5, 6, 7, 8]
# even_numbers = list(filter(lambda x: x % 2 == 0, numbers))
# print(even_numbers)  # 输出：[2, 4, 6, 8]

# # reduce() 函数会对参数序列中元素进行累积
# from functools import reduce
# numbers = [1, 2, 3, 4, 5]
# # 使用 reduce() 和 lambda 函数计算乘积
# product = reduce(lambda x, y: x * y, numbers)
# print(product)  # 输出：120

# 装饰器
# Python会自动将 target_function 作为参数传递给 decorator_function，然后将返回的 wrapper 函数替换掉原来的 target_function。
# def decorator_function(original_function):
#     def wrapper(*args, **kwargs):        
#         print("这里是在调用原始函数前添加的新功能")       
#         result = original_function(*args, **kwargs)     
#         print("这里是在调用原始函数后添加的新功能")  
#         return result
#     return wrapper
# # 使用装饰器
# @decorator_function
# def target_function(arg1, arg2):
#     print("我是原函数") # 原始函数的实现
# target_function(1,1)

# def repeat(n):
#     def decorator(func):
#         def wrapper(*args, **kwargs):
#             for _ in range(n):
#                 result = func(*args, **kwargs)
#             return result
#         return wrapper
#     return decorator
# @repeat(3)
# def greet(name):
#     print(f"Hello, {name}!")
# greet("Alice")

# 类装饰器
# class DecoratorClass:
#     def __init__(self, func):
#         self.func = func  
#     def __call__(self, *args, **kwargs):
#         # 在调用原始函数之前/之后执行的代码
#         result = self.func(*args, **kwargs)
#         # 在调用原始函数之后执行的代码
#         return result
# @DecoratorClass
# def my_function():
#     pass
# my_function()

# 。如果我们想在模块被引入时，模块中的某一程序块不执行，我们可以用__name__属性来使该程序块仅在该模块自身运行时执行
# 每个模块都有一个__name__属性，当其值是'__main__'时，表明该模块自身在运行，否则是被引入。
# 说明：__name__ 与 __main__ 底下是双下划线， _ _ 是这样去掉中间的那个空格