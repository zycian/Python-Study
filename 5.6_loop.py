# 为了让计算机能计算成千上万次的重复运算，我们需要循环语句
# Python的循环有两种
# 一种是for...in循环，依次把list或tuple中的每个元素迭代出来

names = ['Michael','Bob']
for name in names:          #这里name只是名字，写啥都行
    print (name)

# 所以for x in ...循环就是把每个元素代入变量x，然后执行缩进块的语句
# 再比如我们想计算1-10的整数之和，可以用一个sum变量做累加：

sum = 0
for x in [1,2,3,4,5,6,7,8,9,10]:
    sum = sum + x
print(sum)

# 如果要计算1-100的整数之和，从1写到100有点困难
# 幸好Python提供一个range()函数，可以生成一个整数序列，再通过list()函数可以转换为list
# 比如range(5)生成的序列是从0开始小于5的整数        即到n-1

print(list(range(5)))
# 可以方便的生成0到101
sum1 = 0
for x in range(101):
    sum1 = sum1 + x
print(sum1)

# 第二种循环是while循环，只要条件满足，就不断循环，条件不满足时退出循环
# 比如我们要计算100以内所有奇数之和，可以用while循环实现

sum3 = 0
n = 99
while n > 0:
    sum3 = sum3 + n 
    n = n-2         # n不断自减直到不满足条件
print(sum3)



# break         打断

# 在循环中，break语句可以提前退出循环

n = 1
while n <=100:
    if n > 10:          # 只能打印到11
        break
    print(n)
    n = n + 1
print('END')


# comtonue      跳过

# 在循环过程中，也可以通过continue语句，跳过当前的这次循环，直接开始下一次循环

n = 0
while n < 10:
    n = n + 1
    if n % 2 == 0:      # 如果n是偶数，执行continue语句
        continue # continue语句会直接继续下一轮循环，后续的print()语句不会执行
    print(n)




# 小结

# 循环是让计算机做重复任务的有效的方法。
# break语句可以在循环过程中直接退出循环，而continue语句可以提前结束本轮循环，并直接开始下一轮循环
# 这两个语句通常都必须配合if语句使用
# 要特别注意，不要滥用break和continue语句
# break和continue会造成代码执行逻辑分叉过多，容易出错
# 大多数循环并不需要用到break和continue语句，上面的两个例子，都可以通过改写循环条件或者修改循环逻辑，去掉break和continue语句。
# 有些时候，如果代码写得有问题，会让程序陷入“死循环”，也就是永远循环下去
# 这时可以用Ctrl+C退出程序，或者强制结束Python进程。

# 死循环如

# while True:
#     print(1)