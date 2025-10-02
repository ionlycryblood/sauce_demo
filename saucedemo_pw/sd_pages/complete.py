import allure

class CompletePage:
    def __init__(self, page):
        self.page = page
        self.back_home_button = page.get_by_role('button', name = 'back-to-products')
        self.success_message = page.get_by_text('Thank you for your order!')

    def success(self):
        with allure.step('makin sure we completed successfully'):
            return self.success_message.is_visible()