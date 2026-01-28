from selenium import webdriver
import pytest

@pytest.fixture()
def setup(browser):
    if browser == "chrome":
        driver = webdriver.Chrome()
        print("Launching Chrome......")
    elif browser == "firefox":
        driver = webdriver.Firefox()
        print("Launching Firefox......")
    else:
        driver = webdriver.Chrome()
        print("Launching Chrome by default......")

    return driver


def pytest_addoption(parser):
    parser.addoption("--browser", action="store", default="chrome")


@pytest.fixture()
def browser(request):
    return request.config.getoption("--browser")

# ##### Pytest HtMl report###
# def pytest_configure(config):
#     config.metadata['Project Name'] = 'nop Commerce'
#     config.metadata['Module Name'] = 'Customers'
#     config.metadata['Tester'] = 'Nishpavg'
#
# #it is hook for delete /Modify Enivronment info to HTML Report
# @pytest.mark.optionalhook
# def pytest_metadata(metadata):
#     metadata.pop("Java_home",None)
#     metadata.pop("Plugins",None)

import pytest

def pytest_configure(config):
    if hasattr(config, "metadata"):
        config.metadata['Project Name'] = 'nop Commerce'
        config.metadata['Module Name'] = 'Customers'
        config.metadata['Tester'] = 'Nishpavg'

def pytest_metadata(metadata):
    metadata.pop("JAVA_HOME", None)
    metadata.pop("Plugins", None)




