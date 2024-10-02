import pytest
import logging
import inspect


@pytest.mark.usefixtures("setup")
class BaseClass:

    def getLogger(self):
        loggerName = inspect.stack()[1][3]     # Give the name of the method in which the logger method is being called
        logger = logging.getLogger(loggerName)

        # Creating object from the parent, to set the log file name
        fileHandler = logging.FileHandler('logfile.log')

        # Set the log format and set it to an object
        formatter = logging.Formatter("%(asctime)s : %(levelname)s : %(name)s : %(message)s")

        # Connecting the format to the fileHandler object
        fileHandler.setFormatter(formatter)

        # Give the file name information to the 'logger' object created previously
        logger.addHandler(fileHandler)

        # Set Level what will be printed, based on these default order: debug, info, warning, error, critical
        logger.setLevel(logging.INFO)  # This will only print log from info, warning, error, critical (without debug)

        return logger
