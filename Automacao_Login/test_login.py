import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from login_page import LoginPage


@pytest.mark.usefixtures("setup")
class TestLogin:
    @pytest.fixture(autouse=True)
    def setup(self):
        self.driver = webdriver.Chrome()
        yield
        self.driver.quit()

    @pytest.mark.login_valido
    def test_login_valido(self):
        page = LoginPage(self.driver)
        page.load()  # Carrega a página de login
        page.realizar_login_valido("tomsmith", "SuperSecretPassword!")

    @pytest.mark.login_invalido
    def test_login_invalido(self):
        page = LoginPage(self.driver)
        page.load()  # Carrega a página de login
        page.realizar_login_invalido("usuario_invalido", "senha_invalida")


