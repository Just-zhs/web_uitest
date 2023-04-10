
import os.path
import traceback

import allure
from selenium.common import StaleElementReferenceException

from webframe.utils.log_utils import logger

_BLACK_LIST = [()]


def black_wrapper(fun):
    def run(*args, **kwargs):
        from webframe.page_objects.base_page import BasePage
        basepage: BasePage = args[0]
        try:
            logger.info(f"开始查找元素：{args[2]}")
            return fun(*args, **kwargs)
        except StaleElementReferenceException:
            logger.info(f"开始查找元素：{args[2]}")
            return fun(*args, **kwargs)
        except Exception as e:
            curtime = BasePage.get_time()
            tmp_name = curtime + ".png"
            logger.info("截图路径：" + os.path.dirname(__file__))
            tmp_path = os.path.join(os.path.dirname(__file__), '..', 'image', tmp_name)
            basepage.screenshot(tmp_path)
            allure.attach.file(tmp_path, name="失败截图", attachment_type=allure.attachment_type.PNG)
            logger.warning("元素未找到")
            for black in _BLACK_LIST:
                logger.info(f"处理黑名单：{black}")
                eles = basepage.driver.find_elements(*black)
                if len(eles) > 0:
                    logger.info(f"点击黑名单弹框")
                    eles[0].click()
                    return fun(*args, **kwargs)
            logger.error(f"遍历黑名单，仍未找到元素，异常信息====>{e}")
            logger.error(f"traceback.format_exc异常信息====>{traceback.format_exc()}")
            raise e

    return run
