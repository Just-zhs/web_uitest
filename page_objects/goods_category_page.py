from time import sleep

from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

from webframe.page_objects.base_page import BasePage


class GoodsCategoryPage(BasePage):
    _page = '../../webframe/page_objects/goods_category_page.yaml'
    # _BTN_ADD = (By.XPATH, "//*[text()='添加']")
    # _INPUT_GOODS_CATEGORY = (By.XPATH, "//*[text()='类目名称']/../div/div/input")
    # _BTN_SUBMIT = (By.XPATH, "//*[text()='确定']/..")
    # # _BTN_SUBMIT = (By.CSS_SELECTOR, ".el-dialog__footer .el-button--primary")
    #
    # _RES_NAME = (By.XPATH, "//tbody/tr[last()]/td[2]/div")
    #
    # def add_goods_category(self, category):
    #     # self.wait(self._BTN_ADD)
    #     # self.do_click(*self._BTN_ADD)
    #     # self.do_send_keys(category, *self._INPUT_GOODS_CATEGORY)
    #     # WebDriverWait(self.driver, 10).until(expected_conditions.element_to_be_clickable(self._BTN_SUBMIT))
    #     # self.do_click(*self._BTN_SUBMIT)
    #     return self.load('../page_objects/goods_category_page.yaml', 'add_goods_category', category=category)
    #     # return self
    #
    # def get_category_name(self, category):
    #     # sleep(5)
    #     # self.wait(self._RES_NAME)
    #     # WebDriverWait(self.driver, 10).until(expected_conditions.text_to_be_present_in_element(self._RES_NAME, category))
    #     # ele = self.do_find(*self._RES_NAME)
    #     # name = ele.text
    #     return self.load('../page_objects/goods_category_page.yaml', 'get_category_name', category=category)
    #
    # def delete_goods_category(self, category):
    #     # WebDriverWait(self.driver, 10).until(
    #     #     expected_conditions.element_to_be_clickable((By.XPATH, f'//*[text()="{category}"]/../../td[last()]//*[text()="删除"]')))
    #     # self.do_click(By.XPATH, f'//*[text()="{category}"]/../../td[last()]//*[text()="删除"]')
    #     # self.wait((By.XPATH, '//*[text()="删除成功"]'))
    #     # res = self.do_finds(By.XPATH, f'//*[text()="{category}"]')
    #     # return res
    #     return self.load('../page_objects/goods_category_page.yaml', 'delete_goods_category', category=category)
    # def do(self, method, **kwargs):
    #     return getattr(self, 'load')(self._page, method, **kwargs)