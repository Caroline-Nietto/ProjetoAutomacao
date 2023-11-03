# Arquivo conftest.py
import pytest


def pytest_configure(config):
    config.addinivalue_line("markers", "login_valido: Marcação para testes de login válidos")
    config.addinivalue_line("markers", "login_invalido: Marcação para testes de login inválidos")