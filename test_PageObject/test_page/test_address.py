from test_PageObject.page_after_login.main1_page import MainPage1


class TestAddress:
    def test_add_member(self):
        main = MainPage1()
        main.goto_address().add_members()