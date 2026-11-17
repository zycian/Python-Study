# 用if ... elif ... else ...判断时，要写很长一串代码，可读性较差
# 如果要针对某个变量匹配若干种情况，可以使用match语句
# 例如，某个学生的成绩只能是A、B、C，用if语句编写如下
score = 'B'
if score == 'A':
    print('score is A.')
elif score == 'B':
    print('score is B.')
elif score == 'C':
    print('score is C.')
else:
    print('invalid score.')

# 如果用match语句改写，则改写如下
score = 'A'

match score:
    case 'A':
        print('score is A.')
    case 'B':
        print('score is B.')
    case 'C':
        print('score is C.')
    case _: # _表示匹配到其他任何情况
        print('score is ???.')

# 使用match语句时，依次用case xxx匹配，并且可以在最后（且仅能在最后）加一个case _表示“任意值”


# 复杂匹配

#  match语句除了可以匹配简单的单个值外，还可以匹配多个值、匹配一定范围，并且把匹配后的值绑定到变量
age = 15

match age:
    case x if x < 10:
        print(f'< 10 years old: {x}')
    case 10:
        print('10 years old')
    case 11 | 12 | 13 | 14 | 15 | 16 | 17 | 18:
        print('11~18 years old')
    case 19:
        print('19 years old')
    case _:
        print('not sure')
    
# 在上面这个示例中
# 第一个case x if x < 10表示当age < 10成立时匹配，且赋值给变量x
# 第二个case 10仅匹配单个值，第三个case 11|12|...|18能匹配多个值，用|分隔
# 可见，match语句的case匹配非常灵活


# 匹配列表

# match语句还可以匹配列表，功能非常强大
# 我们假设用户输入了一个命令，用args = ['gcc', 'hello.c']存储，下面的代码演示了如何用match匹配来解析这个列表
args = ['gcc','hello.c','world.c']
# args = ['clean']
# args = ['gcc']
match args:
    # 出现仅gcc，报错
    case ['gcc']:
        print('gcc: missing scorce file(s).')
    # 出现gcc，且至少指定了一个文件：
    case ['gcc',file1,*files]:
        print('gcc compile: ' + file1 + ', ' + ', '.join(files))
    # 仅出现clean：
    case ['clean']:
        print('clean')
    case _:
        print('invalid command.')
# 第一个case ['gcc']表示列表仅有'gcc'一个字符串，没有指定文件名，报错；
# 第二个case ['gcc', file1, *files]表示列表第一个字符串是'gcc'，第二个字符串绑定到变量file1，后面的任意个字符串绑定到*files（符号*的作用将在函数的参数中讲解），它实际上表示至少指定一个文件；
# 第三个case ['clean']表示列表仅有'clean'一个字符串；
# 最后一个case _表示其他所有情况。
# 可见，match语句的匹配规则非常灵活，可以写出非常简洁的代码


# case ['gcc', file1, *files]: —— 变长匹配
# 这是最“魔法”的地方。

# 'gcc'：包裹第一个东西必须是“gcc”。

# file1：把第二个东西抓出来，起个名字叫 file1。
# 比如 args = ['gcc', 'hello.c', 'world.c']，那么 file1 就等于 'hello.c'。

# *files：把剩下所有的东西（从第三个开始）装进一个叫 files 的小篮子。
# 上面例子中，files = ['world.c']。
# 如果只有两个东西（['gcc', 'hello.c']），files 就是空篮子 []。

# 通俗理解：
# “gcc”打头，第二个文件我单拎出来叫 file1（可能用于特殊处理），剩下的不管有多少个，全部放一堆叫 files。
# * 就像吸尘器，把剩下的全部吸进来。