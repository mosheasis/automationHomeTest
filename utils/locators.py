
"""
Implements PagesLocators.
"""
from selenium.webdriver.common.by import By


class PagesLocators(object):
    USER = (By.ID, 'user-name')
    PASSWORD = (By.ID, 'password')
    SUBMIT = (By.ID, 'login-button')
    ERROR_MESSAGE = (By.ID, 'message_error')
    INVENTORY = (By.CLASS_NAME, 'inventory_item')
    CART_LINK = (By.CLASS_NAME, 'shopping_cart_link')
    ADD_TO_CART_BUTTON = (By.CLASS_NAME, 'btn ')
    CART_ITEMS = (By.CLASS_NAME, 'cart_item')
    BADGE = (By.CLASS_NAME, 'shopping_cart_badge')
