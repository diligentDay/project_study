#coding=utf-8
def num_div(num1,num2):
    assert isinstance(num1,int),'num1必须是整数'
    assert isinstance(num2,int),'num2必须是整数'
    assert num2 !=0,'除数不能为0'
    print num1/num2
num_div(100,40)
