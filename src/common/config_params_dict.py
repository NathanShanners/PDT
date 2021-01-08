# <editor-fold desc="File Header">
# Copyright   :
# Description : Contains classes, functions and scripts related to defining config parameter names and types
# </editor-fold>


# <editor-fold desc="Function - Returns dictionary containing definition for jira config file">
def config_params():
    # Define dictionary for parameters
    params_dict = {  # Parameters to read from config, specifies section, variable name and type
        'PDT-App': {'app_exit': 'bool',
                    'app_enable': 'bool',
                    'loop_freq': 'int'},
        'PDT-Logger': {'file_handler_level': 'str',
                       'stream_handler_level': 'str'},
    }

    # Assign outputs
    return params_dict
# </editor-fold
