# conftest.py，文件名字固定，不能更改
# 用来存放公共的一些fixture（作用域为session或者package）,方便合作的其他人调用
# pytest的实现机制：在执行当前这个模块或包之前，先去加载conftest.py

# 在执行测试用例之前，先加载conftest.py，
# 如果这里改写了hook函数，就按照改写的规则执行测试用例，如果没有改写，就按照pytest默认的规则，执行测试用例

import datetime
from typing import List

import pytest


# 该fixture的作用域是module整个项目，所以项目下的其他文件可以直接调用，不需要导入
# 该fixture的作用域是session整个项目，在整个项目的前和后被调用一次，一般会用在conftest里面
@pytest.fixture(scope='session')
def login():
    print('登录操作>>>>>>（yield之前的语句）')
    token = datetime.datetime.now()
    # yield触发登出操作，同时，yield想当于return,可以返回一些参数，结果等
    print("下面一句就是yield语句了，执行到这里，就要返回token的值了，是一个当前时间哦")
    yield token
    print('登出操作>>>>>（yield之后的语句，是放到teardown里执行的哦）')


def pytest_collection_modifyitems(
        session: "Session", config: "Config", items: List["Item"]
) -> None:
    # items就是测试用例的集合
    print(items)
    for item in items:
        # name 是测试用例的路径，包括名字
        # 对测试用例的路径重新编码，先encode，再 decode
        item.name = item.name.encode('utf-8').decode('unicode-escape')
        # nodeid 是测试用例的名字
        # 对测试用例的名字重新编码，先encode，再 decode
        item._nodeid = item.nodeid.encode('utf-8').decode('unicode-escape')

        #给测试用例加标签add,在命令行执行pytest test_calculator.py -m add时，就只执行有add的测试用例
        if 'add' in item._nodeid:
            item.add_marker(pytest.mark.add)


    # items就是测试用例的集合,是一个列表，列表就可以反转，追加等
    # 测试用例倒序执行
    items.reverse()
