import pytest
from selenium import webdriver
from pages.dragndrop import DragAndDropPage


@pytest.fixture
def browser():
    driver = webdriver.Chrome()
    driver.implicitly_wait(10)
    yield driver
    driver.quit()

def test_drag_column_a_to_column_b(browser):
    dragndrop_page = DragAndDropPage(browser)
    dragndrop_page.load()

    dragndrop_page.perform_dragndrop()
    assert dragndrop_page.column_a_header() == "B"
    assert dragndrop_page.column_b_header() == "A"