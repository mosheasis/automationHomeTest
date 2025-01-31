from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException


class BasePage(object):
    def __init__(self, driver, base_url='https://www.saucedemo.com'):
        self.base_url = base_url
        self.driver = driver
        self.timeout = 30

    def load(self):
        self.driver.get(self.base_url)

    def find_element(self, *locator):
        return self.driver.find_element(*locator)

    def find_all_elements(self, *locator):
        return self.driver.find_elements(*locator)

    def wait_element(self, *locator):
        try:
            WebDriverWait(self.driver, 10).until(EC.presence_of_element_located(locator))
        except TimeoutException:
            print("\n * ELEMENT NOT FOUND WITHIN GIVEN TIME! --> %s" %(locator[1]))
            self.driver.quit()
