# list  可以类比数组，同理也存在二维三维乃至更高

# Python内置的一种数据类型是列表：list。list是一种有序的集合，可以随时添加和删除其中的元素
#如列出全班同学的名字
classmates = ['mike','bob','sdkd']      #用[]是list
print(classmates)
print(len(classmates))  #得到元素个数
# 用索引来访问list中每一个位置的元素，记得索引是从0开始的
print(classmates[0])
#print(classmates[3])    #会越界，报IndexError
print(classmates[-1])   #-1索引指向最后一个，但同理到-4（倒数第四个）就越界了
# list是一个可变的有序表，所以，可以往list中追加元素到末尾
classmates.append('adam')
print(classmates)
# 也可以把元素插入到指定的位置，比如索引号为1的位置
classmates.insert(1,'jack')
print(classmates)
# 删除同样
classmates.pop()        #删末尾
print(classmates)
classmates.pop(1)       #删指定索引处
print(classmates)
classmates[1] = 'sarah' #替换
print(classmates)
# list里面的元素的数据类型也可以不同，如
L = ['apple',123,3.12,True]
print(L)
# list元素也可以是另一个list，如
s = ['asd','java',['ssd','123'],'eee']
print(s)
print(len(s))           #一个list是一个元素
print(len(s[2]))        #而元素list又有几个元素
# 也能写成
p = ['3','4']           #注意代码是一行行执行的，要先赋值p
a = ['1',p,'2']
# 想拿到‘3’，有两种
print(p[0])
print(a[1][0])



# tuple

# 另一种有序列表叫元组：tuple。tuple和list非常类似，但是tuple一旦初始化就不能修改
mates = ('a','s','d')   #用（）就是tuple
# 现在，mates这个tuple不能变了，它也没有append()，insert()这样的方法
# 其他获取元素的方法和list是一样的，可以使用mates[0]，mates[-1]，但不能赋值成另外的元素
# 不可变的tuple有什么意义？
# 因为tuple不可变，所以代码更安全。如果可能，能用tuple代替list就尽量用tuple
# tuple的陷阱：当你定义一个tuple时，在定义的时候，tuple的元素就必须被确定下来
# 如果要定义一个空的tuple，可以写成()
# 但是，要定义一个只有1个元素的tuple，如果你这么定义
t = (1)
# 定义的不是tuple，是1这个数！
# 这是因为括号()既可以表示tuple，又可以表示数学公式中的小括号，这就产生了歧义
# 因此，Python规定，这种情况下，按小括号进行计算，计算结果自然是1
# 所以，只有1个元素的tuple定义时必须加一个逗号,，来消除歧义
t1 = (1,)

# 特别地，对于tuple中的list是可变的，如
m = ('a', 'b', ['A', 'B'])
m[2][0] = 'X'
m[2][1] = 'Y'
print(m)
# 所以，需要注意tuple所说的不变是指指向的不变，而不是说内容不变
# 就是说指向的list不变，但对于list内是否改变不管
m[2].append('Z')    #对于增减啊之类的list可用的也不管
print(m)


# 总而言之，[]是list，是有序的可变序列，类似数组，有append/insert/pop；（）是tuple，是指向不变的不可变序列；那么{}是什么？是另一种类型

# 发现python中很多都是指向，而不是改变，或者说是命名？