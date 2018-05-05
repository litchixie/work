#coding:utf-8
import requests
import unittest
from common import guojiadiqu_api
from common import token_api
from common import captchaCode_api

class TestCase(unittest.TestCase):
    def setUp(self):  # 定义一个全局变量，这里是定义注册地址变量
        self.url = "http://192.168.14.228:1337/api/v1/auth/register"
        self.s = requests.session()
        self.e = guojiadiqu_api.Guojiadiqu_api() # 国家地区类的实例化
        self.Country = self.e.Country() # 获取国家地区信息
        self.province = self.e.Country() # 获取国家地区一级信息
        self.city = self.e.city() # 获取国家地区二级信息--省市
        self.area = self.e.area() # 获取国家地区二级信息--县区
        # self.address = {self.province,self.city,self.area}
        self.t = token_api.token() # token类的实例化
        self.token = self.t # 获取token信息

    # @classmethod
    # def setUpClass(cls):
    #     print("----所有用例执行前清理一次----")

    # 定义一个注册的方法
    def zhuce(self,shopName,userName,password,currencyCode,captchaCode,nationCode,phoneNo,contactMan,introducer,country,address,token):
        body = {
        "shopName":shopName, # 门店名称
        "userName":userName, # 登录帐号
        "password":password, # 密码
        "currencyCode":currencyCode, # 货币代码
        "captchaCode":captchaCode, # 短信验证码
        "nationCode":"+86", # 区号
        "phoneNo":phoneNo, # 电话号码
        "contactMan":contactMan, # 联系人
        "introducer":introducer, # 介绍人
        "country": {  # 门店所在地
        "id": 86,
        "code": "+86",
        "name": "中国"
        },
        "address": {   # 详细地址
        "province": {
            "id": 150000,
            "code": "",
            "name": "内蒙古自治区"
        },
        "city": {
            "id": 150100,
            "code": "0471",
            "name": "呼和浩特市"
        },
        "area": {
            "id": 150102,
            "code": "0471",
            "name": "新城区"
        }
        },
        "token":token
        }
        r = self.s.post(self.url,json=body)
        print(r.text)
        result = r.text
        res = r.json() # 解析json格式
        success = res['success'] # 提前success这个返回值
        return success

    def test_01(self):
        u'''全部正确输入，注册成功用例'''
        phoneNo = "1352456001" # 每条用例号码需是唯一的
        a = captchaCode_api.CaptchaCode() # 短信验证码类的实例化
        b = a.fasongyanzhengma(phoneNo) # 发送验证码
        print(b)
        c = a.jieshouyanzhengma() # 接收验证码
        print(c)
        success = self.zhuce("litchi自动注册3",phoneNo,"111111","CNY",c,"+86",phoneNo,"litchi自动注册1","litchi自动注册1",self.Country,None,self.t)
        self.assertTrue(success,success == "true")

    def test_02(self):
        u'''门店名称插入特殊字符，注册成功'''
        phoneNo = "1352456202" # 每条用例号码需是唯一的
        a = captchaCode_api.CaptchaCode() # 短信验证码类的实例化
        b = a.fasongyanzhengma(phoneNo) # 发送验证码
        print(b)
        c = a.jieshouyanzhengma() # 接收验证码
        print(c)
        success = self.zhuce("litchi#￥%/*&×自动注册#￥%/*",phoneNo,"111111","CNY",c,"+86",phoneNo,"litchi自动注册1","litchi自动注册1",self.Country,None,self.t)
        self.assertTrue(success,success == "ture")

    def test_03(self):
        u'''门店名称输入65个字符，注册失败'''
        phoneNo = "1352456503" # 每条用例号码需是唯一的
        a = captchaCode_api.CaptchaCode() # 短信验证码类的实例化
        b = a.fasongyanzhengma(phoneNo)  # 发送验证码
        print(b)
        c = a.jieshouyanzhengma()# 接收验证码
        print(c)
        success = self.zhuce("士大夫健康士大夫健康士大夫商带来发就圣诞快乐发就是快乐的就商带来发就是打开了房间斯大林分开了斯蒂芬金是断开连接发商带来发数量的佛教",phoneNo,"111111","CNY",c,"+86",phoneNo,"litchi自动注册1","litchi自动注册1",self.Country,None,self.t)
        self.assertFalse(success,success == "false")

    def test_04(self):
        u'''门店名称输入空格，注册失败'''
        phoneNo = "1352456504" # 每条用例号码需是唯一的
        a = captchaCode_api.CaptchaCode()
        b = a.fasongyanzhengma(phoneNo)
        print(b)
        c = a.jieshouyanzhengma()
        print(c)
        success = self.zhuce(" ",phoneNo,"111111","CNY",c,"+86",phoneNo,"litchi自动注册1","litchi自动注册1",self.Country,None,self.t)
        self.assertFalse(success,success == "false")

    def test_05(self):
        u'''门店名称输入已存在名称，注册失败'''
        phoneNo = "1352456505" # 每条用例号码需是唯一的
        a = captchaCode_api.CaptchaCode()
        b = a.fasongyanzhengma(phoneNo)
        print(b)
        c = a.jieshouyanzhengma()
        print(c)
        success = self.zhuce("测试门店litchi",phoneNo,"111111","CNY",c,"+86",phoneNo,"litchi自动注册1","litchi自动注册1",self.Country,None,self.t)
        self.assertFalse(success,success == "false")

    def test_06(self):
        u'''门店名称输入已存在名称，注册失败'''
        phoneNo = "1352456506" # 每条用例号码需是唯一的
        a = captchaCode_api.CaptchaCode()
        b = a.fasongyanzhengma(phoneNo)
        print(b)
        c = a.jieshouyanzhengma()
        print(c)
        success = self.zhuce("litchi自动注册2",phoneNo,"111111","CNY",c,"+86",phoneNo,"litchi自动注册1","litchi自动注册1",self.Country,None,self.t)
        self.assertFalse(success,success == "false")

    def test_07(self):
        u'''门店名称为空，注册失败'''
        phoneNo = "1352456507" # 每条用例号码需是唯一的
        a = captchaCode_api.CaptchaCode() # 短信验证码类的实例化
        b = a.fasongyanzhengma(phoneNo) # 发生验证码
        print(b)
        c = a.jieshouyanzhengma() # 接收验证码
        print(c)
        success = self.zhuce("",phoneNo,"111111","CNY",c,"+86",phoneNo,"litchi自动注册1","litchi自动注册1",self.Country,None,self.t)
        self.assertFalse(success,success == "false")

    def test_08(self):
        u'''登录帐号为空，注册失败'''
        phoneNo = "1352456508" # 每条用例号码需是唯一的
        a = captchaCode_api.CaptchaCode()  # 短信验证码类的实例化
        b = a.fasongyanzhengma(phoneNo) # 发生验证码
        print(b)
        c = a.jieshouyanzhengma() # 接收验证码
        print(c)
        success = self.zhuce("litchi自动注册4","","111111","CNY",c,"+86",phoneNo,"litchi自动注册1","litchi自动注册1",self.Country,None,self.t)
        self.assertFalse(success,success == "false")

    def test_09(self):
        u'''登录帐号输入字符65个，注册失败'''
        phoneNo = "1352456509" # 每条用例号码需是唯一的
        a = captchaCode_api.CaptchaCode()
        b = a.fasongyanzhengma(phoneNo)
        print(b)
        c = a.jieshouyanzhengma()
        print(c)
        success = self.zhuce("litchi自动注册4","士大夫健康士大夫健康士大夫商带来发就圣诞快乐发就是快乐的就商带来发就是打开了房间斯大林分开了斯蒂芬金是断开连接发商带来发数量的佛教","111111","CNY",c,"+86",phoneNo,"litchi自动注册1","litchi自动注册1",self.Country,None,self.t)
        self.assertFalse(success,success == "false")

    def test_10(self):
        u'''登录帐号输入特殊字符，注册成功'''
        phoneNo = "13524563001" # 每条用例号码需是唯一的
        a = captchaCode_api.CaptchaCode()
        b = a.fasongyanzhengma(phoneNo)
        print(b)
        c = a.jieshouyanzhengma()
        print(c)
        success = self.zhuce("litchi自动注册4","含23sd#$%^&","111111","CNY",c,"+86",phoneNo,"litchi自动注册1","litchi自动注册1",self.Country,None,self.t)
        self.assertTrue(success,success == "ture")

    def test_10(self):
        u'''登录帐号输入空格，注册失败'''
        phoneNo = "13524563510" # 每条用例号码需是唯一的
        a = captchaCode_api.CaptchaCode()
        b = a.fasongyanzhengma(phoneNo)
        print(b)
        c = a.jieshouyanzhengma()
        print(c)
        success = self.zhuce("litchi自动注册失败4"," ","111111","CNY",c,"+86",phoneNo,"litchi自动注册1","litchi自动注册1",self.Country,None,self.t)
        self.assertFalse(success,success == "false")

    def test_11(self):
        u'''密码输入空格，注册成功'''
        phoneNo = "135245634002" # 每条用例号码需是唯一的
        a = captchaCode_api.CaptchaCode()
        b = a.fasongyanzhengma(phoneNo)
        print(b)
        c = a.jieshouyanzhengma()
        print(c)
        success = self.zhuce("litchi自动注册失败002",phoneNo,"      ","CNY",c,"+86",phoneNo,"litchi自动注册1","litchi自动注册1",self.Country,None,self.t)
        self.assertTrue(success,success == "ture")

    def test_12(self):
        u'''密码输入中文，注册失败'''
        phoneNo = "13524563513" # 每条用例号码需是唯一的
        a = captchaCode_api.CaptchaCode()
        b = a.fasongyanzhengma(phoneNo)
        print(b)
        c = a.jieshouyanzhengma()
        print(c)
        success = self.zhuce("litchi自动失败513",phoneNo,"测试出色出色","CNY",c,"+86",phoneNo,"litchi自动注册1","litchi自动注册1",self.Country,None,self.t)
        self.assertFalse(success,success == "false")

    def test_13(self):
        u'''密码小于6位，注册失败2'''
        phoneNo = "13524564513" # 每条用例号码需是唯一的
        a = captchaCode_api.CaptchaCode()
        b = a.fasongyanzhengma(phoneNo)
        print(b)
        c = a.jieshouyanzhengma()
        print(c)
        success = self.zhuce("litchi自动注册4",phoneNo,"sdf45","CNY",c,"+86",phoneNo,"litchi自动注册1","litchi自动注册1",self.Country,None,self.t)
        self.assertFalse(success,success == "false")

    def test_14(self):
        u'''密码输入超出6位，注册成功'''
        phoneNo = "13524565001" # 每条用例号码需是唯一的
        a = captchaCode_api.CaptchaCode()  # 短信验证码类的实例化
        b = a.fasongyanzhengma(phoneNo)  # 发送验证码
        print(b)
        c = a.jieshouyanzhengma() # 接收验证码
        print(c)
        success = self.zhuce("litchi自动注册成功4",phoneNo,"sdf45445dsfs5/-6","CNY",c,"+86",phoneNo,"litchi自动注册1","litchi自动注册1",self.Country,None,self.t)
        self.assertTrue(success,success == "ture")

    def test_15(self):
        u'''货币代码输入为空，注册失败'''
        phoneNo = "13524565015" # 每条用例号码需是唯一的
        a = captchaCode_api.CaptchaCode()  # 短信验证码类的实例化
        b = a.fasongyanzhengma(phoneNo)  # 发送验证码
        print(b)
        c = a.jieshouyanzhengma() # 接收验证码
        print(c)
        success = self.zhuce("litchi自动注册101",phoneNo,"111111","",c,"+86",phoneNo,"litchi自动注册1","litchi自动注册1",self.Country,None,self.t)
        self.assertFalse(success,success == "false")

    def test_16(self):
        u'''货币代码输入空格，注册失败'''
        phoneNo = "13524565016" # 每条用例号码需是唯一的
        a = captchaCode_api.CaptchaCode()  # 短信验证码类的实例化
        b = a.fasongyanzhengma(phoneNo)  # 发送验证码
        print(b)
        c = a.jieshouyanzhengma() # 接收验证码
        print(c)
        success = self.zhuce("litchi自动注册002",phoneNo,"111111"," ",c,"+86",phoneNo,"litchi自动注册1","litchi自动注册1",self.Country,None,self.t)
        self.assertFalse(success,success == "false")

    def test_17(self):
        u'''货币代码输入不存在的，注册失败'''
        phoneNo = "13524565017" # 每条用例号码需是唯一的
        a = captchaCode_api.CaptchaCode()  # 短信验证码类的实例化
        b = a.fasongyanzhengma(phoneNo)  # 发送验证码
        print(b)
        c = a.jieshouyanzhengma() # 接收验证码
        print(c)
        success = self.zhuce("litchi自动注册003",phoneNo,"111111","QQQ",c,"+86",phoneNo,"litchi自动注册1","litchi自动注册1",self.Country,None,self.t)
        self.assertFalse(success,success == "false")

    def test_18(self):
        u'''货币代码输入HKD，注册成功'''
        phoneNo = "13524515018" # 每条用例号码需是唯一的
        a = captchaCode_api.CaptchaCode()  # 短信验证码类的实例化
        b = a.fasongyanzhengma(phoneNo)  # 发送验证码
        print(b)
        c = a.jieshouyanzhengma() # 接收验证码
        print(c)
        success = self.zhuce("litchi自动注册5018",phoneNo,"111111","HKD",c,"+86",phoneNo,"litchi自动注册1","litchi自动注册1",self.Country,None,self.t)
        self.assertTrue(success,success == "ture")


    def test_19(self):
        u'''货币代码输入MOP，注册成功'''
        phoneNo = "13524525018" # 每条用例号码需是唯一的
        a = captchaCode_api.CaptchaCode()  # 短信验证码类的实例化
        b = a.fasongyanzhengma(phoneNo)  # 发送验证码
        print(b)
        c = a.jieshouyanzhengma() # 接收验证码
        print(c)
        success = self.zhuce("litchi自动注册25018",phoneNo,"111111","MOP",c,"+86",phoneNo,"litchi自动注册1","litchi自动注册1",self.Country,None,self.t)
        self.assertTrue(success,success == "ture")

    def test_20(self):
        u'''货币代码输入SGD，注册成功'''
        phoneNo = "13524535018" # 每条用例号码需是唯一的
        a = captchaCode_api.CaptchaCode()  # 短信验证码类的实例化
        b = a.fasongyanzhengma(phoneNo)  # 发送验证码
        print(b)
        c = a.jieshouyanzhengma() # 接收验证码
        print(c)
        success = self.zhuce("litchi自动注册35018",phoneNo,"111111","SGD",c,"+86",phoneNo,"litchi自动注册1","litchi自动注册1",self.Country,None,self.t)
        self.assertTrue(success,success == "ture")

    def test_21(self):
        u'''货币代码输入THB，注册成功'''
        phoneNo = "13524545018" # 每条用例号码需是唯一的
        a = captchaCode_api.CaptchaCode()  # 短信验证码类的实例化
        b = a.fasongyanzhengma(phoneNo)  # 发送验证码
        print(b)
        c = a.jieshouyanzhengma() # 接收验证码
        print(c)
        success = self.zhuce("litchi自动注册45018",phoneNo,"111111","THB",c,"+86",phoneNo,"litchi自动注册1","litchi自动注册1",self.Country,None,self.t)
        self.assertTrue(success,success == "ture")

    def test_22(self):
        u'''货币代码输入MYR，注册成功'''
        phoneNo = "13524555018" # 每条用例号码需是唯一的
        a = captchaCode_api.CaptchaCode()  # 短信验证码类的实例化
        b = a.fasongyanzhengma(phoneNo)  # 发送验证码
        print(b)
        c = a.jieshouyanzhengma() # 接收验证码
        print(c)
        success = self.zhuce("litchi自动注册55018",phoneNo,"111111","MYR",c,"+86",phoneNo,"litchi自动注册1","litchi自动注册1",self.Country,None,self.t)
        self.assertTrue(success,success == "ture")

    def test_23(self):
        u'''货币代码输入TWD，注册成功'''
        phoneNo = "13524565018" # 每条用例号码需是唯一的
        a = captchaCode_api.CaptchaCode()  # 短信验证码类的实例化
        b = a.fasongyanzhengma(phoneNo)  # 发送验证码
        print(b)
        c = a.jieshouyanzhengma() # 接收验证码
        print(c)
        success = self.zhuce("litchi自动注册65018",phoneNo,"111111","TWD",c,"+86",phoneNo,"litchi自动注册1","litchi自动注册1",self.Country,None,self.t)
        self.assertTrue(success,success == "ture")

    def test_24(self):
        u'''货币代码输入USD，注册成功'''
        phoneNo = "13524575018" # 每条用例号码需是唯一的
        a = captchaCode_api.CaptchaCode()  # 短信验证码类的实例化
        b = a.fasongyanzhengma(phoneNo)  # 发送验证码
        print(b)
        c = a.jieshouyanzhengma() # 接收验证码
        print(c)
        success = self.zhuce("litchi自动注册75018",phoneNo,"111111","USD",c,"+86",phoneNo,"litchi自动注册1","litchi自动注册1",self.Country,None,self.t)
        self.assertTrue(success,success == "ture")

    def test_25(self):
        u'''货币代码插入空格，注册失败'''
        phoneNo = "13524585018" # 每条用例号码需是唯一的
        a = captchaCode_api.CaptchaCode()  # 短信验证码类的实例化
        b = a.fasongyanzhengma(phoneNo)  # 发送验证码
        print(b)
        c = a.jieshouyanzhengma() # 接收验证码
        print(c)
        success = self.zhuce("litchi自动注册85018",phoneNo,"111111","US D",c,"+86",phoneNo,"litchi自动注册1","litchi自动注册1",self.Country,None,self.t)
        self.assertFalse(success,success == "false")

    def test_26(self):
        u'''货币代码插入特殊字符，注册失败'''
        phoneNo = "13524595018" # 每条用例号码需是唯一的
        a = captchaCode_api.CaptchaCode()  # 短信验证码类的实例化
        b = a.fasongyanzhengma(phoneNo)  # 发送验证码
        print(b)
        c = a.jieshouyanzhengma() # 接收验证码
        print(c)
        success = self.zhuce("litchi自动注册95018",phoneNo,"111111","US%……￥&D",c,"+86",phoneNo,"litchi自动注册1","litchi自动注册1",self.Country,None,self.t)
        self.assertFalse(success,success == "false")

    def test_27(self):
        u'''短信验证码不输入，注册失败'''
        phoneNo = "13524586018" # 每条用例号码需是唯一的
        a = captchaCode_api.CaptchaCode()  # 短信验证码类的实例化
        b = a.fasongyanzhengma(phoneNo)  # 发送验证码
        print(b)
        c = a.jieshouyanzhengma() # 接收验证码
        print(c)
        success = self.zhuce("litchi自动注册86018",phoneNo,"111111","CNY","","+86",phoneNo,"litchi自动注册1","litchi自动注册1",self.Country,None,self.t)
        self.assertFalse(success,success == "false")


    def test_28(self):
        u'''短信验证码插入空格，注册失败'''
        phoneNo = "13524587018" # 每条用例号码需是唯一的
        a = captchaCode_api.CaptchaCode()  # 短信验证码类的实例化
        b = a.fasongyanzhengma(phoneNo)  # 发送验证码
        print(b)
        c = a.jieshouyanzhengma() # 接收验证码
        print(c)
        success = self.zhuce("litchi自动注册87018",phoneNo,"111111","CNY"," ","+86",phoneNo,"litchi自动注册1","litchi自动注册1",self.Country,None,self.t)
        self.assertFalse(success,success == "false")

    def test_29(self):
        u'''区号插入空格，注册失败'''
        phoneNo = "13524588018" # 每条用例号码需是唯一的
        a = captchaCode_api.CaptchaCode()  # 短信验证码类的实例化
        b = a.fasongyanzhengma(phoneNo)  # 发送验证码
        print(b)
        c = a.jieshouyanzhengma() # 接收验证码
        print(c)
        success = self.zhuce("litchi自动注册88018",phoneNo,"111111","CNY",c,"+8 6",phoneNo,"litchi自动注册1","litchi自动注册1",self.Country,None,self.t)
        self.assertFalse(success,success == "false")


    def test_30(self):
        u'''区号输入不存在的，注册失败'''
        phoneNo = "13524589018" # 每条用例号码需是唯一的
        a = captchaCode_api.CaptchaCode()  # 短信验证码类的实例化
        b = a.fasongyanzhengma(phoneNo)  # 发送验证码
        print(b)
        c = a.jieshouyanzhengma() # 接收验证码
        print(c)
        success = self.zhuce("litchi自动注册89018",phoneNo,"111111","CNY",c,"+888886",phoneNo,"litchi自动注册1","litchi自动注册1",self.Country,None,self.t)
        self.assertFalse(success,success == "false")

    def test_31(self):
        u'''区号输入为空，注册失败'''
        phoneNo = "13524599018" # 每条用例号码需是唯一的
        a = captchaCode_api.CaptchaCode()  # 短信验证码类的实例化
        b = a.fasongyanzhengma(phoneNo)  # 发送验证码
        print(b)
        c = a.jieshouyanzhengma() # 接收验证码
        print(c)
        success = self.zhuce("litchi自动注册99018",phoneNo,"111111","CNY",c,"",phoneNo,"litchi自动注册1","litchi自动注册1",self.Country,None,self.t)
        self.assertFalse(success,success == "false")

    def test_32(self):
        u'''电话号码输入为空，注册失败'''
        phoneNo = "13524599018" # 每条用例号码需是唯一的
        a = captchaCode_api.CaptchaCode()  # 短信验证码类的实例化
        b = a.fasongyanzhengma(phoneNo)  # 发送验证码
        print(b)
        c = a.jieshouyanzhengma() # 接收验证码
        print(c)
        success = self.zhuce("litchi自动注册99018",phoneNo,"111111","CNY",c,"+86","","litchi自动注册1","litchi自动注册1",self.Country,None,self.t)
        self.assertFalse(success,success == "false")

    def test_33(self):
        u'''电话号码输入空格，注册失败'''
        phoneNo = "13524599118" # 每条用例号码需是唯一的
        a = captchaCode_api.CaptchaCode()  # 短信验证码类的实例化
        b = a.fasongyanzhengma(phoneNo)  # 发送验证码
        print(b)
        c = a.jieshouyanzhengma() # 接收验证码
        print(c)
        success = self.zhuce("litchi自动注册99118",phoneNo,"111111","CNY",c,"+86"," ","litchi自动注册1","litchi自动注册1",self.Country,None,self.t)
        self.assertFalse(success,success == "false")

    def test_34(self):
        u'''电话号码输入16位，注册失败'''
        phoneNo = "13524599218" # 每条用例号码需是唯一的
        a = captchaCode_api.CaptchaCode()  # 短信验证码类的实例化
        b = a.fasongyanzhengma(phoneNo)  # 发送验证码
        print(b)
        c = a.jieshouyanzhengma() # 接收验证码
        print(c)
        success = self.zhuce("litchi自动注册99218",phoneNo,"111111","CNY",c,"+86","1234567890123456","litchi自动注册1","litchi自动注册1",self.Country,None,self.t)
        self.assertFalse(success,success == "false")

    def test_35(self):
        u'''联系人不输入，注册失败'''
        phoneNo = "13524599318"   # 每条用例号码需是唯一的
        a = captchaCode_api.CaptchaCode()  # 短信验证码类的实例化
        b = a.fasongyanzhengma(phoneNo)  # 发送验证码
        print(b)
        c = a.jieshouyanzhengma() # 接收验证码
        print(c)
        success = self.zhuce("litchi自动注册99318",phoneNo,"111111","CNY",c,"+86",phoneNo,"","litchi自动注册1",self.Country,None,self.t)
        self.assertFalse(success,success == "false")

    def test_36(self):
        u'''联系人输入空格，注册失败'''
        phoneNo = "13524599418" # 每条用例号码需是唯一的
        a = captchaCode_api.CaptchaCode()  # 短信验证码类的实例化
        b = a.fasongyanzhengma(phoneNo)  # 发送验证码
        print(b)
        c = a.jieshouyanzhengma() # 接收验证码
        print(c)
        success = self.zhuce("litchi自动注册99418",phoneNo,"111111","CNY",c,"+86",phoneNo,"  ","litchi自动注册1",self.Country,None,self.t)
        self.assertFalse(success,success == "false")

    def test_37(self):
        u'''门店所在地输入空格，注册失败'''
        phoneNo = "13524599518" # 每条用例号码需是唯一的
        a = captchaCode_api.CaptchaCode()  # 短信验证码类的实例化
        b = a.fasongyanzhengma(phoneNo)  # 发送验证码
        print(b)
        c = a.jieshouyanzhengma() # 接收验证码
        print(c)
        success = self.zhuce("litchi自动注册99518",phoneNo,"111111","CNY",c,"+86",phoneNo,"litchi测试","litchi自动注册1","  ",None,self.t)
        self.assertFalse(success,success == "false")

    def test_38(self):
        u'''门店所在地输入为空，注册失败'''
        phoneNo = "13524599618" # 每条用例号码需是唯一的
        a = captchaCode_api.CaptchaCode()  # 短信验证码类的实例化
        b = a.fasongyanzhengma(phoneNo)  # 发送验证码
        print(b)
        c = a.jieshouyanzhengma() # 接收验证码
        print(c)
        success = self.zhuce("litchi自动注册99618",phoneNo,"111111","CNY",c,"+86",phoneNo,"litchi测试","litchi自动注册1","",None,self.t)
        self.assertFalse(success,success == "false")

    def test_39(self):
        u'''token输入为空，注册失败'''
        phoneNo = "13524599618" # 每条用例号码需是唯一的
        a = captchaCode_api.CaptchaCode()  # 短信验证码类的实例化
        b = a.fasongyanzhengma(phoneNo)  # 发送验证码
        print(b)
        c = a.jieshouyanzhengma() # 接收验证码
        print(c)
        success = self.zhuce("litchi自动注册99618",phoneNo,"111111","CNY",c,"+86",phoneNo,"litchi测试","litchi自动注册1","",None,"")
        self.assertFalse(success,success == "false")

    def test_40(self):
        u'''token输入空格，注册失败'''
        phoneNo = "13524599718"  # 每条用例号码需是唯一的
        a = captchaCode_api.CaptchaCode()  # 短信验证码类的实例化
        b = a.fasongyanzhengma(phoneNo)  # 发送验证码
        print(b)
        c = a.jieshouyanzhengma() # 接收验证码
        print(c)
        success = self.zhuce("litchi自动注册99718",phoneNo,"111111","CNY",c,"+86",phoneNo,"litchi测试","litchi自动注册1","",None,"  ")
        self.assertFalse(success,success == "false")






# if __name__ == "__main__":
#     unittest.main()












