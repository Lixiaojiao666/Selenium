from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions

class TestWait:
    def setup(self):
        self.driver = webdriver.Firefox()
        self.driver.implicitly_wait(3)
        self.driver.get("https://home.testing-studio.com/")
    def teardown(self):
        self.driver.quit()

    def test_wait(self):
        self.driver.find_element(By.XPATH,'//*[@title="所有分类"]').click()
        #sleep(3)

        #定义一个函数，传入到显式等待的until()里
        #函数内定义了一个条件，判断页面上是否出现某个元素，如果出现，就return true，如果到了设定的时间还未发现元素，就返回false
        #def wait(x):#必须要有个参数，因为until()会传给它一个参数
            #find_elements()发现多个元素，len(self.driver.find_elements())发现元素的长度，即发现元素的个数
        #    return len(self.driver.find_elements(By.XPATH,'//*[@class="table-heading"]')) >= 1

        #显式等待，until()要传入一个函数，这里定义了函数wait()
        #until(wait)是传参，until(wait()):是调用函数
        #WebDriverWait(self.driver,10).until(wait)

        # 当然，也可以不自己定义函数，而直接使用内置函数
        # 内置函数：expected_conditions.element_to_be_clickable()等待元素直到元素可以被点击
        WebDriverWait(self.driver, 10).until(expected_conditions.element_to_be_clickable((By.XPATH,'//*[@class="table-heading"]')))
        self.driver.find_element(By.XPATH, '//*[@title="过去一年、一个月、一周或一天中最活跃的话题"]').click()



