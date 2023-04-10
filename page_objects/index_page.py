from selenium.webdriver.common.by import By

from webframe.page_objects.base_page import BasePage


class IndexPage(BasePage):
    _page = '../../webframe/page_objects/index_page.yaml'

    # def goto_product_grounding(self):
    #
    #     return self.load('../page_objects/index_page.yaml', 'goto_product_grounding')
    #     # from webframe.page_objects.goods_grounding_page import GoodsGroundingPage
    #     # return GoodsGroundingPage(self.driver)
    #
    # def goto_product_category(self):
    #
    #     return self.load('../page_objects/index_page.yaml', 'goto_product_category')
    #     # from webframe.page_objects.goods_category_page import GoodsCategoryPage
    #     # return GoodsCategoryPage(self.driver)

    # def do(self, method, **kwargs):
    #     return getattr(self, 'load')(self._page, method, **kwargs)
