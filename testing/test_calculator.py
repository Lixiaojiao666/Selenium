import sys
import pytest
import yaml

sys.path.append('..')
print(sys.path)

from pythoncode.Calculator import Calculator


def get_yaml_datas(name,type='int'):
    # with open 可以自动关闭
    with open("./datas/calculator.yml") as f:
        data = yaml.safe_load(f)
        datas = data[name][type]['datas']
        ids = data[name][type]['ids']
        return (datas,ids)
'''
def get_yaml_datas1():
    # with open 可以自动关闭
    with open("./datas/calculator.yml") as f:
        datas1 = yaml.safe_load(f)
        return (datas1['div']['datas'],datas1['div']['ids'])
'''
class TestCalculator():
    # datas:list = get_yaml_datas()
    add_int_datas = get_yaml_datas('add')
    add_float_datas = get_yaml_datas('add', type='float')
    add_str_datas = get_yaml_datas('add', type='str')
    div_int_datas = get_yaml_datas('div')
    div_float_datas = get_yaml_datas('div',type='float')
    div_zero_datas = get_yaml_datas('div',type='zero')

    def setup_class(self):
        self.calc = Calculator()
        print("准备工作")

    def teardown_class(self):
        print("收尾工作")

    @pytest.mark.parametrize("a,b,result",add_int_datas[0],ids=add_int_datas[1])
    def test_add_int(self,a,b,result):
        assert result == round(self.calc.add(a,b),3)

    @pytest.mark.parametrize("a,b,result",add_float_datas[0],ids=add_float_datas[1])
    def test_add_float(self,a,b,result):
        assert result == round(self.calc.add(a,b),3)

    @pytest.mark.parametrize("a,b,result", add_str_datas[0], ids=add_str_datas[1])
    def test_add_str(self, a, b, result):
        with pytest.raises(TypeError):
            assert result == round(self.calc.add(a, b), 3)


    @pytest.mark.parametrize("a,b,result1",div_int_datas[0],ids=div_int_datas[1])
    def test_div_int(self,a,b,result1):
        print(f"a={a},b={b},result={result1}")
        assert result1 == self.calc.div(a,b)

    @pytest.mark.parametrize("a,b,result1",div_float_datas[0],ids=div_float_datas[1])
    def test_div_float(self,a,b,result1):
        print(f"a={a},b={b},result={result1}")
        assert result1 == self.calc.div(a,b)

    @pytest.mark.parametrize("a,b,result1", div_zero_datas[0], ids=div_zero_datas[1])
    def test_div_zero(self, a, b, result1):
        print(f"a={a},b={b},result={result1}")
        with pytest.raises(ZeroDivisionError):
            assert result1 == self.calc.div(a, b)
