# <editor-fold desc="File Header">
# Copyright   :
# Description : This python file contains all classes, functions and scripts related to config file control
# </editor-fold>


# <editor-fold desc="Python file variables">
filename = 'common_config_control'  # Name of python filename (useful for logger traceability)
# </editor-fold>


# <editor-fold desc="Function to open the requested config file">
def config_open_file(logger_name, config_filename):
    # Import Control
    import os.path
    import configparser
    import logging

    # Constants
    fcn_name = 'config_open_file'

    # Function logger (handlers typically picked up from parent)
    if logger_name is not None:
        fcn_logger = logging.getLogger(logger_name + '.' + fcn_name)
    else:
        fcn_logger = None

    #  Define variables
    cwd = os.getcwd()
    if '\\tests' in cwd:
        cwd = cwd.replace('\\tests', '')  # Replace tests folder (used for py.test)
        if logger_name is not None:
            fcn_logger.info('Replacing tests in file path, assuming in test mode')
    config_file_path = cwd + '\\' + config_filename
    # Read config file & parse parameters
    if os.path.exists(config_file_path):
        config = configparser.ConfigParser()
        config.read(config_file_path)
    else:  # Config file is missing
        config = 'Error'
        if logger_name is not None:
            fcn_logger.error('Config file is missing %s' % config_file_path)

    # Return output from function
    return config
# </editor-fold>


# <editor-fold desc="Function - Config File Reader">
def read_config_file(logger_name, cfg_filename, section, params_dict_def):
    # <editor-fold desc="Function Info">
    # Copyright : InnoQuanTech Ltd
    # Description : Function which reads a specific section of a config file
    #               If an error is encountered the whole application will terminate
    # </editor-fold>

    # Import control
    from common_variable_control import custom_convert
    from common_variable_control import auto_update_dict
    from common_logger_control import logger_config_update
    import sys
    import logging

    # Constants
    fcn_name = 'read_config_file'

    # Function logger (handlers typically picked up from parent)
    if logger_name is not None:
        logger_name = logger_name + '.' + fcn_name
        fcn_logger = logging.getLogger(logger_name)
    else:
        fcn_logger = None

    # Import Configuration
    config = logger_config_update(cfg_filename, logger_name)  # Updates logger and reads config file

    # Read parameters from Config file
    params_dict = {}
    # TODO: Split the following code as a common function or method for config control
    if section in config:
        for param_name in params_dict_def:
            try:
                param_value_str = config[section][param_name]  # Read parameter from config (all will be strings)
                param_type = params_dict_def[param_name]
                param_value = custom_convert(param_type, param_value_str)
                params_dict = auto_update_dict(params_dict, param_name, param_value)
            except KeyError:
                fcn_logger.error('Error: Reading variable "%s" from section "%s" in config file' %
                                 (param_name, section))
                sys.exit()  # Exit application
                # TODO: May want to just return an error flag to allow the caller to decide if the app should terminate
    # Write output of function
    return params_dict
# </editor-fold


# <editor-fold desc="Main script to run code or tests">
if __name__ == "__main__":
    a = 1
# </editor-fold>
