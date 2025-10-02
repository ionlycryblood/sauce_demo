import allure

class LoginPage:
    def __init__(self, page):
        self.page = page
        self.username_input = page.get_by_placeholder('Username')
        self.password_input = page.get_by_placeholder('Password')
        self.login_button = page.locator('#login-button')

    def load(self):
        with allure.step('loading url'):
            self.page.goto('https://www.saucedemo.com', timeout= 600000)

    def login(self, username, password):
        with allure.step(f'Login with {username}'):
            self.username_input.fill(username)
            self.password_input.fill(password)
            self.login_button.click()