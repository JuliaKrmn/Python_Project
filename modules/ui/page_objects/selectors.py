from modules.ui.page_objects.base_page import BasePage
from selenium.webdriver.common.by import By 
import time

#Site for testing automation https://magento.softwaretestingboard.com/ selectors, paths, fields etc: 
class Selectors(BasePage):

    current_url = "https://magento.softwaretestingboard.com/"
    search_field = By.CSS_SELECTOR, "#search"
    search_button = By.CSS_SELECTOR, "#nav-search-submit-button"


    #Homepage Locators
    store_logo = By.CSS_SELECTOR, ".logo"
    search_field = By.CSS_SELECTOR, "#search"
    search_button = By.CSS_SELECTOR, "button[title='Search']"
    cart_icon = By.CSS_SELECTOR, ".showcart"
    sign_in_link = By.LINK_TEXT, "Sign In"
    create_account_link = By.LINK_TEXT, "Create an Account"
    whats_new_menu = By.LINK_TEXT, "What's New"
    women_menu = By.LINK_TEXT, "Women"
    promo_banner = By.CSS_SELECTOR, ".blocks-promo"

    #Search results
    search_results_title=By.CSS_SELECTOR, "span.base"
    message_notice = By.CSS_SELECTOR, "div.message.notice"
    search_results_text = By.CSS_SELECTOR, "div.search.results"           

    #Product Page Locators
    product_title = By.CSS_SELECTOR, ".page-title span"
    product_price = By.CSS_SELECTOR, ".price"
    size_options = By.CSS_SELECTOR, ".swatch-attribute.size"
    color_options = By.CSS_SELECTOR, ".swatch-attribute.color"
    add_to_cart_button = By.CSS_SELECTOR, "#product-addtocart-button"
    color_blue = By.ID, "option-label-color-93-item-50"
    color_purple = By.ID, "option-label-color-93-item-57"
    size_XL = By.ID, "option-label-size-143-item-170"  # f"//a[contains(text(), '{product_name}')]/../../..//button[@title='Add to Cart']")
 
    #Messages
    success_message =  By.CLASS_NAME, "message-success"

    #Cart Page Locators
    cart=By.XPATH, "//*[text()='My Cart']" 
    cart_action = By.CSS_SELECTOR, "a.action.showcart"
    empty_cart = By.CSS_SELECTOR, ".subtitle.empty"
    empty_cart_message = "You have no items in your shopping cart." 
    edit_cart = By.LINK_TEXT, "View and Edit Cart"
    view_cart_link = By.CSS_SELECTOR, ".action.showcart"
    cart_dropdown_viewcart = By.CSS_SELECTOR, ".showcart .actions a.viewcart"
    cart_item_name = By.CSS_SELECTOR, ".product-item-name"
    cart_quantity_input = By.CSS_SELECTOR, "input.input-text.qty"
    proceed_to_checkout_button = By.CSS_SELECTOR, ".checkout-methods-items .action.primary.checkout"
    remove_from_cart = By.CSS_SELECTOR, '[title="Remove item"]'
    cart_is_empty = By.CSS_SELECTOR, "div.cart-empty"

    #Login & Account Locators
    login_email = By.ID, "email"
    login_password = By.ID, "pass"
    login_button = By.ID, "send2"
    dashboard_heading = By.CSS_SELECTOR, ".page-title span"