# coding:utf-8
import requests
import re


# 定义一个接收验证码的方法
class CaptchaCode():

    # 发送短信验证码
    def fasongyanzhengma(self,phoneNo):  #　初始化发送验证码
        self.phoneNo = phoneNo  # 定义全局参数
        url = "http://ip:端口/api/v1/auth/sendCode"
        par = {
            "nationCode":"+86",
            "phoneNo":phoneNo
        }
        r = requests.get(url,params=par)
        res = r.json()['message']
        for i in res:
            return res



    # 接收验证码
    def jieshouyanzhengma(self):
        r1 = requests.get("ip")
        result = r1.content.decode('utf-8')
        # 下面正则提取接受的验证码第一个
        res = re.findall('手机号:<span class="phoneNo">(\d+)</span> 在<span class="createdAt">(.*)</span>申请的验证码:<b><span class="code">(\d+)</span></b>',result)
        tuple = res[0] # 将正则提示队列内第一个元祖信息
        return tuple[-1] # 提取元组内最后一个值，并将它返回

# 将类实例化测试一下
# if __name__ == "__main__":
#     a = CaptchaCode()
#     b = a.fasongyanzhengma("2564457")
#     print(b)
#     c = a.jieshouyanzhengma()
#     print(c)

