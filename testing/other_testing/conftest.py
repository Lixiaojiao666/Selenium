import datetime
import pytest

#该fixture的作用域是module整个项目，所以项目下的其他文件可以直接调用，不需要导入
@pytest.fixture(scope='module')
def login():
    print('登录操作（yield之前的语句）')
    #token=datetime.datetime.now()
    #yield触发登出操作，同时，yield想当于return,可以返回一些参数，结果等
    print("下面一句就是yield语句了，执行到这里，就要返回token的值了，是一个当前时间哦")
    name = '阿里巴巴'
    yield name
    print('登出操作（yield之后的语句，是放到teardown里执行的哦）')
