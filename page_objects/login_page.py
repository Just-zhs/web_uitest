import yaml
from selenium.webdriver.common.by import By

from webframe.page_objects.base_page import BasePage


# class LoginPage:
class LoginPage(BasePage):
    _page = '../../webframe/page_objects/login_page.yaml'
    # _page = '../page_objects/login_page.yaml'
    # _INPUT_USERNAME = (By.XPATH, "//*[@name='username']")
    # _INPUT_PASSWORD = (By.XPATH, "//*[@name='password']")
    # _BNT_LOGIN = (By.XPATH, "//*[text()='登录']")

    # def login(self):
    #     return self.load('../page_objects/login_page.yaml', "login")

    # def do(self, method, **kwargs):
    #     return getattr(self, 'load')(self._page, method, **kwargs)
