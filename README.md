
# Selenium Page Object Model and  Rest API with Python 
Welcome to my solution the ControlUp Automation Test!

I divided the tests into two folders.
 1. tests_api folder for rest api tests.
 2. tests_ui folder for UI tests.

For UI tests I used the (POM) Page Object Model.
my POM contains 3 class:
`BasePage` class include basic functionality and driver initialization
```python
# base_page.py
class BasePage(object):
    def __init__(self, driver, base_url='https://www.saucedemo.com'):
        self.base_url = base_url
        self.driver = driver
        self.timeout = 30
```
`LoginPage` class 
```python
class LoginPage(BasePage):
    def __init__(self, driver):
        self.locator = PagesLocators
        super(LoginPage, self).__init__(driver)
```

`InventoryPage` class 
```python
class InventoryPage(LoginPage):
    def __init__(self, driver):
        self.locator = PagesLocators
        super(InventoryPage, self).__init__(driver)
```