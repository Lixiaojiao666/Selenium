from pageObject_learn.main import Main
from selenium_frame_window.base import Base


class TestPageObject(Base):
    def test_pageObject(self):
        #实例化一个Main类的对象，该实例就可以点出Main的所有方法
        main = Main()

        # 实例就可以点出Main的send_keys()方法
        main.send_keys()

        # 实例就可以点出Main的click()方法
        main.click()

        # 实例就可以点出Main的title()方法
        main.title()

        # 实例就可以点出Main的click_first_link()方法，该方法return了Hogwarts类
        # 所以就可以继续点出Hogwarts类的方法
        main.click_first_link()

        # 点出Hogwarts类的方法title()
        main.click_first_link().title()

        # 点出Hogwarts类的方法get_text()
        main.click_first_link().get_text()