import json
import time
import requests
'''
本文件主要实现通过企业微信应用给企业成员发消息
'''

CORP_ID = "wwb473764920b9cb10"
SECRET = "A9WnIfeeO8xgb5vdwCL3pyuKZdHW7Itysl48Dp5HUr0"

class WeChatPub:
    s = requests.session()

    def __init__(self):
        self.token = self.get_token()

    def get_token(self):
        url = f"https://qyapi.weixin.qq.com/cgi-bin/gettoken?corpid={CORP_ID}&corpsecret={SECRET}"
        rep = self.s.get(url)
        if rep.status_code != 200:
            print("request failed.")
            return
        return json.loads(rep.content)['access_token']

    def send_msg(self, content):
        url = "https://qyapi.weixin.qq.com/cgi-bin/message/send?access_token=" + self.token
        header = {
            "Content-Type": "application/json"
        }
        form_data = {
            "touser": "YeYiFeng",#接收人
            "toparty": "2",#接收部门
            "totag": " TagID1 | TagID2 ",#通讯录标签id
            "msgtype": "textcard",
            "agentid": 1000003,#应用ID
            "textcard": {
                "title": "青年大学习提醒",
                "description": content,
                "url": "http://qndxx.youth54.cn/SmartLA/dxx.w?method=enterIndexPage&fxopenid=&fxversion=",
                "btntxt": "更多"
            },
            "safe": 0
        }
        rep = self.s.post(url, data=json.dumps(form_data).encode('utf-8'), headers=header)
        if rep.status_code != 200:
            print("request failed.")
            return
        return json.loads(rep.content)

if __name__ == "__main__":
    wechat = WeChatPub()
    timenow = time.strftime("%Y-%m-%d %H:%M:%S",time.localtime())
    wechat.send_msg(f"<div class=\"gray\">{timenow}</div> <div class=\"normal\">注意！</div><div class=\"highlight\">青年大学习记得看！！</div>")
    print('消息已发送！')