import allure

class CartPage:
    def __init__(self, page):
        self.page = page
        page.checkout_button = page.get_by_role('button', name= 'checkout')


    def checkout(self):
        with allure.step('checkout btn click'):
            self.page.checkout_button.click()

