# <editor-fold desc="File Header">
# Copyright   : Copyright information (if applicable)
# Author      : Author Name
# Date        : 17/10/2019
# Description : This python file contains all classes, functions and scripts related to config file control
# </editor-fold>


# <editor-fold desc="Function to open the requested config file">
def config_open_file(config_filename):
    # Import Control
    import os.path
    import configparser

    #  Define variables
    cwd = os.getcwd()
    if cwd.find('\\tests'):
        print('Replacing tests in file path, assuming in test mode')
    cwd = cwd.replace('\\tests', '')  # Replace tests folder (used for py.test)
    config_file_path = cwd + '\\' + config_filename
    # Read config file & parse parameters
    if os.path.exists(config_file_path):
        config = configparser.ConfigParser()
        config.read(config_file_path)
    else:  # Config file is missing
        print('Config file is missing %s' % config_file_path)
        config = 'Error'

    # Return output from function
    return config
# </editor-fold>


# <editor-fold desc="Main script to run code or tests">
if __name__ == "__main__":
    a = 1
# </editor-fold>
