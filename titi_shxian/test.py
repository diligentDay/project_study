#coding:utf-8
ningijkkoi
ni
def user_login(func):
    def func1(request,*args,**kvargs):
        print 'ab'
        a = func(request,*args,**kvargs)
        print 'cd'
        return a
    return func1
@user_login
def center(request):
    # user = HeroInfo.objects.get(pk=request.session['uid'])
    # context={'title':'用户中心','user':user}
    # return render(request,'ttsx_user/user_center_info.html',context)
    print request
    return 'ok'
# center = user_login(center)

if __name__ == "__main__":
    ret = center('asdfasdf')
    print('zhixing wanghc')
    print ret
