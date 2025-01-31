import pytest
from tests_ui.conftest import *
from pages.inventory_page import InventoryPage
from utils import users


@pytest.fixture(scope="function")
def browser():
    driver_web = set_up()
    driver_web.get("https://www.saucedemo.com")
    yield driver_web
    driver_web.quit()


@pytest.fixture(scope="function")
def log_in_to_inventory_page(browser) -> InventoryPage:
    login_page = InventoryPage(browser)
    login_page.enter_user_name(users.get_user())
    login_page.enter_password(users.get_password())
    login_page.click_sign_in_button()
    return login_page


@pytest.mark.parametrize("number_of_airports", [6])
def test_verify_inventory_items(number_of_airports, log_in_to_inventory_page) -> None:
    """
        Scenario 1: Verify that the response contains exactly 30 airports

         :param number_of_airports:
                log_in_to_inventory_page:

    :return:
    """
    login_page = log_in_to_inventory_page
    assert (login_page.check_page(number_of_airports))


@pytest.mark.parametrize("inventory_items", [1])
@pytest.mark.parametrize("cart_badge_items", [1])
def test_add_item_to_cart(inventory_items,cart_badge_items, log_in_to_inventory_page) -> None:
    """
    Scenario 2: Add Item to Cart

    :param log_in_to_inventory_page:
           inventory_items:
           cart_badge_items:
    :return:
    """

    login_page = log_in_to_inventory_page
    login_page.add_to_cart(cart_badge_items)
    assert (login_page.check_cart(inventory_items))
