# 公司: 北京富邦智慧物联科技有限公司
# 1. 请看下面代码， 补全答案
def foo_str(s):
    s = s+",world"
s = "hello"
foo_str(s)
print s
# 答案： "hello，world"
# 定义函数没有写 def
#----------
def foo_list(a):
    a.append(999)
a = [123]
foo_list(a)
print a
# 答案： "[123,999]"
# 定义函数没有写 def
#----------
def foo_dict(m):
    m["c"] = 3
m = {"a":1, "b":2}
foo_dict(m)
print m
# 答案： {"a":1,"b":2,"c":3}
# 定义函数没有写 def
#----------
# 2. 把字典的各元素的value按推导式生成出来
my_dict = {1:3, 2:1}
values = [my_dict[k] for k in my_dict]
# 3. python里如何拷贝一个对象（赋值， 深拷贝， 浅拷贝）
# 有pdf文件
# 4. 按照字典的value的大小排序， 并打印出来
my_dict = {1:3, 2:1}
for k in sorted(my_dict, key=lambda x: my_dict[x], reverse=True):
    print 'value:',my_dict[k]







