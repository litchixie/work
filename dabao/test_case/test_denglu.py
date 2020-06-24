# coding:utf-8
import requests
import unittest

class TestCase(unittest.TestCase):
    # 定义公用的请求方法
    def setUp(self):
        self.url = "XXX"
        self.s = requests.session()

    @classmethod
    def setUpClass(cls):
        print('---所有用例执行前清理一次---')


    def denglu(self,shopIdentity,userIdentity,password,token,channel): # 定义一个全局共用的登录接口方法，不是test开头的，就不是变量或用例，如这里是denglu，就是定义一个登录的方法，denglu为方法名

        body = {
                "shopIdentity": shopIdentity,
                "userIdentity":userIdentity,
                "password":password,
                "token":token,
                "channel":channel
                }
        h = {
            "User-Agent": "Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.162 Safari/537.36"
            }
        r = self.s.post(self.url, json=body,headers=h)  # 传json格式的body参数
        result = r.text
        res = r.json() # 解析json格式
        success = res['success'] # 提前success这个返回值
        return success

    # 定义第二个全局共用的登录接口，用来测试可登录版本权限

    def denglu2(self,shopIdentity,userIdentity,password,token,channel):

        body2 = {
                "shopIdentity": shopIdentity,
                "userIdentity":userIdentity,
                "password":password,
                "token":token,
                "channel":channel
                }
        h2 = {
            "User-Agent": "Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.162 Safari/537.36"
            }
        r2 = self.s.post(self.url, json=body2,headers=h2)  # 传json格式的body参数
        result2 = r2.text
        res2 = r2.json() # 解析json格式
        success2 = res2['success'] # 提前success这个返回值
        return success2

    # # 定义第三个全局共用登录界接口参数化方法，用来测试密码大小写校验
    # def denglu3(self,shopIdentity,userIdentity,password,token,channel):
    #     body3 = {
    #             "shopIdentity": shopIdentity,
    #             "userIdentity":userIdentity,
    #             "password":password,
    #             "token":token,
    #             "channel":channel
    #             }
    #     h3 = {
    #         "User-Agent": "Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.162 Safari/537.36"
    #         }
    #     r3 = self.s.post(self.url, json=body3,headers=h3)  # 传json格式的body参数
    #     result3 = r3.text
    #     res3 = r3.json() # 解析返回json值
    #     success3 = res3['success'] # 提前success这个返回值
    #     return success3     # 返回success3作为判断条件


    def test_01(self):  # 用例名称一定要用test开头
        u'''登录成功测试用例'''
        success = self.denglu( "null","13425469854","111111","f987b369942389d61c4e1c284c0e0fe2669f169b","PC")
        self.assertTrue(success,success == "True")
        print(success)


    def test_02(self):  # 用例名称一定要用test开头
        u'''账号输入不正确，密码正确'''
        success = self.denglu( "null","13425469800","111111","f987b369942389d61c4e1c284c0e0fe2669f169b","PC")
        self.assertFalse(success,success == "False")

    def test_03(self):  # 用例名称一定要用test开头
        u'''账号输入不完整，密码正确'''
        success = self.denglu( "null","134","111111","f987b369942389d61c4e1c284c0e0fe2669f169b","PC")
        self.assertFalse(success,success == "False")

    def test_04(self):  # 用例名称一定要用test开头
        u'''账号输入为空，密码正确'''
        success = self.denglu( "null","","111111","f987b369942389d61c4e1c284c0e0fe2669f169b","PC")
        self.assertFalse(success,success == "False")

    def test_05(self):  # 用例名称一定要用test开头
        u'''账号输入空格，密码正确'''
        success = self.denglu( "null"," ","111111","f987b369942389d61c4e1c284c0e0fe2669f169b","PC")
        self.assertFalse(success,success == "False")
        print(success)

    def test_06(self):  # 用例名称一定要用test开头
        u'''账号正确输入后加插特殊字符，密码正确'''
        success = self.denglu( "null","13425469854*","111111","f987b369942389d61c4e1c284c0e0fe2669f169b","PC")
        self.assertFalse(success,success == "False")

    def test_07(self):  # 用例名称一定要用test开头
        u'''账号输入正确，加空格，密码正确'''
        success = self.denglu( "null","1342 5 469854","111111","f987b369942389d61c4e1c284c0e0fe2669f169b","PC")
        self.assertFalse(success,success == "False")

    def test_08(self):  # 用例名称一定要用test开头
        u'''账号正确，密码输入不完整'''
        success = self.denglu( "null","13425469854","111","f987b369942389d61c4e1c284c0e0fe2669f169b","PC")
        self.assertFalse(success,success == "False")

    def test_09(self):  # 用例名称一定要用test开头
        u'''账号输入正确，密码输入错误-英文'''
        success = self.denglu( "null","13425469854","111aaa","f987b369942389d61c4e1c284c0e0fe2669f169b","PC")
        self.assertFalse(success,success == "False")

    def test_10(self):  # 用例名称一定要用test开头
        u'''账号正确，密码输入错误-中文'''
        success = self.denglu( "null","13425469854","sd111","f987b369942389d61c4e1c284c0e0fe2669f169b","PC")
        self.assertFalse(success,success == "False")

    def test_11(self):  # 用例名称一定要用test开头
        u'''账号正确，密码输入空格'''
        success = self.denglu( "null","13425469854","111 111","f987b369942389d61c4e1c284c0e0fe2669f169b","PC")
        self.assertFalse(success,success == "False")

    def test_12(self):  # 用例名称一定要用test开头
        u'''账号正确，密码输入特殊字符'''
        success = self.denglu( "null","13425469854","///111","f987b369942389d61c4e1c284c0e0fe2669f169b","PC")
        self.assertFalse(success,success == "False")

    def test_13(self):  # 用例名称一定要用test开头
        u'''账号正确，密码输入为空'''
        success = self.denglu( "null","13425469854","","f987b369942389d61c4e1c284c0e0fe2669f169b","PC")
        self.assertFalse(success,success == "False")

    def test_14(self):  # 用例名称一定要用test开头
        u'''账号正确，密码输入空格'''
        success = self.denglu( "null","13425469854","      ","f987b369942389d61c4e1c284c0e0fe2669f169b","PC")
        self.assertFalse(success,success == "False")

    def test_15(self):  # 用例名称一定要用test开头
        u'''账号正确，密码输入校验大小写'''
        success = self.denglu( "null","lnt-7","111QQQ","ab0e90dc936ae4883e08eea0d6b1257317f2f648","PC")
        self.assertFalse(success,success == "False")

    def test_16(self):  # 用例名称一定要用test开头
        u'''账号和密码全部为空'''
        success = self.denglu( "null","","","f987b369942389d61c4e1c284c0e0fe2669f169b","PC")
        self.assertFalse(success,success == "False")

    def test_17(self):  # 用例名称一定要用test开头
        u'''可登录版本权限为APP，在PC登录'''
        success2 = self.denglu2("null","lnt-6","111111","7574a703c5cec0ff0801e72aea4a916ab02aa041","PC")
        self.assertFalse(success2,success2 == "False")

    def test_18(self):  # 用例名称一定要用test开头
        u'''可登录版本权限为PAD，在PC登录'''
        success2 = self.denglu2("null","lnt-6","111111","7574a703c5cec0ff0801e72aea4a916ab02aa041","PC")
        self.assertFalse(success2,success2 == "False")

    def test_19(self):  # 用例名称一定要用test开头
        u'''可登录版本权限为PAD，channel值为空'''
        success2 = self.denglu2("null","lnt-6","111111","7574a703c5cec0ff0801e72aea4a916ab02aa041","")
        self.assertFalse(success2,success2 == "False")

    def test_20(self):  # 用例名称一定要用test开头
        u'''可登录版本权限为PAD，channel值输入非法值'''
        success2 = self.denglu2("null","lnt-6","111111","7574a703c5cec0ff0801e72aea4a916ab02aa041","234")
        self.assertFalse(success2,success2 == "False")

    def test_21(self):  # 用例名称一定要用test开头
        u'''可登录版本权限为PAD，channel值为小写'''
        success2 = self.denglu2("null","lnt-6","111111","7574a703c5cec0ff0801e72aea4a916ab02aa041","app")
        self.assertFalse(success2,success2 == "False")

    def test_22(self):  # 用例名称一定要用test开头
        u'''可登录版本权限为PAD，channel值为小写'''
        success2 = self.denglu2("null","lnt-6","111111","7574a703c5cec0ff0801e72aea4a916ab02aa041","pc")
        self.assertFalse(success2 == "False")

    import time
    time.sleep(2)
    @classmethod
    def tearDownClass(cls):   # 清理执行用例垃圾的命令
        print("--所有用例执行后清理一次--")
