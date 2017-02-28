# -*- coding:utf-8 -*-
#进程
#对操作系统来说，一个任务就是一个进程(process)
#进程内的子任务称为线程，每一个进程至少有一个线程
#进程/线程的伪同时运行，是操作系统在不同的进程/线程之间进行切换；真正的同时进行多任务需要多核CPU

#同时执行多个任务：
#启动多个进程，每个进程只有一个线程，可以多个进程一块执行多个任务
#启动一个进程，在一个进程内启动多个线程，多个线程执行多个任务
#多进程，多线程，复杂，少用
#线程是最小的执行单元，进程至少包含一个线程，调度线程与进程的执行，由操作系统决定

#多进程multiprocessing
#unix/linux中：fork()函数调用一次，返回两次，在父进程与子进程间分别返回一次
#子进程返回0，父进程返回子进程的ID，父进程可以fork出多个子进程，所以需要返回子进程ID，而子进程
#调用getppid()可以得到父进程的ID

# import os 

# print "Process (%s) start .." % os.getpid()
# pid = os.fork()
# if pid == 0:
	# print "I am child process %s and my parent is %s" %(os.getpid(),os.getppid)
# else:
	# print "I am parent process %s and my child is %s"%(os.getpid(),pid)

#跨平台多进程模块multiprocessing
from multiprocessing import Process
import os 

def run_proc(name):
	print "Run child process %s (%s)..." %(name,os.getpid())

if __name__ == "__main__":
	print 'Parent process %s' % os.getpid()
	p = Process(target=run_proc,args=('test',))#传入执行函数和函数的参数
	print 'Child process will start.'
	p.start()#start()方法启动
	p.join()#join()方法等待子进程结束后再继续往下运行，通常用于进程间的同步
	print 'Child process end'

#进程池Pool,用于启动大量的子进程
from multiprocessing import Pool
import os,time,random

# p = Pool(4)#设置默认最多进程同时进行数量，Pool默认大小为CPU核数
# for i in range(5):
	# p.apply_async(func,args=(i,))
# p.close()
# p.join()
#对Pool对象调用join()方法会等待所有子进程执行完毕，调用join()前必须close()，调用
#close()后无法再添加新的Process

#控制子进程的的输入输出，利用subprocess模块

#进程间的通信
#multiprocessing提供了Queue,Pipes等多种方式交换数据
#在WINDOWS中，父进程在传入子进程数据时，应考虑序列化传入子进程

