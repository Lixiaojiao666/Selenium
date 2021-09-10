from typing import List


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
        #if 'add' in item._nodeid:
        #    item.add_marker(pytest.mark.add)


    # items就是测试用例的集合,是一个列表，列表就可以反转，追加等
    # 测试用例倒序执行
    #items.reverse()