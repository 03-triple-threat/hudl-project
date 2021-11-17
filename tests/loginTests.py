import time
import unittest
from selenium import webdriver

from pages import LoginPage
from pages.LoginPage import LoginPageClass, HomePageClass, LoginOrganizationPage


class loginTests(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        self.driver.get("https://www.hudl.com/login")

    def tearDown(self):
        self.driver.close()
        self.driver.quit()

    def test_invalid_login_no_email_no_password(self):
        loginPage = LoginPageClass
        loginPage.login(self, '', '')

        assert loginPage.loginErrorMessageIsDisplayed(self)
        assert loginPage.loginErrorMessageText(self) == LoginPageClass.loginErrorMessage

    def test_invalid_login_no_email_with_password(self):
        loginPage = LoginPageClass
        loginPage.login(self, '', LoginPageClass.INVALID_PASSWORD)

        assert loginPage.loginErrorMessageIsDisplayed(self)
        assert loginPage.loginErrorMessageText(self) == LoginPageClass.loginErrorMessage

    def test_invalid_login_valid_email_no_password(self):
        loginPage = LoginPageClass
        loginPage.login(self, LoginPageClass.VALID_EMAIL, '')

        assert loginPage.loginErrorMessageIsDisplayed(self)
        assert loginPage.loginErrorMessageText(self) == LoginPageClass.loginErrorMessage

    def test_invalid_login_valid_email_invalid_password(self):
        loginPage = LoginPageClass
        loginPage.login(self, LoginPageClass.VALID_EMAIL, LoginPageClass.INVALID_PASSWORD)

        assert loginPage.loginErrorMessageIsDisplayed(self)
        assert loginPage.loginErrorMessageText(self) == LoginPageClass.loginErrorMessage

    def test_valid_login_valid_email_valid_password(self):
        loginPage = LoginPageClass
        loginPage.login(self, '', '') #TODO - enter valid username & password

        homePage = HomePageClass

        assert self.driver.current_url == "https://www.hudl.com/home"
        assert homePage.userProfileNameText(self) == HomePageClass.userProfileNameString

    def test_invalid_organization_login_invalid_email(self):
        loginPage = LoginPageClass
        loginPage.clickLoginWithOrganization(self)

        assert self.driver.current_url == "https://www.hudl.com/app/auth/login/organization"

        loginOrganizationPage = LoginOrganizationPage
        loginOrganizationPage.login(self, loginOrganizationPage.VALID_EMAIL)
        time.sleep(5)

        assert self.driver.current_url == "https://www.hudl.com/login?e=6"
        assert loginPage.loginWithOrganizationErrorIsDisplayed(self)
        # assert loginPage.loginWithOrganizationErrorText(self) == loginPage.loginWithOrganizationErrorText(self)







