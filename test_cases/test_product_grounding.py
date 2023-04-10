
import pytest

from webframe.utils.page_manager import PageManager


class TestProductManage:
    def setup(self):
        self.page = PageManager()

    def teardown(self):
        self.page.quit()

    # @pytest.mark.skip
    @pytest.mark.parametrize('num, product_name, price', (['131400', '测试啊啊', '600'],
                                                          ['131401', '测试haha', '610']))
    def test_product_grounding(self, num, product_name, price):
        # done:改造yaml文件，return返回一个值，用于传入navigate中
        page1 = self.page.start()
        next_page = self.page.navigate(page1)
        page2 = self.page.do(next_page, 'goto_product_grounding')
        next_page = self.page.navigate(page2)
        page3 = self.page.do(next_page, 'goods_grounding', num=num,
                             product_name=product_name,
                             price=price)
        next_page = self.page.navigate(page3)
        res = self.page.do(next_page, 'get_product_name')
        assert res == product_name

    # @pytest.mark.skip
    @pytest.mark.parametrize('product_name', ('测试haha', '测试啊啊'))
    def test_delete_product(self, product_name):
        step1 = self.page.start()
        step2 = self.page.do(self.page.navigate(), 'goto_product_list')
        delete_product = self.page.do(self.page.navigate(step2), 'delete_product', product_name=product_name)
        assert delete_product == []

    # @pytest.mark.skip
    @pytest.mark.parametrize('category', (['测试啊啊啊']))
    def test_product_category(self, category):
        page1 = self.page.start()
        page2 = self.page.do(self.page.navigate(page1), 'goto_product_category')
        page3 = self.page.do(self.page.navigate(page2), 'add_goods_category', category=category)
        name = self.page.do(self.page.navigate(page3), 'get_category_name', category=category)
        assert name == category

    # @pytest.mark.skip
    @pytest.mark.parametrize('category', (['测试啊啊啊']))
    def test_delete_product_category(self, category):
        step1 = self.page.start()
        step2 = self.page.do(self.page.navigate(), 'goto_product_category')
        name = self.page.do(self.page.navigate(), 'delete_goods_category', category=category)
        assert name == []
