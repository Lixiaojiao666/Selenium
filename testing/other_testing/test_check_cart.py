#需要用到conftest的登录操作

def test_check_cart(login):
    print("查看购物车都有什么")
    print(f"name:{login}")