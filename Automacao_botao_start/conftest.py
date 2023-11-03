# Arquivo conftest.py
import pytest


def pytest_configure(config):
    config.addinivalue_line("markers", "dynamic_loading: Marcação para clicar no botao start")
