Python Project: Automated UI Testing Framework
This project is an automated UI testing framework built using Python and Selenium WebDriver. It focuses on testing the user interface of a web-based shop application, ensuring that critical functionalities like account creation, login, and product search work as expected.

Features
Page Object Model (POM): Structured and maintainable codebase using POM design pattern.
Automated Test Cases: Comprehensive test coverage for user registration, login, and product search functionalities.
Randomized Test Data: Utilizes dynamic data generation to ensure test independence and avoid conflicts.
Pytest Integration: Leverages Pytest for test execution and reporting.
Selenium WebDriver: Automates browser interactions for end-to-end testing.

Project Structure

Python_Project/  
├── modules/  
│   └── ui/  
│       ├── page_objects/  
│       │   ├── shop_page.py  
│       │   └── ...  
│       └── selectors/  
│           └── selectors.py  
├── tests/  
│   └── ui/  
│       └── test_ui_page_objects.py  
├── requirements.txt  
└── README.md  

modules/ui/page_objects/: Contains Page Object classes representing different pages of the application.

modules/ui/selectors/: Holds selector definitions used by the Page Objects.

tests/ui/: Includes test cases that utilize the Page Objects to perform UI tests.

requirements.txt: Lists all Python dependencies required to run the project.

README.md: Provides an overview and instructions for the project.
