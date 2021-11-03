import time

from selenium import webdriver

from selenium_frame_window.base import Base

#TestWindows类 继承 Base类，就可以引用Base类里面的 setup和teardown
class TestWindows(Base):
    '''
    setup和teardown 每次都要写，很麻烦，可以单独放到一个类base里，再继承这个类，就可以了
    def setup(self):
        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(3)
        self.driver.maximize_window()


    def teardown(self):
        self.driver.quit()
    '''

    def test_windows(self):
        self.driver.get('http://www.baidu.com')
        self.driver.find_element_by_link_text('登录').click()
        #打印当前窗口的句柄
        print(self.driver.current_window_handle)
        self.driver.find_element_by_link_text('立即注册').click()
        # 打印当前窗口的句柄
        print(self.driver.current_window_handle)
        # 打印当前所有的窗口的句柄,所有的窗口会以列表的形式展示出来，可以通过索引来获取其中的某个窗口
        print(self.driver.window_handles)

        windows = self.driver.window_handles

        #切换窗口到 注册页面
        self.driver.switch_to_window(windows[-1])
        #在注册页面，输入用户名
        self.driver.find_element_by_id('TANGRAM__PSP_4__userName').send_keys('username')
        # 在注册页面，输入手机号
        self.driver.find_element_by_id('TANGRAM__PSP_4__phone').send_keys('13800000000')
        time.sleep(3)

        #回到之前的页面，
        self.driver.switch_to_window(windows[0])
        # 点击‘用户登录’
        #self.driver.find_element_by_id('TANGRAM_PSP_10_footerULoginBtn').send_keys('13800000000')
        #在登录页面，输入用户名
        self.driver.find_element_by_id('TANGRAM__PSP_11__userName').send_keys('login_username')
        #在登录页面，输入密码
        self.driver.find_element_by_id('TANGRAM__PSP_11__password').send_keys('login_password')
        # 在登录页面，点击登录按钮
        self.driver.find_element_by_id('TANGRAM__PSP_11__submit').click()
        time.sleep(3)
