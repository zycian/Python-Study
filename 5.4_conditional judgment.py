# 计算机之所以能做很多自动化的任务，因为它可以自己做条件判断。

# 如，输入用户年龄，根据年龄打印不同的内容，在Python程序中，用if语句实现：
age = 20
if age >=18:            # 注意不要少写了冒号:
    print('your age is', age)
    print('adult')
# 也可以给if添加一个else语句，意思是如果if判断是False，不执行if的内容，把else执行了
else:
    print('your age is',age)
    print('adult')
# 当然上面是粗略的判断，可以用elif做更细致的判断
age = 3
if age >= 18:
    print('adult')
elif age >= 6:          # elif是else if缩写
    print('teenager')
else:
    print('kid')

# if语句执行有个特点，它是从上往下判断
# 如果在某个判断上是True，把该判断对应的语句执行后，就忽略掉剩下的elif和else
# if判断条件还可以简写，比如写
if 1:
    print('True')       # 只要x是非零数值、非空字符串、非空list等，就判断为True，否则为False


# 再议input

# 最后看一个有问题的条件判断。很多同学会用input()读取用户的输入，这样可以自己输入，程序运行得更有意思
#birth = input('birth: ')
#if birth < 2000:
#    print('00前')
#else:
#    print('00后')

# 输入1982会报错
# 这是因为input()返回的数据类型是str，str不能直接和整数比较，必须先把str转换成整数
# Python提供了int()函数来完成这件事情
s = input('birth: ')
birth = int(s)
if birth < 2000:
    print('00前')
else:
    print('00后')
# 但是，如果输入abc呢？又会得到一个错误信息
# 因为int()函数发现一个字符串并不是合法的数字时就会报错，程序就退出了。
# 如何检查并捕获程序运行期的错误呢？后面的错误和调试会讲到。


## sum

# 条件判断可以让计算机自己做选择，Python的if...elif...else很灵活。
# 条件判断从上向下匹配，当满足条件时执行对应的块内语句，后续的elif和else都不再执行。