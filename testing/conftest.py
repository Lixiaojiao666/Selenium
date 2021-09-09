# conftest.py，文件名字固定，不能更改
# 用来存放公共的一些fixture（作用域为session或者package）,方便合作的其他人调用
# pytest的实现机制：在执行当前这个模块或包之前，先去加载conftest.py

import datetime
import pytest

#该fixture的作用域是module整个项目，所以项目下的其他文件可以直接调用，不需要导入
#该fixture的作用域是session整个项目，在整个项目的前和后被调用一次，一般会用在conftest里面
@pytest.fixture(scope='session')
def login():
    print('登录操作>>>>>>（yield之前的语句）')
    token=datetime.datetime.now()
    #yield触发登出操作，同时，yield想当于return,可以返回一些参数，结果等
    print("下面一句就是yield语句了，执行到这里，就要返回token的值了，是一个当前时间哦")
    yield token
    print('登出操作>>>>>（yield之后的语句，是放到teardown里执行的哦）')
