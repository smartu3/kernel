#-*- coding:utf-8 -*-

#Python的MRO模式
#python2.1：经典类；python2.2：新式类与经典类混用；python9只有新式类

#经典类的MRO：从左至右的深度优先遍历；

#新式类MRO：新式类可以通过__mro__属性获取类的MRO；同样是深度优先遍历，但重复类只取最后一个
#同时会更尊重基类出现的顺序

#python2.3后 C3 MRO，最简便方法便是调用__mro__方法

#读取文件IO操作

f=open('/xxxxx','r')
#文件不存在为IOError

f.read()#一次性读取文件的全部内容，将内容读入内存
f.close()#关闭文件句柄，释放资源

with open('/xxx','r') as f:
	print f.read()
#自动释放

#read(size)读取指定字节数的内容，raadline()读取每行
#f.write()写文件，

#StringIO 在内存中读写
from io import StringIO
f=StringIO()
f.write('hello')
f.write(' ')#1
f.write('world!')
print f.getvalue() # hello world!

f = StringIO('Hello!\nHi!\nGoodbye!')
while True:
	s = f.readline()
	if s =="":
		break
	print s.strip()

#StringIO只能是字符串，对于二进制数据，应该用BytesIO

#操作文件和目录，用OS模块
os.path.abspath('.')#当前目录的绝对路径
os.path.join('/xxx','tesdir')#在某个目录下创建新目录，再把新目录的完整路径表示出来
os.mkdir('/xxx')#创建一个目录
os.rmdir('/xxx')#删除一个目录
os.path.join('/xxx','b')#合成路径
os.path.split('/xxx')#拆分路径
os.path.splitext('/xxx')#获得文件扩展名
#os模块还有很多功能，shutil模块对OS模块作功能补充
[x for x in os.listdir('.') if os.path.isdir(x)]#列出当前目录下所有目录
[x for x in os.listdir('.') if os.path.isfile(x) and os path.splitext(x)[1] =='.py']
#列出所有的.py文件

#将变量从内存中变为可存储或传输的过程称为序列化，pickling
#序列化后的内容可以写入磁盘，或者通过网络传输到别的机器上
#把变量内容从序列化的对象重新读到内存里称之为反序列化，unpickling
#pickle模块实现序列化
import pickle 
d = dict(name='Bob',age=20,score=88)
pickle.dumps(d)
#b'\x80\.....'
#pickle.dumps()方法把任意对象序列化为一个bytes
#用pickle.dump方法将序列化对象写入一个file-like Object
f=oepn('dump.txt','wb')
pickle.dump(d,f)
f.close()
#反序列化,pickle.loads
f = open('dump.txt','rb')
d = pickle.load(f)
f.close()
d # {'age':20,'score':88...}


