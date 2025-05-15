import pytest
import time
import selenium
import playwright
from selenium import webdriver
from selenium.webdriver.common.by import By

# from selenium import webdriver
# from selenium.webdriver.chrome.service import Service
# from webdriver_manager.chrome import ChromeDriverManager
# #from webdriver_manager.chrome import C


# from selenium.webdriver.chromium.service import ChromiumService


@pytest.mark.ui
def test_check_incorrect_username():
    #Створення об"єкту управління браузером 
    #driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    #driver = webdriver.Chrome(service=Service(r"/home/julia/Desktop/Python_Project/Python_Project" + "chromedriver"))
    # driver = webdriver.ChromiumEdge
    driver = webdriver.Chrome()

    # Відкриваємо сторінку гітхабу
    driver.get("https://github.com/login")

    #Знаходимо поле, в яке будемо вводити неправильне ім"я користувача та поштову адресу 
    login_elem = driver.find_element(By.ID, "login_field")

    #Вводимо неправильне ім"я користувача або поштову адресу 
    login_elem.send_keys("sergiybutenko@mistakenemail.com")
   

    # Знаходимо поле та вводимо неправильний пароль

    password_element = driver.find_element(By.ID, "password")
    password_element.send_keys("Wrong password")


    # Натиснути на кнопку Сайн-Ін
    btn_elem = driver.find_element(By.NAME, "commit")

    # Емулюємо клік лівою кнопкою миші 
    btn_elem.click()
    time.sleep(5)

    # Перевірка, що назва сторінки така, яку ми очікуємо 
    #print(driver.title)
    assert driver.title == "Sign in to GitHub · GitHub"
    # Закриваємо браузер 
    driver.close()


#browser = webdriver.Chrome(options=chrome_options, service=chrome_service(ChromeDriverManager().install()))


