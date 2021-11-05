from time import sleep

from selenium.webdriver import ActionChains

from selenium_frame_window.base import Base


class TestAlert(Base):
    def test_alert(self):
        self.driver.get("https://www.runoob.com/try/try.php?filename=jqueryui-api-droppable")

        #目标元素在frame，要先切换到frame里，才能定位到元素
        self.driver.switch_to.frame('iframeResult')
        drag_ele = self.driver.find_element_by_id('draggable')
        drop_ele = self.driver.find_element_by_id('droppable')

        #拖拽需要用到ActionChains
        action = ActionChains(self.driver)

        # 在drag_ele位置点击鼠标，并且不放开，移动到drop_ele位置，然后释放鼠标
        action.click_and_hold(drag_ele).move_to_element(drop_ele).release()
        action.perform()
        sleep(3)

        #点击弹窗的确定按钮
        self.driver.switch_to_alert().accept()

        #切换回父级页面,点击 点击运行 按钮
        self.driver.switch_to_default_content()
        self.driver.find_element_by_id('submitBTN').click()
        sleep(3)
