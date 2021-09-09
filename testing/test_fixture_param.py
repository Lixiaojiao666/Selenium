import pytest

'''
 :param params:
        An optional list of parameters which will cause multiple invocations
        of the fixture function and all of the tests using it. The current
        parameter is available in ``request.param``.
'''

# fixture的参数之一：params参数化
# 要获取到params的值，需要用到request.param，request也是一个fixture，不能修改名字，这里相当于是fixture调用了另一个fixture
@pytest.fixture(params=['Alibaba','Tencent'],ids=['a','b'])
def login(request):#request也是一个fixture，不能修改名字，这里相当于是fixture调用了另一个fixture
    print("login")
    return request.param

def test_search(login):
    print("搜索")
    print(login)