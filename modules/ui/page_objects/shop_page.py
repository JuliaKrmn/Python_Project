from modules.ui.page_objects.selectors import Selectors
from modules.ui.page_objects.base_page import BasePage
from selenium.webdriver.common.by import By 
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from typing import Any


    #------------------My tests-----------------------
    #The idea - take all selectors out of code so we can reuse it constantly 

    

class ShopPage(BasePage):

    def __init__(self, driver):
        super().__init__(driver) # Sets self.driver

    def go_to_specific_page(self):
        self.driver.get(Selectors.current_url)

    def find_inactive_element(self, by, value):
        return self.driver.find_element(by, value)

    def find_element(self, product_name):

    #From Seleniom support site: 
        # wait = WebDriverWait(driver, timeout=2)
        # wait.until(lambda _ : revealed.is_displayed())

    # In my time it was WaitForTheElementToShow: 
    # presence_of_element_located — element exists in the DOM (might be hidden)
    # visibility_of_element_located — element exists and is visible
    # element_to_be_clickable — element is visible and enabled so you can click it

        wait = WebDriverWait(self.driver, 10)  #explicit wait

        find_product = wait.until(EC.presence_of_element_located(Selectors.search_field))
        find_product.send_keys(product_name)

        search_button = wait.until(EC.element_to_be_clickable(Selectors.search_button))
        search_button.send_keys(Keys.RETURN)


    def validate_results(self, product_name):
        wait = WebDriverWait(self.driver, 10) 
        wait.until(EC.presence_of_element_located(Selectors.product_title))

        element = self.driver.find_element(*Selectors.search_results_title)
        expected_text = f"Search results for: '{product_name}'"
        assert expected_text in element.text, f"Expected '{expected_text}' but got '{element.text}'"

 
    def search_for_the_text(self, text):
        wait = WebDriverWait(self.driver, 10)

        message_element = wait.until(EC.presence_of_element_located((By.XPATH, f"//*[contains(text(), '{text}')]")))

        assert text in message_element.text, f"Expected text '{text}', but found '{message_element.text}'"
        print("My text:", text, "Found element:", message_element.text)


    def chose_color(self, color):
        wait = WebDriverWait(self.driver, 10)
        chose_color = wait.until(EC.element_to_be_clickable((color)))
        chose_color.click()
        
    def chose_size(self, size):
        wait = WebDriverWait(self.driver, 10)
        chose_size = wait.until(EC.element_to_be_clickable((size)))
        chose_size.click()
        print("chosen size")

    def hover_and_add_to_cart(self, product_name):
        wait = WebDriverWait(self.driver, 10)
    
        # Find the product tile (or link) by visible name
        product = wait.until(EC.presence_of_element_located((By.XPATH, f"//a[contains(text(), '{product_name}')]")))

        # Hover over the product tile to reveal hidden buttons 
        ActionChains(self.driver).move_to_element(product).perform()

        self.chose_color(Selectors.color_blue)

        # Wait for the now-visible Add to Cart button
        add_to_cart_button = wait.until(EC.element_to_be_clickable(
        (By.XPATH, f"//a[contains(text(), '{product_name}')]/../../..//button[@title='Add to Cart']")
        ))

        add_to_cart_button.click()

 
    def add_product_to_cart(self, product_name):
       
        self.driver.get(Selectors.current_url)
        self.driver.delete_all_cookies()
        wait = WebDriverWait(self.driver, 5)

        # Search for the product
        search_box = wait.until(EC.presence_of_element_located((By.ID, "search")))
        search_box.send_keys(product_name)
        search_box.submit()

    # Hover over the product in search results
        product = wait.until(EC.presence_of_element_located(
            (By.XPATH, f"//a[contains(text(), '{product_name}')]")
            ))

        ActionChains(self.driver).move_to_element(product).pause(1).perform()

    # Wait and click the "Add to Cart" button 
        add_to_cart_btn = wait.until(EC.element_to_be_clickable(
             (By.XPATH, f"//a[contains(text(), '{product_name}')]/../../..//button[@title='Add to Cart']")
         ))

        self.chose_color(Selectors.color_purple)


        self.chose_size(Selectors.size_XL)

        try:
            add_to_cart_btn.click()
        except:
            self.driver.execute_script("arguments[0].click();", add_to_cart_btn)

    # Wait for success message
        wait.until(EC.presence_of_element_located((Selectors.success_message)))

    # Go to cart
        cart_link = wait.until(EC.element_to_be_clickable((Selectors.cart_action)))
        cart_link.click()

    # Wait for mini cart to load, then view and edit cart
        wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, ".product-item-details")))
        view_cart = wait.until(EC.element_to_be_clickable((Selectors.edit_cart)))
        view_cart.click()

    # Validate product is in cart
        cart_item = wait.until(EC.presence_of_element_located(
            (By.XPATH, f"//td[@class='col item']//a[contains(text(), '{product_name}')]")
        ))
        assert product_name in cart_item.text, f"Expected '{product_name}' in cart, but found '{cart_item.text}'"


    def change_quantity(self, quantity):
        self.driver.get("https://magento.softwaretestingboard.com/checkout/cart/")
        time.sleep(2)

    # Find quantity input and change value
        qty_input = self.driver.find_element(*Selectors.cart_quantity_input)
        qty_input.clear()
        qty_input.send_keys(quantity)
        qty_input.send_keys(Keys.RETURN)
        time.sleep(20)

    # Verify quantity was updated
        updated_qty = self.driver.find_element(*Selectors.cart_quantity_input).get_attribute("value")
        assert updated_qty == quantity
        

    def remove_from_cart(self):
         # Open cart (again)
        self.driver.get(Selectors.current_url + "checkout/cart/")
        wait = WebDriverWait(self.driver, 10)
        try:
            remove_button = wait.until(EC.element_to_be_clickable((Selectors.remove_from_cart)))
            remove_button.click()
        except:
            print("Remove button not found or not clickable.")
            return

    def validate_cart_is_empty(self):

        self.driver.get(Selectors.current_url + "checkout/cart/")
        wait = WebDriverWait(self.driver, 10)
        try:
            wait.until(EC.text_to_be_present_in_element((Selectors.cart_is_empty), "You have no items in your shopping cart."))
            print("Cart is empty")
        except:
            print("Cart is not empty or message not found.")
        
        assert "You have no items in your shopping cart." in self.driver.page_source

    def create_new_account(self, firstName, lastName, email, password):
        self.driver.get(Selectors.current_url + "customer/account/create/")
        wait = WebDriverWait(self.driver, 10)

        # first_name = self.driver.find_element(*Selectors.first_name)
        # first_name.send_keys(firstName)

        # last_name = self.driver.find_element(*Selectors.last_name)
        # last_name.send_keys(lastName)

        # email_input = self.driver.find_element(*Selectors.email)
        # email_input.send_keys(email)

        # password_input = self.driver.find_element(*Selectors.password)
        # password_input.send_keys(password)

        # password_confirmation = self.driver.find_element(*Selectors.password_confirmation)
        # password_confirmation.send_keys(password)


        fields = [
            (Selectors.first_name, firstName),
            (Selectors.last_name, lastName),
            (Selectors.email, email),
            (Selectors.password, password),
            (Selectors.password_confirmation, password),
            ]

        for selector, value in fields:
            element = wait.until(EC.presence_of_element_located(selector))
            element.send_keys(value)

        create_account_button = self.driver.find_element(*Selectors.create_acount_button)
        create_account_button.click()

        time.sleep(5)

        assert self.driver.title == "My Account"









