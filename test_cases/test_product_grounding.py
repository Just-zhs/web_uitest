import pytest

from webframe.page_objects.login_page import LoginPage


class TestProductManage:
    def setup(self):
        # import os
        # os.getcwd()
        # os.path.abspath(os.curdir)
        # print(os.path.abspath('.'))
        self.login = LoginPage()

    def teardown(self):
        self.login.quit()

    # @pytest.mark.skip
    @pytest.mark.parametrize('num, product_name, price', (['131400', '测试啊啊', '600'],
                                                          ['131401', '测试haha', '610']))
    def test_product_grounding(self, num, product_name, price):
        # name = self.login.login().goto_product_grounding().goods_grounding(num, product_name, price).get_product_name()
        name = self.login.do("login").do(
            'goto_product_grounding').do(
            'goods_grounding', num=num,
            product_name=product_name,
            price=price).do('get_product_name')
        assert name == product_name

    @pytest.mark.parametrize('category', (['测试啊啊啊']))
    def test_product_category(self, category):
        name = self.login.do('login').do('goto_product_category').do('add_goods_category', category=category).do(
            'get_category_name', category=category)
        assert name == category

    @pytest.mark.parametrize('category', (['测试啊啊啊']))
    def test_delete_product_category(self, category):
        name = self.login.do('login').do('goto_product_category').do('delete_goods_category', category=category)
        assert name == []
