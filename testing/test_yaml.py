import yaml


def test_yaml():
    # with open 可以自动关闭
    with open("./datas/calculator.yml") as f:
        datas = yaml.safe_load(f)
        print(datas)