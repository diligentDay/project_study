#coding:utf-8
"""
在py2环境下测试代码片段
"""

# 01 列表乘以数字的测试
# 结论:print a_list*6(打印出来是6个1) b_list*6(打印出来是6个2,3)
# 使用*号得到多个相同的元素
a_list = [1]
b_list = [2,3]
print a_list*6
# output: [1, 1, 1, 1, 1, 1]
print b_list*6
# output: [2, 3, 2, 3, 2, 3, 2, 3, 2, 3, 2, 3]

# 02 正则表达式中match方法去匹配,是否能匹配上?
# 结论:re.match('abc','defg') 输出结果None 'abc'是要找的模式
# 'defg'是被找的字符串, 找不到返回None 如果找到返回一个match对象
# 使用group()方法获取匹配到的字符串
import re
a = re.match('abc','defg')
print a
# output: None
a = re.match('.*f','defg')
print a
# output: <_sre.SRE_Match object at 0x7fa350591f38>
print a.group()
# output: def
