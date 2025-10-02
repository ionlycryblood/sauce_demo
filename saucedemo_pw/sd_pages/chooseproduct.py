class ChoosePage:
    def __init__(self, page):
        self.page = page
        page.first_product = page.locator("#add-to-cart-sauce-labs-bike-light")
        page.second_product = page.locator('#add-to-cart-sauce-labs-backpack')
        page.cart_button = page.locator(".shopping_cart_link")
        page.your_cart_text = page.get_by_text('Your Cart')



    def go_to_cart(self):
        self.page.first_product.click()
        self.page.second_product.click()
        self.page.cart_button.click()
        return self.page.locator("[data-test='item-quantity']").all_text_contents()

    def get_total_quantity(self):
        quantities = self.page.locator("[data-test='item-quantity']").all_text_contents()
        return sum(int(q) for q in quantities)

