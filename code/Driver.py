from dataclasses import dataclass


@dataclass
class DriverInfo:
    """Represents dataclass of information about 'Driver'.

    Arguments:
        id (int): ID of 'Driver'.
        f_name (str): First name of 'Driver'.
        l_name (str): Last name of 'Driver'.
        age (int): Age of 'Driver'.
        work_experience (int): Work experience in years of 'Driver'.

    """
    id: int
    f_name: str
    l_name: str
    age: int
    work_experience: int


class Driver:
    """Represents class 'Driver'.

    Properties:
        @property
        driver_info ():
            Returns parameter '_driver_info'.

        @driver_info.setter
        driver_info (driver_info: DriverInfo):
            Setting parameter '_driver_info' values of 'driver_info'.

    """
    def __init__(self):
        self._driver_info = None

    @property
    def driver_info(self):
        return self._driver_info

    @driver_info.setter
    def driver_info(self, driver_info: DriverInfo):
        if isinstance(driver_info, DriverInfo):
            self._driver_info = driver_info
