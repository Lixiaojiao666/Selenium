import json
from time import sleep
from selenium import webdriver


class TestLoginQiYeWeiXin():
    def setup(self):

        #使用remote复用cookie
        #声明一个webdriver参数类
        chrome_arg = webdriver.ChromeOptions()
        chrome_arg.debugger_address = '127.0.0.1:9222'
        #设置参数options=chrome_arg，或者chrome_options=chrome_arg复用浏览器，参数不同与selenium版本有关系
        #self.driver = webdriver.Chrome(chrome_options=chrome_arg)
        #不复用浏览器，打开新的浏览器
        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(3)


    def teardown(self):
        self.driver.quit()

    #使用cookie登录
    def test_login_cookie(self):
        '''
        #存入cookie

        #首先，拿到cookie，必须是登录后的状态才能拿到cookie（未登录的状态下的cookie里面没有包含任何身份信息）
        cookies0 = self.driver.get_cookies()
        #写入到文件中
        with open("cookie.txt","w",encoding="utf-8") as f:
            # 将获取的cookie写入的文件中，json.dumps()可以把python的数据结构转化成字符串
            #f.write(json.dumps(cookies0))
            #将获取的cookie写入的文件中，json.dump(cookies0,f)写入文件
            json.dump(cookies0,f)

        '''
        #读取cookie

        self.driver.get("https://work.weixin.qq.com/wework_admin/frame#contacts")
        '''
        #读取写了cookie的文件,方式一json.loads()
        with open("cookie.txt", "r", encoding="utf-8") as f:
            # 将读取的文件内容赋值给raw_cookies
            raw_cookies = f.read()
            # 序列化将raw_cookies从字符串格式转化为python数据结构（list）
            cookies_read = json.loads(raw_cookies)
        '''
        # 读取写了cookie的文件,方式二json.dump()
        with open("cookie.txt", "r", encoding="utf-8") as f:
            # 序列化将raw_cookies从字符串格式转化为python数据结构（list）
            cookies_read = json.load(f)

        #添加cookie到driver中
        for i in cookies_read:
            self.driver.add_cookie(i)
        self.driver.refresh()
        sleep(6)


