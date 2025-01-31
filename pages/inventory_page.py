from utils.locators import *
from pages.login_page import LoginPage


class InventoryPage(LoginPage):
    def __init__(self, driver):
        self.locator = PagesLocators
        super(InventoryPage, self).__init__(driver)

    def add_to_cart(self, id_item):
        element = self. find_all_elements(*self.locator.ADD_TO_CART_BUTTON)
        element[id_item].click()

    def check_cart(self,items):
        try:
            element = self.find_all_elements(*self.locator.CART_LINK)
            if len(element) == items:
                return True
            else:
                return False
        except:
            return False