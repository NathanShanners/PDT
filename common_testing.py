# <editor-fold desc="File Header">
# Copyright   : Copyright information (if applicable)
# Author      : Author Name
# Date        : 17/10/2019
# Description : This python file contains all classes, functions and scripts related to testing (support for py.test)
# </editor-fold>

# <editor-fold desc="Import Control">
from contextlib import contextmanager
# </editor-fold>


# <editor-fold desc="Function to check if except is not raised when executed">
@contextmanager
def not_raises(exception):
    # Import control
    import pytest

    # Main code (error handling)
    try:
        yield
    except exception:
        raise pytest.fail("DID RAISE {0}".format(exception))
# </editor-fold>


# <editor-fold desc="Main script for this test file">
if __name__ == '__main__':
    a = 6
# </editor-fold>
