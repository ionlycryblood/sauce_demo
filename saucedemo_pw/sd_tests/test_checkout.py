from ..sd_pages.checkout_page import CheckoutPage
from ..sd_pages.login_page import LoginPage
from ..sd_pages.chooseproduct import ChoosePage
from ..sd_pages.cart_page import CartPage
import pytest

@pytest.mark.parametrize('firstname, lastname, postalcode, expect',[
    ('','','', False),
    ('', 'Lill', '1234', False),
    ('Tim', '', '1234', False),
    ('Tim', 'Lill', '', False),
    ('Tim', 'Lill', '1234', True)
])
def test_checkout(page, firstname, lastname, postalcode, expect):
    login = LoginPage(page)
    login.load()
    login.login("standard_user", "secret_sauce")
    add_item = ChoosePage(page)
    add_item.go_to_cart()
    page.wait_for_url("**/cart.html")
    cart_page = CartPage(page)
    cart_page.checkout()
    checkout_page = CheckoutPage(page)
    checkout_page.info(firstname, lastname, postalcode)

    if not expect:
        assert page.locator("[data-test='error']").is_visible()
    else:
        assert 'checkout-step-two' in page.url