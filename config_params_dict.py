# <editor-fold desc="File Header">
# Copyright   : Copyright information (if applicable)
# Author : Author
# Date : 12/07/2019
# Description : Contains classes, functions and scripts related to defining config parameter names and types
# </editor-fold>


# <editor-fold desc="Function - Returns dictionary containing definition for jira config file">
def config_params():
    # Define dictionary for parameters
    params_dict = {  # Parameters to read from config, specifies section, variable name and type
        'Logger PDT': {'file_handler_level': 'str',
                       'stream_handler_level': 'str'},
        'App PDT': {'app_exit': 'bool',
                    'app_enable': 'bool',
                    'loop_freq': 'int'},
    }

    # Assign outputs
    return params_dict
# </editor-fold
