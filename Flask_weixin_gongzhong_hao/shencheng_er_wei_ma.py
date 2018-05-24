#coding:utf-8
import time
import urllib2
import json
WECHAT_APPID = "wx8ec5ff22d5fb2211"
WECHAT_APPSECRET = "934608cbe213191cd9372c77bbcb3eb6"
from flask import Flask
#要生成带有参数的二维码：1.获取access_token,2.获取 tickey,3.通过tick换取二维码
class AccessToken(object):
    #专门用于外界要使用access_token的时候调用的类
   __accessf_token = {
        "access_token": "",
        "update_time":time.time(),
        "expires_in":7200
    }
    @classmethod
    def get_access_token(cls):
        #1.判断access_token是否存在,2,删除access_token是否过期,3获取access_t        oken的逻辑
        #if access_token不存在 or access_token 已过期:
        if not cls.__access_token.get("access_token") or\
            (time.time() - cls.__access_token.get('update_time') >\
            cls.__access_token.get("expires_in"))
            #去获取 access_token
            url = "https://api.weixin.qq.com/cgi-bin/token?\
                grant_type=client_credential&appid=%s&secret=%s"\
                 % (WECHAT_APPID, WECHAT_APPSECRET)
            #发起请求获取到响应
            response = urllib2.urlopen(url)
            #取到响应数据
            resp_data = response.read()
            #将字符串转DICT
            resp_dict = json.loads(resp_data)
            if "errcode" in resp_dict:
                raise Exception(resp_dict.get("errmsg"))
            #获取完成之后要进行保存
            cls.__access_token["access_token"] = resp_dict.get("access_token")
            cls.__access_token["updata_time"] = time.time()
            cls.__access_token["expires_in"] = resp_dict.get("expires_in")
    
        return cls.__access_token.get("access_token")
app = Flask(__name__)
@app.route('/get_qrcode/<int:scene_id>')
def index(scene_id):
    #获取ticket
    url = "https://api.weixin.qq.com/cgi-bin/qrcode/create?access_token=" \
        + AccessToken.get_access_token()
    params = {
        "expire_seconds":604800,
        "action_name":"QR_SCENE",
        "action_info":{"scene": {"scene_id":sceme_id}}
    }
    response = urllib2.urlopen(url,data=json.dumps(parms))
    resp_data = respojnse.read()
    resp_dict = json.loads(resp_data)

    ticket = resp_dict.get("ticket")
    expire_seconds = resp_dict.get("expire_seconds")
    url = resp_dict.get("url")
   print ticket,expire_seconds,url

    #通过ticket换取二维码
    return '<img src="https://mp.weixin.qq.com/cgi-bin/showqrcode?ticket=%s">' % ticket
if __name__ == '__main__':
    app.run(debug=True)
