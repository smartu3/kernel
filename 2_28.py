#-*- coding:utf-8 -*-

#Python��MROģʽ
#python2.1�������ࣻpython2.2����ʽ���뾭������ã�python9ֻ����ʽ��

#�������MRO���������ҵ�������ȱ�����

#��ʽ��MRO����ʽ�����ͨ��__mro__���Ի�ȡ���MRO��ͬ����������ȱ��������ظ���ֻȡ���һ��
#ͬʱ������ػ�����ֵ�˳��

#python2.3�� C3 MRO�����㷽�����ǵ���__mro__����

#��ȡ�ļ�IO����

f=open('/xxxxx','r')
#�ļ�������ΪIOError

f.read()#һ���Զ�ȡ�ļ���ȫ�����ݣ������ݶ����ڴ�
f.close()#�ر��ļ�������ͷ���Դ

with open('/xxx','r') as f:
	print f.read()
#�Զ��ͷ�

#read(size)��ȡָ���ֽ��������ݣ�raadline()��ȡÿ��
#f.write()д�ļ���

#StringIO ���ڴ��ж�д
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

#StringIOֻ�����ַ��������ڶ��������ݣ�Ӧ����BytesIO

#�����ļ���Ŀ¼����OSģ��
os.path.abspath('.')#��ǰĿ¼�ľ���·��
os.path.join('/xxx','tesdir')#��ĳ��Ŀ¼�´�����Ŀ¼���ٰ���Ŀ¼������·����ʾ����
os.mkdir('/xxx')#����һ��Ŀ¼
os.rmdir('/xxx')#ɾ��һ��Ŀ¼
os.path.join('/xxx','b')#�ϳ�·��
os.path.split('/xxx')#���·��
os.path.splitext('/xxx')#����ļ���չ��
#osģ�黹�кܶ๦�ܣ�shutilģ���OSģ�������ܲ���
[x for x in os.listdir('.') if os.path.isdir(x)]#�г���ǰĿ¼������Ŀ¼
[x for x in os.listdir('.') if os.path.isfile(x) and os path.splitext(x)[1] =='.py']
#�г����е�.py�ļ�

#���������ڴ��б�Ϊ�ɴ洢����Ĺ��̳�Ϊ���л���pickling
#���л�������ݿ���д����̣�����ͨ�����紫�䵽��Ļ�����
#�ѱ������ݴ����л��Ķ������¶����ڴ����֮Ϊ�����л���unpickling
#pickleģ��ʵ�����л�
import pickle 
d = dict(name='Bob',age=20,score=88)
pickle.dumps(d)
#b'\x80\.....'
#pickle.dumps()����������������л�Ϊһ��bytes
#��pickle.dump���������л�����д��һ��file-like Object
f=oepn('dump.txt','wb')
pickle.dump(d,f)
f.close()
#�����л�,pickle.loads
f = open('dump.txt','rb')
d = pickle.load(f)
f.close()
d # {'age':20,'score':88...}


