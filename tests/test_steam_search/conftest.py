import pytest
from driver.driver import DriverSingleton


@pytest.fixture(scope='function')
def driver():
    driver = DriverSingleton.get_driver()
    yield driver
    DriverSingleton.quit_driver()