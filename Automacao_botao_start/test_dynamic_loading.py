import pytest
from selenium import webdriver
from dynamic_loading_page import DynamicLoadingPage


class TestDynamicLoading:
    @pytest.fixture(autouse=True)
    def setup(self):
        self.driver = webdriver.Chrome()
        self.dynamic_loading_page = DynamicLoadingPage(self.driver)
        yield
        self.driver.quit()

    @pytest.mark.dynamic_loading
    def test_dynamic_loading(self):
        self.dynamic_loading_page.load()
        self.dynamic_loading_page.click_start()
        hello_world_text = self.dynamic_loading_page.wait_for_text()
        assert "Hello World" in hello_world_text
