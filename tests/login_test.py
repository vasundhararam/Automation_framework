from selenium import webdriver
import pytest
import allure
from pages.loginpage import LoginPage
from pages.homepage import Homepage
from utils import utils as utils

class TestLogin():
        @pytest.fixture(scope="class")
        def test_setup(self):
            global driver
            driver = webdriver.Chrome(executable_path="C:/Users/keerthanasiddula/PycharmProjects/Automation_framework/drivers/chromedriver.exe")
            driver.implicitly_wait(5)
            driver.maximize_window()
            yield
            driver.close()
            driver.quit()
            print("Completed")
get_screenshot_as_png()

        def test_login(self,test_setup):
            driver.get(utils.URL)
            login_obj= LoginPage(driver)
            login_obj.enter_username(utils.USERNAME)
            login_obj.enter_password(utils.PASSWORD)
            login_obj.click_Login()
           #old codecdsfsjbkfbsjdkfdbgsjfdbgdjfgbdjcxv sncbfsjd
           # driver.find_element_by_id("txtUsername").send_keys("Admin")
           # driver.find_element_by_id("txtPassword").send_keys("admin123")
           # driver.find_element_by_id("btnLogin").click()


        def test_logout(self,test_setup):
        try:
            home_obj = Homepage(driver)
            home_obj.click_welcome()
            home_obj.click_logout()
            x= driver.title
            assert x== "OrangeHRM"

        except AssertionError as error:
            print("Assertionerror")
            print(error)
            raise

        except:
            print("there is an exception")
            raise

        else:
            print("No Exception occured")

        finally:
            print("Test Completed")
           # driver.find_element_by_id("welcome").click()
            #driver.find_element_by_link_text("Logout").click()

