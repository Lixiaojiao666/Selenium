from time import sleep

import pytest

@pytest.mark.dependency() #设置依赖关系
@pytest.mark.xfail(reason='deliberate fail')
def test_a():
    sleep(5)
    assert False

@pytest.mark.dependency() #设置依赖关系
def test_b():
    sleep(5)
    pass

#依赖测试用例test_a，test_a失败的话，test_c就跳过不执行
@pytest.mark.dependency(depends=["test_a"])
def test_c():
    sleep(5)
    pass

#依赖测试用例test_b
@pytest.mark.dependency(depends=["test_b"])
def test_d():
    sleep(5)
    pass

#依赖测试用例test_b和test_c，test_c跳过的话，test_e也就会跳过
@pytest.mark.dependency(depends=["test_b,test_c"])
def test_e():
    sleep(5)
    pass
