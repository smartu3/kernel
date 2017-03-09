# -*- coding:utf-8 -*-

#JSON

#Python内置的json模块提供了Python对象到JSON格式的转换

import json
d = dict(name='Bob',age = 20,score =88)
json.dumps(d)
#'{"age":20,"score":88,"name":"Bob"}'
#dumps方法返回一个str，内容为标准的JSON格式，同样，dump方法可以将JSON写入一个file-like object
f = open('dumps.txt','w')
json.dump(d,f)
f.close()
#JSON反序列化为Python对象：loads()方法，将JSON对象转换为Python对象；load()方法将JSON数据从file-like 
#object 文件中读出并转换为python对象
json_str = json.dumps(d)
json.loads(json_str)
with open('dumps.txt','r') as f:
	json.load(f)
