import os
import yaml

from webframe.page_objects.base_page import BasePage
from webframe.utils.log_utils import logger


class PageManager:
    _current_page = ''
    __instance = None

    # _base = BasePage()

    def __init__(self, url=None, path='page_objects'):
        file_list = os.listdir(path)
        yaml_files = [file for file in file_list if file.endswith('.yaml')]
        self.graphic = {}
        self.page_to_yaml = {}
        for yaml_file in yaml_files:
            yaml_path = path + '/' + yaml_file
            with open(yaml_path, encoding="utf-8") as f:
                data = yaml.safe_load(f)
            filename = yaml_file.split('.')[0]
            self.graphic[filename] = data['adjacency']
            self.page_to_yaml[filename] = yaml_path
        # todo: 不知道是不是该把这个初始化放在init函数里，放在外面pytest无法初始化
        self._base = BasePage(url)
        # {'goods_category_page': [None], 'goods_grounding_page': ['goods_list_page'], 'goods_list_page': [None],
        #  'index_page': ['goods_category_page', 'goods_grounding_page'], 'login_page': ['index_page']}
        # {'goods_category_page': '../page_objects/goods_category_page.yaml',
        #  'goods_grounding_page': '../page_objects/goods_grounding_page.yaml',
        #  'goods_list_page': '../page_objects/goods_list_page.yaml', 'index_page': '../page_objects/index_page.yaml',
        #  'login_page': '../page_objects/login_page.yaml'}

    def __new__(cls, *args, **kwargs):
        if cls.__instance is None:
            cls.__instance = super().__new__(cls)
        return cls.__instance

    def start(self, start_page='login_page', method='login', **kwargs):
        file_path = self.page_to_yaml[start_page]
        self._current_page = start_page
        return self._base.load(file_path, method, **kwargs)

    def navigate(self, to_page=None, from_page=None):
        """
        页面跳转函数
        :param to_page: 要跳转的界面，如果为None，说明当前页面只有一个下一个界面，
                        多于一个需要传递下一个界面的名称
        :param from_page: 当前界面，默认为None，取_current_page
        :return: 下一个要执行的界面的yaml文件路径
        """
        if from_page is None:
            # from_page为空时自动取self._current_page
            from_page = self._current_page
            logger.info(f"当前界面：{from_page}")
        if to_page is None:
            # to_page为空时判断当前界面是否存在下一页，有则跳转，无则跳转当前页
            if self.graphic[self._current_page][0] is not None:
                to_page = self.graphic[self._current_page][0]
            else:
                to_page = self._current_page
        else:
            # to_page不为空时判断是否是当前界面的下一页，不是则返回
            if to_page not in self.graphic[from_page]:
                return False
        yaml_file = self.page_to_yaml[to_page]
        self._current_page = to_page
        logger.info(f"要跳转到界面：{to_page}")
        return yaml_file

    def do(self, page_yaml, method, **kwargs):
        return self._base.load(page_yaml, method, **kwargs)

    def quit(self):
        self._base.quit()


if __name__ == '__main__':
    yaml = PageManager()
