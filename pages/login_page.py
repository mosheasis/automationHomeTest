from utils.locators import *
from pages.base_page import BasePage


class LoginPage(BasePage):
    def __init__(self, driver):
        self.locator = PagesLocators
        super(LoginPage, self).__init__(driver)

    def click_sign_in_button(self):
        self.find_element(*self.locator.SUBMIT).click()
        return LoginPage(self.driver)

    def enter_user_name(self, user_name):
        self.find_element(*self.locator.USER).send_keys(user_name)

    def enter_password(self, password):
        self.find_element(*self.locator.PASSWORD).send_keys(password)

    def click_login_button(self):
        self.find_element(*self.locator.SUBMIT).click()

    def check_page(self, num_of_items):
        try:
            element = self.find_all_elements(*self.locator.INVENTORY)
            if len(element) == num_of_items:
                return True
            else:
                return False
        except:
            return False
