#在计算机内存中，统一使用Unicode编码
#当需要保存到硬盘或者需要传输的时候，就转换为UTF-8编码
 
#用记事本编辑的时候，从文件读取的UTF-8字符被转换为Unicode字符到内存里，编辑完成后，保存的时候再把Unicode转换为UTF-8保存到文件

#浏览网页的时候，服务器会把动态生成的Unicode内容转换为UTF-8再传输到浏览器


#字符串（python 3中以Unicode编码，支持多语言）//当然也支持gb2312等其它编码方式

#对于单个字符的编码（注意是单个），Python提供了ord()函数获取字符的整数表示
#chr()函数把编码转换为对应的字符
a = ord('z')
b = ord('帅')
c = chr(1234)
print(a)
print(b)
print(c)
#如果知道字符的整数编码，还可以用十六进制这么写str
print('\u4e2d\u6587')

#字节与字符串是不同类型，人来提供编码信息，防止编码混乱
x = b'\x88'        # 一个字节，值是 0x88
#通过decode，encode来实现转换，要标明编码表
#Python对bytes类型的数据用带b前缀的单引号或双引号表示
print(x)           # b'\x88'
print(len(x))      # 1
print(x[0])        # 136   十进制
#以Unicode表示的str通过encode()方法可以编码为指定的bytes
print('中文'.encode('utf-8'))
print('why'.encode('ascii'))
#反过来，如果我们从网络或磁盘上读取了字节流，那么读到的数据就是bytes
#要把bytes变为str，就需要用decode()方法
print(b'duck'.decode('ascii'))
print(b'\xe4\xb8\xad\xe6\x96\x87'.decode('utf-8'))
#如果bytes中只有一小部分无效的字节，可以传入errors='ignore'忽略错误的字节：
print(b'\xe4\xb8\xad\xff'.decode('utf-8', errors='ignore'))
#要计算str包含多少个字符，可以用len()函数
print(len('abc'))
print(len('法'))
print(len(b'aaa'))
print(len(b'\xe4\xb8\xad\xe6\x96\x87'))
print(len('中文'.encode('utf-8')))

#由于Python源代码也是一个文本文件
#所以当你的源代码中包含中文的时候，在保存源代码时要指定保存为UTF-8编码
#当Python解释器读取源代码时，为了让它按UTF-8编码读取
#我们通常在文件开头写上这两行：
#!/usr/bin/env python3      
# //告诉Linux/OS X系统，这是一个Python可执行程序，Windows系统会忽略这个注释
# -*- coding: utf-8 -*-
# //告诉Python解释器按照UTF-8编码读取源代码，否则在源代码中写的中文输出可能会有乱码
#申明了UTF-8编码并不意味着你的.py文件就是UTF-8编码的
#必须并且要确保文本编辑器正在使用UTF-8编码



#格式化

#如何输出格式化的字符串
#在Python中，采用的格式化方式和C语言是一致的，用%实现，即占位符     //原来这叫格式化
# %d	整数
# %f	浮点数
# %s	字符串
# %x	十六进制整数
#格式化整数和浮点数还可以指定是否补0和整数与小数的位数，如
print('%2d-%02d' % (3, 1))  #与c同理，%2d表示至少占两个格
#拓展下，我都不知道  AI大人！！！
# %2d	宽度 2，右对齐（默认）	5 → " 5"
# %-2d	宽度 2，左对齐	5 → "5 "
# %02d	宽度 2，左边补 0	5 → "05"
# %5.2f	宽度 5，保留 2 位小数	3.14159 → " 3.14"
# %s	字符串	'ab' → "ab"
print('%.2f' % 3.1415926)
#如果你不太确定应该用什么，%s永远起作用，它会把任何数据类型转换为字符串
print('Age: %s. Gender: %s' % (25, True))
#若字符串里面的%是一个普通字符就需要转义，用%%来表示一个%
print('growth rate: %d %%' % 7)     #growth rate: 7 %

#format()

#另一种格式化字符串的方法是使用字符串的format()方法
#它会用传入的参数-依次替换-字符串内的占位符{0}、{1}……，不过这种方式写起来比%要麻烦得多
print('Hello, {0}, 成绩提升了 {1:.1f}%'.format('小明', 17.125))

#f-string

#最后一种格式化字符串的方法是使用以f开头的字符串，称之为f-string
#它和普通字符串不同之处在于，字符串如果包含{xxx}，就会以对应的变量替换 如
r = 2.5
s = 3.14*r** 2
print(f'The area of a circle with radius {r} is {s:.2f}')
#上述代码中，{r}被变量r的值替换，{s:.2f}被变量s的值替换
#并且:后面的.2f指定了格式化参数（即保留两位小数），因此，{s:.2f}的替换结果是19.62
