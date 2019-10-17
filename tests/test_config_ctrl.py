# <editor-fold desc="File Header">
# Copyright   : Copyright information (if applicable)
# Author      : Author Name
# Date        : 17/10/2019
# Description : This python file contains all classes, functions and scripts related to testing config control
# </editor-fold>


# <editor-fold desc="Function to test the config file exists">
def test_config_file_exists():
    # Import control
    import os.path

    # Declare variables
    config_filename = 'config.ini'

    # Check file exists
    assert os.path.exists(config_filename), 'Config file "config.ini" does not exist'  # Check config file exists
# </editor-fold>


# <editor-fold desc="Function to test the config file error handling works">
def test_config_file_control():
    # Import control
    import pytest
    from common_config_ctrl import config_open_file
    from common_testing import not_raises

    # Check error handling
    with not_raises(Exception):  # Check that error does not get raised as error handling should occur
        config_dict = config_open_file('not_a_config_file.ini')
    if config_dict != 'Error':  # Check variable does get assigned the string value of "Error" when file doesn't exist
        raise pytest.fail('Config object did not indicate error occurred when trying to read non-existent file')
# </editor-fold>


# <editor-fold desc="Function to test the config file has all the required parameters">
def test_config_parameters():
    # Import control
    import pytest
    from common_config_ctrl import config_open_file

    # Declare variables
    config_filename = "config.ini"

    # Read config file
    config = config_open_file(config_filename)

    # Check file reads correctly
    if config == 'Error':  # Error occurred when reading as config is a string rather than config object
        raise pytest.fail('Config object indicates error occurred when trying to read config file')

    # Check sections
    section = 'Logger PDT'
    assert config.has_section(section), 'Section %s does not exist in config file' % section

    # Check keys
    section = 'Logger PDT'
    key = 'file_handler_level'
    assert config.has_option(section, key), \
        'Section %s does not contain key %s in config file' % (section, key)

    section = 'Logger PDT'
    key = 'stream_handler_level'
    assert config.has_option(section, key), \
        'Section %s does not contain key %s in config file' % (section, key)
# </editor-fold>


# <editor-fold desc="Main script for this test file">
if __name__ == '__main__':
    test_config_parameters()
    a = 6
# </editor-fold>
