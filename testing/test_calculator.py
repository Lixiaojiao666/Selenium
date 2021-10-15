import sys

import allure
import pytest
import yaml

sys.path.append('..')
print(sys.path)

from pythoncode.Calculator import Calculator


def get_yaml_datas(name,type='int'):
    # with open 可以自动关闭
    with open("./datas/calculator.yml",encoding='utf-8') as f:
        data = yaml.safe_load(f)
        datas = data[name][type]['datas']
        ids = data[name][type]['ids']
        return (datas,ids)

@pytest.fixture(autouse=True)
def get_instance():#环境准备
    print("开始计算>>>>>>")
    calc:Calculator = Calculator()
    yield calc
    print("结束计算>>>>>>")

#获取加法，int数据
@pytest.fixture(params=get_yaml_datas('add','int')[0],ids=get_yaml_datas('add','int')[1])#拿到yaml里的测试数据
def get_datas_with_fixture_add_int(request):#从fixture里获取返回值，只要调用这个函数，就可以得到返回值，即测试数据
    return request.param

#获取加法，float数据
@pytest.fixture(params=get_yaml_datas('add','float')[0],ids=get_yaml_datas('add','float')[1])#拿到yaml里的测试数据
def get_datas_with_fixture_add_float(request):#从fixture里获取返回值，只要调用这个函数，就可以得到返回值，即测试数据
    return request.param

#获取加法，str数据
@pytest.fixture(params=get_yaml_datas('add','str')[0],ids=get_yaml_datas('add','str')[1])#拿到yaml里的测试数据
def get_datas_with_fixture_add_str(request):#从fixture里获取返回值，只要调用这个函数，就可以得到返回值，即测试数据
    return request.param

#获取除法，int数据
@pytest.fixture(params=get_yaml_datas('div','int')[0],ids=get_yaml_datas('div','int')[1])#拿到yaml里的测试数据
def get_datas_with_fixture_div_int(request):#从fixture里获取返回值，只要调用这个函数，就可以得到返回值，即测试数据
    return request.param

#获取除法，float数据
@pytest.fixture(params=get_yaml_datas('div','float')[0],ids=get_yaml_datas('div','float')[1])#拿到yaml里的测试数据
def get_datas_with_fixture_div_float(request):#从fixture里获取返回值，只要调用这个函数，就可以得到返回值，即测试数据
    return request.param

#获取除法，zero数据
@pytest.fixture(params=get_yaml_datas('div','zero')[0],ids=get_yaml_datas('div','zero')[1])#拿到yaml里的测试数据
def get_datas_with_fixture_div_zero(request):#从fixture里获取返回值，只要调用这个函数，就可以得到返回值，即测试数据
    return request.param

#-------------------------------------------------------------------------------------------------------------
'''
#临时函数，查看返回值
def test_param(get_datas_with_fixture):
    print(get_datas_with_fixture[0])
'''
#--------------------------------------------------------------------------------------------------------------

@allure.feature("计算器")  #大标题
class TestCalculator():
    # datas:list = get_yaml_datas()
    # add_int_datas = get_yaml_datas('add')
    add_float_datas = get_yaml_datas('add', type='float')
    add_str_datas = get_yaml_datas('add', type='str')
    div_int_datas = get_yaml_datas('div')
    div_float_datas = get_yaml_datas('div',type='float')
    div_zero_datas = get_yaml_datas('div',type='zero')


    #@allure.title(f"计算器-加法_{get_datas_with_fixture_add_int[0]}")
    @allure.story("相加功能-整数") #小标题
    def test_add_int(self,get_instance,get_datas_with_fixture_add_int):
        f = get_datas_with_fixture_add_int
        assert f[2] == round(get_instance.add(f[0],f[1]),3)

    @allure.story("相加功能-浮点数")
    def test_add_float(self,get_instance,get_datas_with_fixture_add_float):
        f = get_datas_with_fixture_add_float
        assert f[2] == round(get_instance.add(f[0],f[1]),3)

    @allure.story("相加功能-字符")
    def test_add_str(self,get_instance, get_datas_with_fixture_add_str):
        f = get_datas_with_fixture_add_str
        with pytest.raises(TypeError):
            assert f[2] == round(get_instance.add(f[0],f[1]), 3)

    @allure.story("相除功能-整数")
    def test_div_int(self,get_instance,get_datas_with_fixture_div_int):
        f = get_datas_with_fixture_div_int
        print(f"a={f[0]},b={f[1]},result={f[2]}")
        assert f[2] == get_instance.div(f[0],f[1])

    @allure.story("相除功能-浮点数")
    def test_div_float(self,get_instance,get_datas_with_fixture_div_float):
        f = get_datas_with_fixture_div_float
        print(f"a={f[0]},b={f[1]},result={f[2]}")
        assert f[2] == get_instance.div(f[0],f[1])

    @allure.story("相除功能-零")
    def test_div_zero(self,get_instance, get_datas_with_fixture_div_zero):
        f = get_datas_with_fixture_div_zero
        print(f"a={f[0]},b={f[1]},result={f[2]}")
        with pytest.raises(ZeroDivisionError):
            assert f[2] == get_instance.div(f[0],f[1])
