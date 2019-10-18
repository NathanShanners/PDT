# <editor-fold desc="File Header">
# Copyright   : Copyright information (if applicable)
# Author      : Author Name
# Date        : 17/10/2019
# Description : This python file contains all classes, functions and scripts related to testing config control
# </editor-fold>


# <editor-fold desc="Import Control">
import sys
import pytest
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
        config_dict = config_open_file(None, 'not_a_config_file.ini')
    if config_dict != 'Error':  # Check variable does get assigned the string value of "Error" when file doesn't exist
        raise pytest.fail('Config object did not indicate error occurred when trying to read non-existent file')
# </editor-fold>


# <editor-fold desc="Function to define reference config data dictionaries (initialise)">
def create_ref_config_dict():
    # Initialise variables
    cfg_dict = dict()
    sec_dict = dict()

    # Create dictionary for section 'Logger PDT'
    sec = 'Logger PDT'  # Define section name
    sec_dict['file_handler_level'] = 'INFO'
    sec_dict['stream_handler_level'] = 'INFO'
    cfg_dict[sec] = sec_dict  # Update main data dictionary

    # Assign output of function
    return cfg_dict
# </editor-fold>


# <editor-fold desc="Function to test if provided section exists in the provided config object">
def section_test(config_obj, sec):
    assert config_obj.has_section(sec), 'Section %s does not exist in config file' % sec
# </editor-fold>


# <editor-fold desc="Function to test if provided section and key exist in the provided config object">
def section_key_test(config_obj, sec, sec_key):
    assert config_obj.has_option(sec, sec_key), \
        'Section %s does not contain key %s in config file' % (sec, sec_key)
# </editor-fold>


# <editor-fold desc="Function to test the config file has all the required parameters">
# ToDo: Fix tests for Linux OS
@pytest.mark.skipif(sys.platform == "linux", reason="tests for windows only")
def test_config_parameters():
    # Import control
    import pytest
    from common_config_ctrl import config_open_file

    # Declare variables
    config_filename = "config.ini"

    # Read config file
    config = config_open_file(None, config_filename)

    # Check file reads correctly
    if config == 'Error':  # Error occurred when reading as config is a string rather than config object
        raise pytest.fail('Config object indicates error occurred when trying to read config file')

    # Create reference data dictionary for config variables
    ref_config_dict = create_ref_config_dict()

    # Check every section in reference data dictionary
    for section in ref_config_dict:
        section_test(config, section)

    # Check every key in reference data dictionary
    for section in ref_config_dict:
        section_dict = ref_config_dict[section]
        for key in section_dict:
            print('Section %s, Key %s, Value %s' % (section, key, section_dict[key]))
            section_key_test(config, section, key)
# </editor-fold>


# <editor-fold desc="Main script for this test file">
if __name__ == '__main__':
    test_config_file_exists()
# </editor-fold>
