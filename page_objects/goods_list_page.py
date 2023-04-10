from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

from webframe.page_objects.base_page import BasePage


class GoodsListPage(BasePage):
    _page = '../page_objects/goods_list_page.yaml'
    # _TEXT_PRODUCT_NAME = (By.XPATH, "//tr[@class='el-table__row'][1]/td[3]/div")

    # def get_product_name(self):
    #     return self.load('../page_objects/goods_list_page.yaml', 'get_product_name')
    #
    # def do(self, method, **kwargs):
    #     return getattr(self, 'load')(self._page, method, **kwargs)
