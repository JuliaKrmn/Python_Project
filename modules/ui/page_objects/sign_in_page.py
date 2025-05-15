from modules.ui.page_objects.base_page import BasePage
from selenium.webdriver.common.by import By 
import time

class SignInPage(BasePage):
    URL = "https://github.com/login"

    def __init__(self) -> None:
        super().__init__()

    def go_to(self):
        self.driver.get(SignInPage.URL)
    
    def try_login(self, username, password):
        #Знаходимо поле, в яке будемо вводити неправильне ім"я користувача та поштову адресу 
        login_elem = self.driver.find_element(By.ID, "login_field")

        #Вводимо неправильне ім"я користувача або поштову адресу 
        login_elem.send_keys(username)
   
        # Знаходимо поле та вводимо неправильний пароль
        password_element = self.driver.find_element(By.ID, "password")
        password_element.send_keys(password)

        # Натиснути на кнопку Сайн-Ін
        btn_elem = self.driver.find_element(By.NAME, "commit")

        # Емулюємо клік лівою кнопкою миші 
        btn_elem.click()
        time.sleep(5)

    def check_title(self, expected_title):
        return self.driver.title == expected_title