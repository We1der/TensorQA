import pytest
from selenium import webdriver
import logging


logging.basicConfig(level=logging.INFO, filename="logfile.log", filemode="w",
                    format="%(asctime)s %(levelname)s %(message)s")


@pytest.fixture(scope="session")
def browser():
    driver = webdriver.Chrome()
    logging.info("new driver was created")
    yield driver
    driver.quit()
    logging.info("driver was closed")
