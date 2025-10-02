import allure

class CartPage:
    def __init__(self, page):
        self.page = page
        self.checkout_button = page.get_by_role('button', name= 'Checkout')


    def checkout(self):
        with allure.step('checkout btn click'):
            self.checkout_button.click()