from .base_page import BasePage
from .locators import ProductPageLocators
class ProductPage(BasePage):

    def add_product_to_basket(self):
        self.click_on_element(*ProductPageLocators.ADD_TO_BASKET_BUTTON)
