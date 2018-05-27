#coding:utf-8
'''
python 常用函数练习
str, list, dict, set, int, float
datatime, re

'''

# 01 str类型的方法capitalize (2018-05-27)
# 参数: 无
# 返回值:'a, B'返回值是'A,b',' a, B'返回值是' a, b'
# 总结:返回首字母大写的字符串,其余字母小写,
# 如果字符串前面加空格则都返回小写
a = 'a, BaaaaaaaBBBBB'
b = a.capitalize()
print b
# output: 'A,b'
a = ' a, BaaaaaaaBBBBB'
b = a.capitalize()
print b
# output :' a,b'

# 02 str类型的方法 center
# 参数:
#    第一个参数: 返回结果字符串的长度, int类型
#    第二个参数: 结果字符首尾要填充的字符, str类型
# 返回值: 字符类型
# 总结:返回一个原字符串居中并使用空格填充长度或者是*
a = 'abcdef'
b = a.center(20,'*')
print b
# output : '*******abcdef*******'
b = a.center(20)
print b
# output : '       abcdef       '

"""
03 str类型的方法 decode
参数:
    第一个参数: 要解码的字符串的编码格式, str类型
    第二个参数: 解码失败时的处理方式,'strict'抛出异常,'ignore'忽略异常
返回值:  unicode类型
总结:返回解码后的unicode类型字符串
"""
str_01 = "this is string example....wow!!!";
str_02 = str_01.encode('base64','strict');

print "Encoded String: " + str_02;
print "Decoded String: " + str_02.decode('base64','strict')

a = '中国'
b = a.decode('utf-8', 'strict')  # 执行成功,
print b
# output: u'\u4e2d\u56fd'
b = a.decode('ascii', 'strict')  # 执行失败, 抛出UnicodeDecodeError类型的异常
b = a.decode('utf-8', 'ignore')  # 执行成功, 虽然没有报错, 但解码失败,结果为空unicode字符串
print b
# output: u''











"""
'count',
i'decode',
'encode',
'endswith',
'expandtabs',
'find',
'format',
'index',
'isalnum',
'isalpha',
'isdigit',
'islower',
'isspace',
'istitle',
'isupper',
'join',
'ljust',
'lower',
'lstrip',
'partition',
'replace',
'rfind',
'rindex',
'rjust',
'rpartition',
'rsplit',
'rstrip',
'split',
'splitlines',
'startswith',
'strip',
'swapcase',
'title',
'translate',
'upper',
'zfill'
"""


