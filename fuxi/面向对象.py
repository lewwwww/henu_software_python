# #!/usr/bin/python3
# class MyClass:
#     """一个简单的类实例"""
#     i = 12345
#     def f(self):
#         return 'hello world'
# # 实例化类
# x = MyClass()
# # 访问类的属性和方法
# print("MyClass 类的属性 i 为：", x.i)
# print("MyClass 类的方法 f 输出为：", x.f())

# 类有一个名为 __init__() 的特殊方法（构造方法），该方法在类实例化时会自动调用
# 类的方法与普通的函数只有一个特别的区别——它们必须有一个额外的第一个参数名称, 按照惯例它的名称是 self,self 代表的是类的实例，代表当前对象的地址
# def 关键字来定义一个方法，必须包含参数 self, 且为第一个参数，self 代表的是类的实例
# 子类（派生类 DerivedClassName）会继承父类（基类 BaseClassName）的属性和方法。
# 多继承需要注意圆括号中父类的顺序，若是父类中有相同的方法名，而在子类使用时未指定，python从左至右搜索 即方法在子类中未找到时，从左到右查找父类中是否包含方法
# class people:
#     #定义基本属性
#     name = ''
#     age = 0
#     #定义私有属性,私有属性在类外部无法直接进行访问
#     __weight = 0
#     #定义构造方法
#     def __init__(self,n,a,w):
#         self.name = n
#         self.age = a
#         self.__weight = w
#     def speak(self):
#         print("%s 说: 我 %d 岁。" %(self.name,self.age))
# #单继承示例
# class student(people):
#     grade = ''
#     def __init__(self,n,a,w,g):
#         #调用父类的构函
#         people.__init__(self,n,a,w)
#         self.grade = g
#     #覆写父类的方法
#     def speak(self):
#         print("%s 说: 我 %d 岁了，我在读 %d 年级"%(self.name,self.age,self.grade))
# #另一个类，多继承之前的准备
# class speaker():
#     topic = ''
#     name = ''
#     def __init__(self,n,t):
#         self.name = n
#         self.topic = t
#     def speak(self):
#         print("我叫 %s，我是一个演说家，我演讲的主题是 %s"%(self.name,self.topic))
# #多继承
# class sample(speaker,student):
#     a =''
#     def __init__(self,n,a,w,g,t):
#         student.__init__(self,n,a,w,g)
#         speaker.__init__(self,n,t)
# test = sample("Tim",25,80,4,"Python")
# test.speak()   #方法名同，默认调用的是在括号中参数位置排前父类的方法
# super() 函数是用于调用父类(超类)的一个方法
# 子类需要自动调用父类的方法：子类不重写__init__()方法，实例化子类后，会自动调用父类的__init__()的方法。
# 子类不需要自动调用父类的方法：子类重写__init__()方法，实例化子类后，将不会自动调用父类的__init__()的方法。
# 子类重写__init__()方法又需要调用父类的方法：使用super关键词
# class FooParent(object):
#     def __init__(self):
#         self.parent = 'I\'m the parent.'
#         print ('Parent')
    
#     def bar(self,message):
#         print ("%s from Parent" % message)
 
# class FooChild(FooParent):
#     def __init__(self):
#         # super(FooChild,self) 首先找到 FooChild 的父类（就是类 FooParent），然后把类 FooChild 的对象转换为类 FooParent 的对象
#         super(FooChild,self).__init__()    
#         print ('Child')
        
#     def bar(self,message):
#         super(FooChild, self).bar(message)
#         print ('Child bar fuction')
#         print (self.parent)
 
# if __name__ == '__main__':
#     fooChild = FooChild()
#     fooChild.bar('HelloWorld')
# 
# 
# 
# 
# 方法重写
#!/usr/bin/python
# -*- coding: UTF-8 -*-
#  #!/usr/bin/python3
# class Parent:        # 定义父类
#    def myMethod(self):
#       print ('调用父类方法')
 
# class Child(Parent): # 定义子类
#    def myMethod(self):
#       print ('调用子类方法')
 
# c = Child()          # 子类实例
# c.myMethod()         # 子类调用重写方法
# super(Child,c).myMethod() #用子类对象调用父类已被覆盖的方法
# 
# 
# 
# 
# __private_attrs：两个下划线开头，声明该属性为私有
# __private_method：两个下划线开头，声明该方法为私有方法，只能在类的内部调用
# __init__ : 构造函数，在生成对象时调用
# __del__ : 析构函数，释放对象时使用
# class Site:
#     def __init__(self, name, url):
#         self.name = name       # public
#         self.__url = url   # private
 
#     def who(self):
#         print('name  : ', self.name)
#         print('url : ', self.__url)
 
#     def __foo(self):          # 私有方法
#         print('这是私有方法')
 
#     def foo(self):            # 公共方法
#         print('这是公共方法')
#         self.__foo()
 
# x = Site('菜鸟教程', 'www.runoob.com')
# x.who()        # 正常输出
# x.foo()        # 正常输出
# x.__foo()      # 报错
# 
# 
# 运算符重载
# class Vector:
#    def __init__(self, a, b):
#       self.a = a
#       self.b = b
#    def __str__(self):
#       return 'Vector (%d, %d)' % (self.a, self.b)
#    def __add__(self,other):
#       return Vector(self.a + other.a, self.b + other.b)
# v1 = Vector(2,10)
# v2 = Vector(5,-2)
# print (v1 + v2)
# print(v1)
# 
# 当内部作用域想修改外部作用域的变量时，就要用到 global 和 nonlocal 关键字
num = 1
def fun1():
    global num  # 需要使用 global 关键字声明
    print(num) 
    num = 123
    print(num)
fun1()
print(num)


def outer():
    num = 10
    def inner():
        nonlocal num   # nonlocal关键字声明
        num = 100
        print(num)
    inner()
    print(num)
outer()

 
a = 10
def test():
    global a
    a = a + 1
    print(a)
test()
# 也可以通过函数参数传递：
a = 10
def test(a):
    a = a + 1
    print(a)
test(a)
# 



# >>> import random
# >>> random.choice(['apple', 'pear', 'banana'])
# 'apple'
# >>> random.sample(range(100), 10)   # sampling without replacement
# [30, 83, 16, 4, 8, 81, 41, 50, 18, 33]
# >>> random.random()    # random float
# 0.17970987693706186
# >>> random.randrange(6)    # random integer chosen from range(6)
# 4
# randrange()从 range(start, stop, step) 返回一个随机选择的元素。
# randint(a,b)返回随机整数 N 满足 a <= N <= b
# choice()从非空序列 seq 返回一个随机元素。 如果 seq 为空，则引发 IndexError
# random()从非空序列 seq 返回一个随机元素。 如果 seq 为空，则引发 IndexError






# import datetime
# #获取当前日期和时间
# current_datetime = datetime.datetime.now()
# print(current_datetime)
# # 获取当前日期
# current_date = datetime.date.today()
# print(current_date)
# # 格式化日期
# formatted_datetime = current_datetime.strftime("%Y-%m-%d %H:%M:%S")
# print(formatted_datetime)  # 输出：2023-07-17 15:30:45



 





















































































































































