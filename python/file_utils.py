#!/usr/bin/env python
# -*- coding: utf-8 -*-

from datetime import datetime
from io import StringIO

#--读文件，方式1. 文件不存在会抛出IOError异常
f = {}
content = {}
try:
    f = open('../_input/file.txt', 'r')
    content = f.read()
    print(content)

finally:
    if f:
        f.close()


#读文件，方式2. with 方法退出时,自动调用f.close()方法 
#读文件，方式3. 二进制文件rb 
#读文件，方式4. 字节编码和遇到错误处理机制：f = open('file.txt', 'r', encoding='gbk', errors='ignore') 
with open('../_input/file.txt', 'r') as fi:
    #只读取一行    
    line = fi.readline()
    print(line) 
    #读取指定字节数
    byte = fi.read(20)
    print(byte) 

#--写文件
with open('../_output/python_file.txt', 'w') as fo:
    fo.write('今天是 ')
    fo.write(datetime.now().strftime('%Y-%m-%d'))
    fo.write(', 慢慢长夜无心睡眠，不如吟诗一首，以解烦忧：\n\n')
    fo.write(content)

#--StringIO就是在内存中创建的file-like Object，常用作临时缓冲
#write StringIO:

fs = StringIO()
fs.write('hello')
fs.write(' ')
fs.write('world')
print(f.getvalue())

#read from StringIO:
fs = StringIO('锄禾日当午，\n汗滴禾下土。\n谁知盘中餐，\n粒粒皆辛苦。')
while True:
    s = fs.readline()
    if s == '':
        break
    print(s.strip())
