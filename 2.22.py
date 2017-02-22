# -*- coding:utf-8 -*-

a = 1
def fun(a):
	a = 2
fun(a)
print a #1

b=[]
def func(a):
	a.append(1)
func(b)

print b # [1]

a = 1
def fun1(a):
	print "func_in",id(a)
	a = 2
	print "re-point",id(a),id(2)
print "func_out",id(a),id(1)
fun1(a)
print a 