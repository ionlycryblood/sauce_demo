from ..sd_pages.login_page import LoginPage
from ..sd_pages.chooseproduct import ChoosePage
from ..sd_pages.cart_page import CartPage
from ..sd_pages.checkout_page import CheckoutPage
from ..sd_pages.overview import OverviewPage
from ..sd_pages.complete import CompletePage



def test_full_purchase_flow(page):
    login_page = LoginPage(page)
    login_page.load()
    login_page.login("standard_user", "secret_sauce")
    assert "inventory" in page.url

    product_page = ChoosePage(page)
    product_page.go_to_cart()
    assert page.your_cart_text.is_visible()


    cart_page = CartPage(page)
    cart_page.checkout()

    check_page = CheckoutPage(page)
    check_page.info('tim', 'lill', '1234')
    assert page.get_by_text('Total: $10.79').is_visible()

    finish_page = OverviewPage(page)
    finish_page.finish()

    complete_page = CompletePage(page)
    complete_page.success()
    assert page.get_by_text('Thank you for your order!').is_visible()






