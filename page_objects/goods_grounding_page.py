from selenium.webdriver.common.by import By

from webframe.page_objects.base_page import BasePage


class GoodsGroundingPage(BasePage):
    _page = '../../webframe/page_objects/goods_grounding_page.yaml'

    # def goods_grounding(self, num, product_name, price):
    #     return self.load('../page_objects/goods_grounding_page.yaml', 'goods_grounding', num=num, product_name=product_name,
    #               price=price)
        # from webframe.page_objects.goods_list_page import GoodsListPage
        # return GoodsListPage(self.driver)

    # def do(self, method, **kwargs):
    #     return getattr(self, 'load')(self._page, method, **kwargs)
