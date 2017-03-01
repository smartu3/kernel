# -*- coding:utf-8 -*-

#多线程
#threading模块
#任何进程启动时均会启动一个线程，该线程为主线程。threading模块有个current_thread()函数，返回当前
#线程实例，主线程实例名字为MainThread，子线程名字在创建时指定（意义不大）

#多线程与多进程最大的不同：多进程中每一份变量均有各自的拷贝，互不影响；
#砸多线程中，所有变量由所有线程共享，任何一个变量被修改，会体现在所有的线程里，在多线程中修改数据
#是一件危险的事

#在线程的不断切换间，有可能导致某个变量的计算或赋值没有完成，所以需要添加线程锁lock，来保证完成
#线程锁只有一个，所以必须在锁定之后，释放
import threading
lock = threading.Lock()
balance = 0

def run_thread(n):
	for i in range(100000):
		lock.acquire()
		try:
			change_it(n)
		finally:
			lock.release()

#锁的好处，确保关键代码段完整执行；坏处：包含锁的代码段无法并发
#GIL全局锁，导致无法在多线程中利用多核；多线程在Python中只能交替进行，无法同时并发
#Python中多线程效率低下，但多进程无影响，进程各自拥有独立的GIL锁

#线程局部变量（ThreadLocal）
#多线程处理变量时，全局变量需要加锁，而局部变量与其他线程互不干扰
#解决局部变量的传递问题，可以建立一个全局变量dict，以线程为key，获取对应value
#ThreadLocal做的就是上面所提的事
import threading
local_school = threading.local()

def process_Student():
	std = local_shcool.student
	print '%s in %s' %(std,threading.current_thread().name)

def process_thread(name):
	local_school.student = name
	process_student()

t1 = threading.Thread(target= process_thread,args=('Alice',),name='Thread-A')
t2 = threading.Thread(target= process_thread,args=('Bob',),name = 'Thread-B')
t1.start()
t2.start()
t1.join()
t2.join()