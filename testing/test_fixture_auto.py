import datetime

import pytest

#假设每个测试用例都需要调用login()函数，在每个测试用例前都写一点调用fixture就很麻烦，这时候可以用使用autouse自动应用
@pytest.fixture(autouse=True)
def login():
    print('登录操作')
    token=datetime.datetime.now()
    #yield触发登出操作，同时，yield想当于return,可以返回一些参数，结果等
    yield token
    print('登出操作')

@pytest.fixture()
def get_username(login):#在fixture方法get_username()里调用另外一个fixture方法login()
    print(f"get_username获取到了login通过yield返回的信息：{login}")
    name = "liiiiiiii"
    return name

def test_cart(get_username):
    print(f"当前用户name={get_username}")

def test_search():
    print(f"b,name={get_username}")

def test_order():
    print(f"c,username = {login},name={get_username}")