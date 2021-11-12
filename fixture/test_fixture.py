import pytest


@pytest.fixture()#加了装饰器以后，就可以在想要调用它的地方直接使用
def login():
    print('登录操作')
    username = 'Tom'
    return username

@pytest.fixture()
def get_username():
    name = "芭比"
    return name

class TestDemo:
    def test_cart(self,login):#测试用例test_a需要登录，可以直接调用加了装饰器的login（）方法
        print(f"a,username = {login}")

    def test_search(self):
        print("b")

    '''
    # fixture使用方法一：直接调用函数名字
    # 测试用例test_order需要登录，可以直接调用加了装饰器的login（）方法
    # 测试用例test_order需要获取用户名，可以直接调用加了装饰器的get_username()方法
    def test_order(self,login,get_username):
        print(f"c,username = {login},name={get_username}")
    '''

    # fixture使用方法二：使用装饰器@pytest.mark.usefixtures('test1')
    @pytest.mark.usefixtures("get_username") #后被调用，写在外层
    @pytest.mark.usefixtures("login") #先被调用，写在内层
    def test_order(self):
        print(f"c,username = {login},name={get_username}")