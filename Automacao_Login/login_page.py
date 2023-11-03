from selenium.webdriver.common.by import By


class LoginPage:
    def __init__(self, driver):
        self.driver = driver
        self.url = "https://the-internet.herokuapp.com/login"
        # Seletor do botão de login
        self.login_button = (By.ID, "login")
        self.flash_message = (By.ID, "flash")


    def load(self):
        self.driver.get(self.url)

    # Método para realizar o login válido
    def realizar_login_valido(self, username, password):
        # Lógica para preencher os campos e fazer login válido
        username_input = self.driver.find_element(By.ID, "username")
        password_input = self.driver.find_element(By.ID, "password")
        username_input.send_keys(username)
        password_input.send_keys(password)
        login_button = self.driver.find_element(*self.login_button)
        login_button.click()

    # Método para realizar o login inválido
    def realizar_login_invalido(self, username, password):
        # Lógica para preencher os campos e fazer login inválido
        username_input = self.driver.find_element(By.ID, "username")
        password_input = self.driver.find_element(By.ID, "password")
        username_input.send_keys(username)
        password_input.send_keys(password)
        login_button = self.driver.find_element(*self.login_button)
        login_button.click()


