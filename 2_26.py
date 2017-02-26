# -*-coding:utf-8 -*-
#Python自省学习

import sys
import inspect#inspect模块用于查看类的参数，模块代码等操作
def foo():pass
class Cat(object):
	def __init__(self,name='kitty'):
		self.name = name
	def sayHi(self):
		print self.name,'says Hi!'

cat = Cat()

print Cat.sayHi #unbound
print cat.sayHi #bound

cat = Cat('kitty')
print cat.name
cat.sayHi()

print dir(cat)#获取实例（OBJ）属性名，以列表形式返回
if hasattr(cat,'name'):#返回布尔值
	setattr(cat,'name','tiger')#same as:a.name = 'tiger'
print getattr(cat,'name')#same as:print a.name
print getattr(cat,'sayHi')
getattr(cat,'sayHi')()#getattr返回对应的属性（方法）

#isinstance(object,classinfo)检查OBJ是否为列举出的类型，返回布尔值，classinfo可以是元组或者列表

#模块（module）
#__doc__：文档字符串，没有返回None
#__name__:定义时的模块名
#__dict__：包含模块里可用的属性名-属性的字典
#__file__:模块的文件路径

#类（class）
#__doc__;__name__;__dict__
#__module__:该类定义的模块名，字符串形式的模块名
#__bases__:直接父类对象的元组（first parent）

#实例（instance）
#__dict__;
#__class__：该实例的类对象

#内建函数和方法（built-in functions and methods）
#内建（built-in）模块指的是以C编写的模块，通过sys.builtin_module_names查看内建模块
#__doc__;__name__;
#__self__：仅方法可用，绑定情况下：指向调用该方法的类或实例，否则为None
#__module__:函数或方法所在的模块名

#函数（function）——特指非内建函数
#__doc__;__name__;__module__;__dict__（在函数中保存属性意义不大）
#func_defaults:函数参数默认值元组
#func_globals:全局命名空间，只读，意义不大
#func_closure:仅当函数是一个闭包时有效：指向一个保存了所引用外部函数的变量cell元组，如果该函数为非内部函数，则为None；只读

#方法（method）
#__doc__;__name__;__module__;
#im_func:获得实际函数对象的引用，__func__
#im_self:绑定：获得调用该方法的类，未绑定，返回None；__self__
#im_Class：实际调用该方法的（实例的）类

#类方法(classmethod)：始终绑定的方法
#静态方法（staticmethod)：需要使用类名调用的函数

