import time
# from webframe.page_objects import *
import yaml
from selenium import webdriver
from selenium.common import StaleElementReferenceException, NoSuchElementException
from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

from webframe.utils.black_handle import black_wrapper
from webframe.utils.log_utils import logger


class BasePage:
    _BASE_URL = "https://litemall.hogwarts.ceshiren.com/"
    _page = ''

    def __init__(self, driver: WebDriver = None):
        if driver is None:
            self.driver = webdriver.Chrome()
            self.driver.maximize_window()
            self.driver.implicitly_wait(10)
            self.driver.get(self._BASE_URL)
        else:
            self.driver = driver

    @black_wrapper
    def do_find(self, by, locator=None):
        # logger.info(f'开始定位元素：{by} {locator}')
        if locator:
            return self.driver.find_element(by, locator)
        else:
            return self.driver.find_element(*by)

    def do_finds(self, by, locator=None):
        logger.info(f'开始定位元素集合：{by} {locator}')
        if locator:
            return self.driver.find_elements(by, locator)
        else:
            return self.driver.find_elements(*by)

    def do_click(self, by: By, locate: str):
        self.do_find(by, locate).click()

    def do_send_keys(self, text, by: By, locate: str):
        ele = self.do_find(by, locate)
        ele.clear()
        ele.send_keys(text)

    def wait(self, locator: tuple, wait_type='', text=''):
        if wait_type == '':
            return WebDriverWait(self.driver, 10).until(expected_conditions.visibility_of_element_located(locator))
        elif wait_type == 'clickable':
            return WebDriverWait(self.driver, 10).until(
                expected_conditions.element_to_be_clickable(locator))
        elif wait_type == 'text_present':
            return WebDriverWait(self.driver, 10).until(
                expected_conditions.text_to_be_present_in_element(locator, text))

    def wait_until_not(self, locator: tuple, wait_type='', text=''):
        return WebDriverWait(self.driver, 10).until_not(expected_conditions.visibility_of_element_located(locator))

    def do_scroll_to_bottom(self):
        self.driver.execute_script('window.scrollTo(0,document.body.scrollHeight)')

    def quit(self):
        self.driver.quit()

    def screenshot(self, name):
        return self.driver.save_screenshot(name)

    @staticmethod
    def get_time():
        t = time.localtime(time.time())
        cur_time = time.strftime("%Y-%m-%d_%H_%M_%S", t)
        # print(cur_time)
        return cur_time

    def load(self, yaml_path, method, **kwargs):
        with open(yaml_path, encoding="utf-8") as f:
            data = yaml.safe_load(f)
        for step in data[method]:
            locator = step.get('find', '')
            if locator:
                for k, v in kwargs.items():
                    locator = locator.replace('"{' + str(k) + '}"', '"' + str(v) + '"')
            if step["action"] == "click":
                self.do_click(By.XPATH, locator)
            elif step["action"] == "send_keys":
                content = step["text"]
                for k, v in kwargs.items():
                    content = content.replace('${' + str(k) + '}', str(v))
                self.do_send_keys(content, By.XPATH, locator)
            elif step["action"] == "scroll_to_bottom":
                self.do_scroll_to_bottom()
            # 新增
            elif step["action"] == "wait":
                EC = step.get('type', '')
                text = step.get('text', '')
                for k, v in kwargs.items():
                    text = text.replace('${' + str(k) + '}', str(v))
                self.wait((By.XPATH, locator), EC, text)
            elif step["action"] == "wait_not":
                EC = step.get('type', '')
                text = step.get('text', '')
                for k, v in kwargs.items():
                    text = text.replace('${' + str(k) + '}', str(v))
                self.wait_until_not((By.XPATH, locator), EC, text)
            elif step["action"] == "text":
                text = self.do_find(By.XPATH, locator).text
                return text
            elif step["action"] == "finds":
                return self.do_finds(By.XPATH, locator)
            # elif step["action"] == "return":
            #     page = step.get('page', 'self')
            #     return self.navigate(page)
            elif step["action"] == "turn":
                # page = step.get('page', 'self')
                page = step.get('page')
                return page
            elif step["action"] == "sleep":
                time.sleep(2)
