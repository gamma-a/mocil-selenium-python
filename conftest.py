import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By


@pytest.fixture(scope="class")
def setup(request):
    driver = webdriver.Chrome()
    driver.get("https://qamocil.dipostar.org/")
    #driver.get("https://www.mocil.id/")
    driver.maximize_window()
    driver.implicitly_wait(4)
    driver.find_element(By.XPATH, "//div/button[@value='accept']").click()  # Accept cookies
    request.cls.driver = driver  # assign the 'driver' from the local var to the other class driver variable

    yield  # yield = executed at the end after the test is performed
    driver.close()
