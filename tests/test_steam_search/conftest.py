import pytest
from driver.driver import DriverSingleton


@pytest.fixture(scope='function')
def driver():
    drv = DriverSingleton.get_driver()
    yield drv
    DriverSingleton.quit_driver()