import time

from product_page_object import ProductPage


def test_count_number_of_items(page, login_to_page):
    product_page = ProductPage(page)
    time.sleep(1)
    assert product_page.count_number_of_items() == 6
