# <editor-fold desc="File Header">
# Copyright   : Copyright information (if applicable)
# Author      : Author Name
# Date        : 18/10/2019
# Description : This python file contains all classes, functions and scripts related to configuration of testing
# </editor-fold>


# <editor-fold desc="Import Control">
import os
import sys
# </editor-fold>


# <editor-fold desc="Path control">
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
# </editor-fold>


# <editor-fold desc="PyTest Config">
# def pytest_configure(config):
#     config.addinivalue_line(
#         "markers", "env(name): mark test to run only on named environment"
#     )
# </editor-fold>
