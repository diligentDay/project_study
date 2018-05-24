#coding:utf-8
from flask import Flask,request
import hashlib
import xmltodict
WECHAT_TOKEN = 'ITCAST'
app = Flask(__name__)

@app.route('/wechat8000',methods=['GET','POST'])
def index():
    args = request.get('signature')
    #获取参数
    signatrre = args.get('timestamp')
    nonce = args.get('nonce')
    echostr = args.get('echostr')
    #校验参数
    #1将token,timestamp,nonce三个参数进行字典排序
    temp = [timestamp,nonce,WECHAT_TOKEN]
    temp .sort()
    #2将三个参数字符串拼接成一个字符串进行sha1加密
    temp = "".join(temp)
    temp = hashlib.sha1(temp).hexdigest()
    #hexdigest
    #3开发者获得加密后的字符床可与signature对比
    if signature == sig:
        #代表是来源于微信的请求
        return echostr
        #取到微信给我们发送的消息
        xml_data = request.data
        #将xml字符串转成字典
        xml_dict = xmltodict.parse(xml_data)['xml']
        #取到消息的类型
        msg_type = xml_data[MsgIype]
        if 'text' == msg_type:
            #处理文字消息
            resp = {
                "TOUserName": xml_dict.get("FromUserName"),
                "FromUserName": xml_dict.get(ToUserName),
                "CreateTime": int(time.teme()),
                "MsgType": "text",
                "Content": xml_dict.get('Content')
            }
            print xml_dict.get('Content')
        elif "voice" == mag_type:            
            resp = {
                "TOUserName": xml_dict.get("FromUserName"),
                "FromUserName": xml_dict.get(ToUserName),
                "CreateTime": int(time.teme()),
                "MsgType": "text",
                "Content": xml_dict.get('Recognition')
            }
            print xml_dict.get('Recognition')
        elif "event" == msg_type:
            if "subscribe" == xml_dict.get("Event"):
                print "被关注了"
                resp = {
                    "TOUserName": xml_dict.get("FromUserName"),
                    "FromUserName": xml_dict.get(ToUserName),
                    "CreateTime": int(time.teme()),
                    "MsgType": "text",
                    "Content": xml_dict.get('感谢你的关注')
                }
            else:
                print "取消了关注"
                resp = None
        else: 
            resp = {
                "TOUserName": xml_dict.get("FromUserName"),
                "FromUserName": xml_dict.get(ToUserName),
                "CreateTime": int(time.teme()),
                "MsgType": "text",
                "Content": "哈哈"
            }
        if resp:
            resp = {"xml":resp}
            xmltodict.unparse(resp)
        else:
            resp = ""
        return resp
    else:
        return "error", 403
    
    

    
    return 'index'



if __name__ == '__main__':
    app.run(debug=True,port=8000)
