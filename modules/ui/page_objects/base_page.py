# from   selenium import webdriver
# from selenium.webdriver.chrome.service import  Service

# class BasePage: 
#     PATH = r"/home/julia/Desktop/Python_Project/Python_Project"
#     DRIVER_NAME = "chromedriver"

#     def __init__(self) ->None:
#         self.driver = webdriver.Chrome(service=Service(BasePage.PATH + BasePage.DRIVER_NAME))

#     def close(self):
#         self.driver.close()

    #----------------------------------webdriver 115 or hight---------------------------------------------------

# from   selenium import webdriver
# from selenium.webdriver.chrome.service import  Service
# from webdriver_manager.chrome import ChromeDriverManager

# class BasePage: 

#     def __init__(self) ->None:
#         self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

#     def close(self):
#         self.driver.close()


#------------------------my version of working chromedriver --------------------------------------

from selenium import webdriver
from selenium.webdriver.common.by import By

class BasePage: 

    def __init__(self) ->None:
        self.driver = webdriver.Chrome()

    def close(self):
        self.driver.close()