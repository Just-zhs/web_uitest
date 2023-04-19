import pytest

from webframe.utils.page_manager import PageManager


class TestProductManage:

    # @pytest.mark.skip
    @pytest.mark.parametrize('num, product_name, price', (['131400', '测试啊啊', '600'],
                                                          ['131401', '测试haha', '610']))
    def test_product_grounding(self, driver, num, product_name, price):
        # done:改造yaml文件，return返回一个值，用于传入navigate中
        # driver是conftest中的fixture函数，返回PageManager()对象
        page1 = driver.start()
        page2 = driver.do(driver.navigate(page1), 'goto_product_grounding')
        page3 = driver.do(driver.navigate(page2), 'goods_grounding', num=num,
                          product_name=product_name,
                          price=price)
        res = driver.do(driver.navigate(page3), 'get_product_name')
        assert res == product_name

    # @pytest.mark.skip
    @pytest.mark.parametrize('product_name', ('测试haha', '测试啊啊'))
    def test_delete_product(self, driver, product_name):
        step1 = driver.start()
        step2 = driver.do(driver.navigate(), 'goto_product_list')
        delete_product = driver.do(driver.navigate(step2), 'delete_product', product_name=product_name)
        assert delete_product == []

    # @pytest.mark.skip
    @pytest.mark.parametrize('category', (['测试啊啊啊']))
    def test_product_category(self, driver, category):
        page1 = driver.start()
        page2 = driver.do(driver.navigate(page1), 'goto_product_category')
        page3 = driver.do(driver.navigate(page2), 'add_goods_category', category=category)
        name = driver.do(driver.navigate(page3), 'get_category_name', category=category)
        assert name == category

    # @pytest.mark.skip
    @pytest.mark.parametrize('category', (['测试啊啊啊']))
    def test_delete_product_category(self, driver, category):
        step1 = driver.start()
        step2 = driver.do(driver.navigate(), 'goto_product_category')
        name = driver.do(driver.navigate(), 'delete_goods_category', category=category)
        assert name == []
