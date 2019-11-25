from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains


class DragAndDropPage:
    URL = "http://the-internet.herokuapp.com/drag_and_drop"

    source_column_a = (By.CSS_SELECTOR, "#column-a")
    source_column_b = (By.CSS_SELECTOR, "#column-b")

    def __init__(self, browser):
        self.browser = browser

    def load(self):
        self.browser.get(self.URL)

    def column_a_header(self):
        header_a = self.browser.find_element(*self.source_column_a)
        return header_a.text

    def column_b_header(self):
        header_b = self.browser.find_element(*self.source_column_b)
        return header_b.text

    def perform_dragndrop(self):
        source_element = self.browser.find_element(*self.source_column_a)
        dest_element = self.browser.find_element(*self.source_column_b)
        # ActionChains(self.browser).drag_and_drop(source_element, dest_element).perform()
        ActionChains(self.browser).click_and_hold(source_element).move_to_element(dest_element).release(source_element).perform()
        # ActionChains(self.browser).move_to_element(source_element).click_and_hold(source_element).move_by_offset(100,0).release(source_element).perform()
