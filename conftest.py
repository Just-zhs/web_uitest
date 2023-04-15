# 收集完测试用例之后被调用的hook函数
from typing import List

import pytest


def pytest_collection_modifyitems(
        session: "Session", config: "Config", items: List["Item"]
) -> None:
    for item in items:
        item.name = item.name.encode('utf-8').decode('unicode-escape')
        item._nodeid = item.nodeid.encode('utf-8').decode('unicode-escape')


def pytest_addoption(parser: "Parser", pluginmanager: "PytestPluginManager") -> None:
    mygroup = parser.getgroup("test-env")
    mygroup.addoption("--env",
                      default='test',
                      help='set your run env'
                      )


# @pytest.fixture(scope='session',autouse=True)
# # @pytest.fixture()
# def cmdoption(request):
#     myenv = request.config.getoption("--env", default='test')
#     if myenv == 'test':
#         test_url: str = "https://litemall.hogwarts.ceshiren.com/"
#     elif myenv == 'dev':
#         test_url: str = "https://www.baidu.com/"
#     # print(test_url)
#     return test_url


