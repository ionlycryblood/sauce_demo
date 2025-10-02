import allure

class OverviewPage:
    def __init__(self, page):
        self.page = page
        self.finish_button = page.get_by_role('button', name = 'finish')

    def finish(self):
        with allure.step('finish btn click'):
            self.finish_button.click()

