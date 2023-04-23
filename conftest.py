# 收集完测试用例之后被调用的hook函数
from typing import List

import pytest
import yaml

from webframe.utils.page_manager import PageManager


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

@pytest.fixture(scope='session',autouse=True)
def get_env(request):
    myenv = request.config.getoption("--env", default='test')
    with open('test_data/config.yaml', encoding="utf-8") as f:
        data = yaml.safe_load(f)
    # if myenv == 'test':
    #     test_url: str = "https://litemall.hogwarts.ceshiren.com/"
    # elif myenv == 'dev':
    #     test_url: str = "https://www.baidu.com/"
    test_url = data[myenv]
    return test_url

@pytest.fixture(autouse=True)
def driver(get_env):
    # done:不知道这个地方是否还有优化空间，每次执行获取一次myenv感觉有损耗
    page = PageManager(get_env)
    yield page
    page.quit()
