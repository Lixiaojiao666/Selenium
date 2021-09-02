def test_a():
    print("我是类外面的函数 测试用例a")
    pass

def test_b():
    print("我是类外面的函数 测试用例b")
    pass


def setup_function():
    print("setup_function")

def teardown_function():
    print("teardown_function")

def setup_module():
    print("setup_module")

def teardown_module():
    print("teardown_module")



class TestSetupTeardown():

    def setup_class(self):
        print("setup_class")

    def teardown_class(self):
        print("teardown_class")

    def setup_method(self):
        print("setup_method")

    def teardown_method(self):
        print("teardown_method")

    def test_c(self):
        print("我是类里面的方法 测试用例c")
        pass

    def test_d(self):
        print("我是类里面的方法 测试用例d")
        pass