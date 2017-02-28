# -*- coding:utf-8 -*-
#python3.5无法得到预期效果

# class ObjectCreator(object):
	# pass

# my_object = ObjectCreator()
# print(my_object)#<__main__.ObjectCreator object at 0x.....>

#类仍然是对象，仍然能够将其赋值给变量，赋值，添加属性，或者作为函数参数传入
# def echo(obj):
	# print(obj)

# echo(ObjectCreator)
# print(hasattr(ObjectCreator,"new_attribute")) #False
# ObjectCreator.new_attribute = "foo"
# print(hasattr(ObjectCreator,"new_attribute")) # True
# ObjectCreatorMirror = ObjectCreator
# print(ObjectCreatorMirror.new_attribute) # foo
# print(ObjectCreatorMirror()) #<__main__.ObjectCreator object at 0x.....>

# def choose_class(name):
	# if name == "foo":
		# class Foo(object)
			# pass
		# return Foo
	# else:
		# class Bar(object):
			# pass
		# return Bar

# MyClass = choose_class('foo')
# print(MyClass)
#<class '__main__.Fll'>
# print(MyClass())
#<__main__.Foo object at 0x....>
#上述只是“伪动态”的创建类，因为类是对象，所以当使用到了class关键词时，Python自动创建了
#类，当然，有自动的方法——type.type除了能够判定对象的类型之外，还能够创建类

#type(类名，用于继承的类元组（可以为空），对应的属性与属性值的字典）
# class MyShinyClass(object):
	# pass

# MyShinyClass = type('MyShinyClass',(),{})
# Foo = type('Foo',(),{'bar':True})
# FooChild = type('FooChild',(Foo,),{})
#添加方法就如同添加属性一样
# def echo_bar(self):
	# print(self.bar)
# FooChild = type('FooChild',(Foo,),{'echo_bar':echo_bar})
# my_foo = FooChild()
# my_foo.echo_bar()# True
#只要定义了方法，就可以添加不受限制的类方法
#所以，当使用关键字class时，Python所做的正如上面所说，利用type动态创建类，同时，也是
#通过元类来定义

#元类，是通过创建这些类对象的类，即类的类；类，用来创建对象，而元类，用来创建类
#元类可以称为类工厂
#type是Python内建的元类

#创建自己的元类，使用__metaclass__属性
#当在定义一个类时添加了__metaclass__属性时，Python将会利用元类来创建该类
#在使用关键字class定义类时，如class Foo(object)，在生成类对象之前，Python首先
#会检查类定义中是否有__metaclass__属性，如果没有，则会使用type函数来生成类

#注意！！！在定义中寻找__metaclass__属性时，若没有找到，Python会在模块中寻找该属性
#即若在一个模块中定义了__metaclass__，则所有定义的类都会按照__metaclass__来创建



#定制metaclasses
# def upper_attr(future_class_name,future_class_parents,future_class_attrs):
	# uppercase_attr={}
	# for name,val in future_class_attrs.items():
		# if not name.startswith("__"):
			# uppercase_attr[name.upper()] = val 
		# else:
			# uppercase_attr[name] = val
	# return type(future_class_name,future_class_parents,uppercase_attr)

# __metaclass__ = upper_attr

# class Foo():
	# bar = "bip"

# print hasattr(Foo,"bar")#False
# print hasattr(Foo,"BAR")#True
# f = Foo()
# print f.BAR# "bip"
#使用真正的元类来创建类
# class UpperAttrMetaclass(type):
	# def __new__(upperattr_metaclass,future_class_name,future_class_parents,future_class_attr):

		# uppercase_attr = {}
		# for name,val in future_class_attr.items():
			# if not name.startswith('__'):
				# uppercase_attr[name.upper()] = val
			# else:
				# uppercase_attr[name] = val
		# return type(future_class_name,future_class_parents,uppercase_attr)
#严格意义上不是面向对象编程，我们直接调用了type函数并且我们并没有重构父类type的__new__方法

# class UpperAttrMetaclass(type):
	# def __new__(upperattr_metaclass,future_class_name,future_class_parents,future_class_attr):
	
		# uppercase_attr = {}
		# for name,val in future_class_attr.items(): #future_class_attr与__dict__有关，返回一个字典包含了属性和方法
			# if not name.startswith('__'):
				# uppercase_attr[name.upper()]=val
			# else:
				# uppercase_attr[name] = val
		# return type.__new__(upperattr_metaclass,future_class_name,future_class_parents,uppercase_attr)
		#return super(UpperAttrMetaclass,upperattr_metaclass).__new__(upperattr_metaclass,future_class_name,future_class_parents,uppercase_attr)
#对于upperattr_metaclass，就如同定义类方法的self参数一样，是__new__方法的固定接收
# class Foo():
	# __metaclass__  = UpperAttrMetaclass
	# bar = "bip"
# print hasattr(Foo,"bar")#False
# print hasattr(Foo,"BAR")#True
#总结：元类，拦截类的创建；修改类；返回被修改后的类
#__metaclass__可以接受任何可调用对象，但使用类具有更多的好处，比如OOP编程，代码直观易读
#元类在ORM中占据了重要的角色
#对于任何类，都是元类的实例，但type是最高的类，即所有类均衍生自type
#对于修改类，可以使用猴子补丁以及装饰器。

#demo
class Demo(type):
	def __new__(cls,cls_name,cls_parents,cls_attr):
		def addWord(dict,word,attr):
			dict.setdefault(word,attr)
		def auto_method(self):
			print "this is a auto_method"
		new_attr={}
		for name,val in cls_attr.items():
				new_attr[name] = val
		addWord(new_attr,"auto_method",auto_method)
		addWord(new_attr,"attr",True)
		return type.__new__(cls,cls_name,cls_parents,new_attr)

class demo(object):
	__metaclass__ = Demo
	bar = "bip"

print hasattr(demo,"bar") # True
print hasattr(demo,"attr")# True
print demo.attr # True
demo().auto_method() # "thisi is a auto_method"

#利用元类编写ORM

class Field(object):
	def __init__(self,name,column_type):
		self.name = name
		self.column_type = column_type
	def __str__(self):
		return '<%s:%s>' % (self.__class__.__name__,self.name)

class StringField(Field):
	def __init__(self,name):
		super(StringField,self).__init__(name,'varchar(100)')

class IntegerField(Field):
	def __init__(self,name):
		super(IntegerField,self).__init__(name,'bigint')

class ModelMetaclass(type):
	def __new__(cls,name,bases,attrs):
		if name =="Model":
			return type.__new__(cls,name,bases,attrs)
		print 'Found model:%s' % name
		mappings = dict()
		for k,v in attrs.items():
			if isinstance(v,Field):
				print 'Found mapping:%s==> %s' %(k,v)
				mappings[k]=v
		for k in mappings.keys():
			sttrs.pop(k)
		attrs['__mappings__'] = mappings
		attrs['__table__'] = name
		return type.__new__(cls,name,bases,attrs)

class Model(dict,metaclass=ModelMetaclass):
	def __init__(self,**kwargs):
		super(Model,self).__init__(**kwargs)
	def __getattr__(self,key):
		try:
			return self[key]
		except KeyError:
			raise AttributeError
	def __setattr__(self,key,value):
		self[key] = value
	def save(self):
		fields = []
		params = []
		args = []
		for k,v in self.__mapping__.items():
			fields.append(v.name)
			params.append('?')
			args.append(getattr(self,k,None))
		sql = 'insert into %s (%s) values (%s)' % (self.__table__, ','.join(fields), ','.join(params))
		print 'SQL: %s' % sql
		print 'ARGS: %s' % str(args)