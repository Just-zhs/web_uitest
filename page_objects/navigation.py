from webframe.page_objects.index_page import IndexPage
from webframe.page_objects.login_page import LoginPage

page_navigation = {
    'login': LoginPage(self.driver),
    'index': IndexPage(self.driver),
}

def turntopage(page):
    """实现界面的跳转"""
    return page_navigation[page]