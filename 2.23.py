# -*-coding:utf-8 -*-

# def foo(x):
	# print "executing foo(%s)" %(x)

# class A(object):
	# def foo(self,x):
		# print "executing foo(%s,%s)" %(self,x)
	
	# @classmethod
	# def class_foo(cls,x):
		# print "executing class_foo(%s,%s)" %(cls,x)

	# @staticmethod
	# def static_foo(x):
		# print "executing static_foo %s" %x

# a=A() 
# a.foo("b") # 实例和"b" 实例方法，传递实例
# A.class_foo("b")#类和"b" 类方法，传递类
# A.static_foo("b")#"b" 静态类方法，无需传递

# class Person:
	# name = "aaa"

# p1 = Person()
# p2 = Person()
# p1.name="bbb" #对实例p1增加了实例变量，即p1拥有了实例属性name
# print p1.name # bbb
# print hasattr(p1,"name") # True
# print p2.name #p2没有实例属性，则会在类中寻找，故输出为aaa
# print hasattr(p2,"name") # True 类属性有name
# print Person.name #aaa


class Person:
	name = []
p1 = Person()
p2 = Person()
p1.name.append(1)
print p1.name #[1]
print p2.name #[1]
print Person.name#[1]
