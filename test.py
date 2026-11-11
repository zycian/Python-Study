# a = [1, 2]
# b = a
# b = b + [3]     # 注意这里是 b = b + ...，不是 b.append
# print(a)
# print(b)

# c = [1, 2]
# d = c
# d.append(3)
# print(c)
# print(d)

x = [1, 2]
y = x
y[0] = 99
print(x)
