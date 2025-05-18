from selenium.webdriver.chrome.webdriver import WebDriver
from modules.ui.page_objects.sign_in_page import SignInPage
from modules.ui.page_objects.selectors import Selectors
from modules.ui.page_objects.shop_page import ShopPage
from typing import Any

import pytest

@pytest.mark.ui
def test_check_incorrect_username_page_object():
    sign_in_page = SignInPage()

    sign_in_page.go_to()

    sign_in_page.try_login("page_objects@hotmail.com", "wrong_password")

    assert sign_in_page.check_title("Sign in to GitHub · GitHub")

    sign_in_page.close()

@pytest.mark.independent_ui
def test_create_account(fresh_driver: WebDriver):
    create_account = ShopPage(fresh_driver)
    create_account.create_new_account("Author", "Latest", "correct1_Password" ) # for testing purposes email is randomly generated 
    create_account.close()
    

@pytest.mark.independent_ui
def test_search_for_existing_product(fresh_driver: WebDriver):

    existing_product = ShopPage(fresh_driver)

    existing_product.go_to_specific_page() 

    existing_product.find_element("Olivia")

    existing_product.validate_results("Olivia")

    existing_product.close()
    
@pytest.mark.independent_ui
def test_add_to_cart_functionality(fresh_driver: WebDriver):
    existing_product = ShopPage(fresh_driver)
    existing_product.add_product_to_cart("Atlas")
    existing_product.close()


@pytest.mark.independent_ui # This was tricky 
def test_search_for_product_empty_query(fresh_driver: WebDriver):

    existing_product = ShopPage(fresh_driver)

    existing_product.go_to_specific_page() 

    button = existing_product.find_inactive_element(*Selectors.search_button)

    assert  not button.is_enabled(), "Button is unexpectedly clickable"
    existing_product.close()

@pytest.mark.independent_ui
def test_search_for_nonexisting_product(fresh_driver: WebDriver):

    existing_product = ShopPage(fresh_driver)

    existing_product.go_to_specific_page() 

    existing_product.find_element("Jerusalem")

    existing_product.search_for_the_text("Your search returned no results.")

    existing_product.close()

@pytest.mark.independent_ui
def test_add_item_via_search(fresh_driver: WebDriver):
    
    cart = ShopPage(fresh_driver)

    cart.go_to_specific_page()

    cart.find_element("Atlas")

    cart.hover_and_add_to_cart("Atlas")

    cart.close()


#---------Tests that run one after another-----------------------------------------------
@pytest.mark.sequential_ui
@pytest.mark.order(1)
def test_add_product_to_cart(shared_driver):
    cart = ShopPage(shared_driver)
    cart.add_product_to_cart("Olivia 1/4 Zip Light Jacket")

@pytest.mark.sequential_ui
@pytest.mark.order(2)
def test_change_quantity(shared_driver): 
    cart = ShopPage(shared_driver)
    cart.change_quantity("10")

@pytest.mark.sequential_ui
@pytest.mark.order(3)
def test_delete_product(shared_driver): 
    cart = ShopPage(shared_driver)
    cart.remove_from_cart()
    cart.validate_cart_is_empty()

