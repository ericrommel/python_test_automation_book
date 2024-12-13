from playwright.sync_api import Page

class ProductPage:
    # Initialize page and selectors
    def __init__(self, page: Page):
        self.page = page
        self.number_of_items = page.locator(".inventory_item_name")



    def count_number_of_items(self) -> int:
        return self.number_of_items.count()