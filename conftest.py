pytest_plugins = [
    "src.fixtures"
]


def pytest_addoption(parser):
    parser.addini("browser_name", "Browser name for tests")
