import sys
import pytest
import yaml

sys.path.append('..')
print(sys.path)

from pythoncode.Calculator import Calculator


def get_yaml_datas():
    # with open 可以自动关闭
    with open("./datas/calculator.yml") as f:
        datas = yaml.safe_load(f)
        return (datas['add']['datas'],datas['add']['ids'])

def get_yaml_datas1():
    # with open 可以自动关闭
    with open("./datas/calculator.yml") as f:
        datas1 = yaml.safe_load(f)
        return (datas1['div']['datas'],datas1['div']['ids'])

class TestCalculator():
    datas:list = get_yaml_datas()
    datas1: list = get_yaml_datas1()
    def setup_class(self):
        self.calc = Calculator()
        print("准备工作")

    def teardown_class(self):
        print("收尾工作")

    @pytest.mark.parametrize("a,b,result",datas[0],ids=datas[1])
    def test_add(self,a,b,result):
        assert result == self.calc.add(a,b)

    #参数化后，就不需要再写多条测试用例
    #def test_add1(self):
    #    assert 10 == self.calc.add(5, 5)


    @pytest.mark.parametrize("c,d,result1",datas1[0],ids=datas1[1])
    def test_div(self,c,d,result1):
        print(f"a={c},b={d},result={result1}")
        assert result1 == self.calc.div(c,d)


