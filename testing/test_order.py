import pytest


#@pytest.mark.run(order=2) #使用这种方式定义顺序的话，顺序就可以随便到多少
@pytest.mark.second #使用这种方式定义顺序的话，要注意只定义到了eight
def test_foo():
    assert True

#@pytest.mark.run(order=1) #使用这种方式定义顺序的话，顺序就可以随便到多少
@pytest.mark.first #使用这种方式定义顺序的话，要注意只定义到了eight
def test_bar():
    assert True