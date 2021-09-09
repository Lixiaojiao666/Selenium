import datetime

import pytest
'''
#假设每个测试用例都需要调用login()函数，在每个测试用例前都写一点调用fixture就很麻烦，这时候可以用使用autouse自动应用
@pytest.fixture(scope='module')
def login():
    print('登录操作（yield之前的语句）')
    token=datetime.datetime.now()
    #yield触发登出操作，同时，yield想当于return,可以返回一些参数，结果等
    print("下面一句就是yield语句了，执行到这里，就要返回token的值了，是一个当前时间哦")
    yield token
    print('登出操作（yield之后的语句，是放到teardown里执行的哦）')
'''
def test_cart(login):
    print(f"我是购物车，当前时间={login}")

def test_search(login):
    print(f"我是搜索，当前时间={login}")

#@pytest.mark.usefixtures("login")#使用装饰器，不能得到返回值，如果想要返回值的话，一定要参数里调用test_order(login)
def test_order(login):
    print(f"我是下单，当前时间={login}")