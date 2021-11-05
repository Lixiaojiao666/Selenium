from time import sleep

from selenium_js.base import Base


class TestJS(Base):
    def test_js_scroll(self):
        self.driver.get("http://www.baidu.com")
        #定位输入框，输入搜索内容
        self.driver.find_element_by_id('kw').send_keys('自动化测试')
        #定位 百度一下 按钮，并点击
        self.driver.find_element_by_id('su').click()
        #也可以用js来定位百度一下 按钮,传给ele,想要获取JS返回的值，一定要加return
        ele = self.driver.execute_script("return document.getElementById('su')")
        #点击 百度一下 按钮
        ele.click()
        sleep(3)
        self.driver.execute_script("document.documentElement.scrollTop=1000000")
        sleep(3)
        self.driver.find_element_by_xpath('//*[@id="page"]/div/a[10]').click()
        sleep(3)
        '''
        for code in [
            #获取页面title
            'return document.title',
            #获取页面一些时间相关的性能数据
            'return JSON.stringify(performance.timing)'
        ]:
             print(self.driver.execute_script(code))
        '''
        # 不放到代码块里，也可以放到括号里，用分号；隔开
        print(self.driver.execute_script("return document.title;return JSON.stringify(performance.timing)"))

    #测试时间控件
    def test_datatime(self):
        #打开12306网站
        self.driver.get("http://www.12306.cn/index/")
        #执行js代码：定位时间控件
        self.driver.execute_script("return document.getElementById('train_date')")
        #执行js代码：移除时间控件的readonly属性
        self.driver.execute_script("document.getElementById('train_date').removeAttribute('readonly')")
        #执行js代码：给时间控件赋值2021-11-11，返回赋值，并打印出来
        print(self.driver.execute_script("return document.getElementById('train_date').value='2021-11-11'"))
        sleep(3)



