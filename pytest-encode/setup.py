# setup.py是一个构建工具,
# pip install安装是在线安装，必须要有网络，
# 如果离线安装（下载源码安装），就必须要有setup.py文件
# 离线安装命令：python setup.py install）

from setuptools import setup

setup(
    name='pytest_encode',#名字要与python包的名字一直
    url='https://github.com/Lixiaojiao666/pytest-encode',
    version='1.0',
    author='lxj',
    author_email='727991861@qq.com',
    description='set your encoding and logger',
    long_description='Learn how to package,this is my first time to upload package',
    classifiers=[# 分类索引、pip对所属包的分类
       'Framework::Pytest',
       'Programming Language::Python',
       'Topic::Software Development::Testing',
       'Programming Language::Python::3.9'
    ],
    license='proprietary',
    package=['pytest_encode'],
    keyword=[
        'pytest','py.test','ptest_encode'
    ],

    #需要安装的依赖，配置了此项以后，安装插件的时候，会自动安装依赖包
    install_requires=[
        'pytest'
    ],

    #入口模块 或者 入口函数
    entry_points={
        'pytest11':[
            'pytest-encode = pytest_encode',
        ]
    },
    #windows系统需要加上这样一个参数
    zip_safe=False
)