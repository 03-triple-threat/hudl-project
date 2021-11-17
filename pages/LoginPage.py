import time

from selenium.webdriver.common.by import By


class BasePage(object):
    def __init__(self, driver):
        self.driver = driver
        time.sleep(3)

    ##STRINGS
    VALID_EMAIL = 'ajhurtado3@gmail.com'
    INVALID_PASSWORD = "password123"


class LoginPageClass(BasePage):
    ## LOCATORS
    emailInput = (By.ID, 'email')
    passwordInput = (By.ID, 'password')
    signInButton = (By.ID, 'logIn')
    loginError = (By.CSS_SELECTOR, 'div.login-error.fade-in-expand > div > p')
    loginWithOrganizationButton = (By.ID, 'logInWithOrganization')
    loginWithOrganizationError = (By.CSS_SELECTOR, 'div.login-error-code > div')

    ## STRINGS
    validEmail = "ajhurtado3@gmail.com"
    invalidPassword = "password123"
    loginErrorMessage = "We didn't recognize that email and/or password. Need help?"
    loginWithOrganizationErrorMessage = "This account can't log in with an organization yet. Please log in using your email and password."

    def login(self, email, password):
        userElement = self.driver.find_element(*LoginPageClass.emailInput)
        userElement.send_keys(email)

        pwElement = self.driver.find_element(*LoginPageClass.passwordInput)
        pwElement.send_keys(password)

        signInButtonElement = self.driver.find_element(*LoginPageClass.signInButton)
        signInButtonElement.click()
        time.sleep(5)

    def loginErrorMessageIsDisplayed(self):
        loginErrorMessageElement = self.driver.find_element(*LoginPageClass.loginError)
        return loginErrorMessageElement.is_displayed()

    def loginErrorMessageText(self):
        loginErrorMessageElement = self.driver.find_element(*LoginPageClass.loginError)
        return loginErrorMessageElement.text
        print(loginErrorMessageElement.text)

    def clickLoginWithOrganization(self):
        loginWithOrganizationButtonElement = self.driver.find_element(*LoginPageClass.loginWithOrganizationButton)
        loginWithOrganizationButtonElement.click()
        time.sleep(3.5)

    def loginWithOrganizationErrorIsDisplayed(self):
        loginWithOrganizationErrorElement = self.driver.find_element(*LoginPageClass.loginWithOrganizationError)
        return loginWithOrganizationErrorElement.is_displayed()

    def loginWithOrganizationErrorText(self):
        loginWithOrganizationErrorElement = self.driver.find_element(*LoginPageClass.loginWithOrganizationError)
        return loginWithOrganizationErrorElement.text


class HomePageClass(BasePage):
    ##LOCATORS
    userProfileName = (By.CSS_SELECTOR, 'div.user-fields > div > a')

    ##STRINGS
    userProfileNameString = 'AJ Hurtado'  ## TODO - update with tester's name

    def userProfileNameText(self):
        userProfileNameElement = self.driver.find_element(*HomePageClass.userProfileName)
        return userProfileNameElement.text


class LoginOrganizationPage(BasePage):
    ##LOCATORS
    emailInput = (By.ID, 'uniId_1')
    loginButton = (By.CSS_SELECTOR, 'form > div.uni-bg--level0.uni-padding--one > button')

    def login(self, username):
        emailInputElement = self.driver.find_element(*LoginOrganizationPage.emailInput)
        emailInputElement.send_keys(username)

        loginButtonElement = self.driver.find_element(*LoginOrganizationPage.loginButton)
        loginButtonElement.click()