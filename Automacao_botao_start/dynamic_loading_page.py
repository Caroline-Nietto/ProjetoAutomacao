from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class DynamicLoadingPage:
    def __init__(self, driver):
        self.driver = driver
        self.url = "https://the-internet.herokuapp.com/dynamic_loading/1"

    def load(self):
        self.driver.get(self.url)

    def click_start(self):
        start_button = self.driver.find_element(By.XPATH, "//div[@id='start']/button")
        start_button.click()

    def wait_for_text(self):
        # Aguarda até que o elemento com o texto 'Hello World' seja visível
        hello_world_element = WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located((By.ID, "finish"))
        )
        return hello_world_element.text
