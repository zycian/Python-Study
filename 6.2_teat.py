# 练习
# 请定义一个函数 quadratic(a, b, c) ，接收3个参数，返回一元二次方程ax^2+bx+c=0的两个解。
# 提示：
# 一元二次方程的求根公式
# 计算平方根可以调用 math.sqrt() 函数
# import math
# math.sqrt(2)
# 1.4142135623730951
import math

def quadratic(a, b, c):
    if a == 0:
        raise ValueError('这不是二次方程')
    else:
        if (b ** 2) == 4 * a * c:
            return -b / 2 * a
        else:
            x1 = (-b + math.sqrt((b ** 2) - 4 * a * c)) / (2 * a)
            x2 = (-b - math.sqrt((b ** 2) - 4 * a * c)) / (2 * a)
            return x1, x2
print(quadratic(2, 3, 1))    # (-0.5, -1.0)
print(quadratic(1, 3, -4))   # (1.0, -4.0)
