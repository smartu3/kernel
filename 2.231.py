# -*-coding:utf-8 -*-

class Itr(object):
	def __init__(self):
		self.result = ['a','b','c','d']
		self.i = iter(self.result)
	
	def __call__(self):
		res = next(self.i)
		print "__call__ called,which would return %s" %res
		return res
	
	def __iter__(self):
		print "__iter__ called"
		return iter(self.result)
#iter函数返回可迭代对象
itr = Itr()
i1 = iter(itr,'c')#itr可调用，返回一个可调用iterator，即每次调用__call__函数；;迭代出c立马停止
print "i1=%s" %i1

i2 = iter(itr)#itr可迭代，__iter__函数返回一个iteration,即调用了定义的__iter__函数，（返回了一个listiterator）
print "i2=%s" %i2#即当使用iter函数时，会查找参数对象是否包含__iter__方法并能返回一个iterator！

for i in i1:
	print i
for i in i2:
	print i

#要想真正定义一个迭代器类iterator类，需要定义__next__方法，每次返回下一个值

class Next(object):
	def __init__(self,data =1):
		self.data = data 
	def __iter__(self):#定义__iter__方法，当调用iter(Next(data))时，可以实现返回实例本身，实例本身定义了__next__方法，即是一个iterator！
		return self 
	def next(self):#注意python3中，__next__;python2中为next。
		print "__next__ called"
		if self.data >5:
			raise StopIteration
		else:
			self.data +=1
			return self.data

for i in Next(3):
	print i  # 4..5..6..StopIteration
for i in iter(Next(3)):
	print i #同上