import pytest
from modules.api.clients.github import GitHub
from selenium import webdriver
from selenium.webdriver.common.by import By

class User:
    def __init__(self) -> None:
        self.name = None
        self.second_name = None 

    def create (self):
        self.name = "Julia"
        self.second_name = "Korman"

    def remove (self):
        self.name = ""
        self.second_name = ""

@pytest.fixture    
def  user():
    user = User()
    user.create()

    yield user 

    user.remove()

@pytest.fixture
def github_api():
    api = GitHub()
    yield api

@pytest.fixture
def fresh_driver():
    driver = webdriver.Chrome()
    driver.implicitly_wait(5)
    yield driver
    driver.quit()

@pytest.fixture(scope="session")
def shared_driver():
    driver = webdriver.Chrome()
    driver.implicitly_wait(5)
    yield driver
    driver.quit()

@pytest.fixture
def driver(request):
    if 'independent_ui' in request.keywords:
        # Use fresh_driver for independent tests
        driver_fixture = request.getfixturevalue('fresh_driver')
    elif 'sequential_ui' in request.keywords:
        # Use shared_driver for sequential tests
        driver_fixture = request.getfixturevalue('shared_driver')
    else:
        # Default to fresh_driver
        driver_fixture = request.getfixturevalue('fresh_driver')
    return driver_fixture