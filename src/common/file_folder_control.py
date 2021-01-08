# <editor-fold desc="File Header">
# Copyright   :
# Description : Contains classes, functions and scripts related to file and folder control
# </editor-fold>

# <editor-fold desc="Function to save provided variable to local Pickle file using provided file path">
# If the provided folder path does not exist it will be created
def save_var_to_pkl(logger_name, save_var, filename, folder="", folder_root=""):
    # <editor-fold desc="Import Control">
    import time
    import logging
    import pickle
    from pathlib import Path
    # </editor-fold>

    # <editor-fold desc="Define Constants">
    fcn_name = 'save_var_to_pkl'
    fcn_purpose = 'Saving variable to local pickle file'
    # </editor-fold>

    # <editor-fold desc="Define Variables">
    time_start = time.time()  # Start timer
    # </editor-fold>

    # <editor-fold desc="Function logger (handlers typically picked up from parent)">
    logger_name = logger_name + '.' + fcn_name
    fcn_logger = logging.getLogger(logger_name)
    fcn_logger.info(fcn_purpose)
    # </editor-fold>

    # <editor-fold desc="Root folder control">
    if not folder_root:  # Specific root folder not provided so use current working directory
        folder_root = Path.cwd()  # Get current working directory
    else:
        folder_root = Path(folder_root)
    # </editor-fold>

    # <editor-fold desc="File and Folder Path Control">
    filename_path = folder_root / folder / (filename.replace('.pkl', '') + '.pkl')  # Create full path to file
    filename_path.parent.mkdir(parents=True, exist_ok=True)  # Create folder if required
    # </editor-fold>

    # <editor-fold desc="Store results in Pickle file">
    fcn_logger.debug('Saving provided variable in file %s' % filename_path)  # Update log
    with open(filename_path, 'wb') as f:
        pickle.dump(save_var, f)
    # </editor-fold>

    # <editor-fold desc="Update Profiler & Log">
    time_elapsed = time.time() - time_start
    fcn_logger.debug('Completed %s in %.2f Seconds' % (fcn_purpose, time_elapsed))
    # </editor-fold>
# </editor-fold>


# <editor-fold desc="Function to save provided variable to local Pickle file using provided file path">
# If the provided folder path does not exist it will be created
def load_var_from_pkl(logger_name, filename, folder="", folder_root=""):
    # <editor-fold desc="Import Control">
    import sys
    import time
    import logging
    import pickle
    from pathlib import Path
    # </editor-fold>

    # <editor-fold desc="Define Constants">
    fcn_name = 'load_var_from_pkl'
    fcn_purpose = 'Loading variable from local pickle file %s' % filename
    # </editor-fold>

    # <editor-fold desc="Define Variables">
    time_start = time.time()  # Start timer
    # </editor-fold>

    # <editor-fold desc="Function logger (handlers typically picked up from parent)">
    logger_name = logger_name + '.' + fcn_name
    fcn_logger = logging.getLogger(logger_name)
    fcn_logger.info(fcn_purpose)
    # </editor-fold>

    # <editor-fold desc="Root folder control">
    if not folder_root:  # Specific root folder not provided so use current working directory
        folder_root = Path.cwd()  # Get current working directory
    else:
        folder_root = Path(folder_root)
    # </editor-fold>

    # <editor-fold desc="File and Folder Path Control">
    filename_path = folder_root / folder / (filename.replace('.pkl', '') + '.pkl')  # Create full path to file
    if not filename_path.exists():  # File does not exist
        fcn_logger.info('The file %s does not exist - exiting' % filename_path)
        sys.exit()
    # </editor-fold>

    # <editor-fold desc="Load Pickle file">
    fcn_logger.debug('Loading file %s' % filename_path)  # Update log
    with open(filename_path, 'rb') as f:
        load_var = pickle.load(f)
    # </editor-fold>

    # <editor-fold desc="Update Profiler & Log">
    time_elapsed = time.time() - time_start
    fcn_logger.debug('Completed %s in %.2f Seconds' % (fcn_purpose, time_elapsed))
    # </editor-fold>

    # <editor-fold desc="Return variables from function">
    return load_var
    # </editor-fold>
# </editor-fold>


# <editor-fold desc="Main script to run code or tests">
if __name__ == "__main__":
    # <editor-fold desc="Import Control">
    import os
    import sys
    from common_logger_control import create_logger
    from config_params_dict import config_params
    from common_config_control import read_config_file
    import pickle
    # </editor-fold>

    # <editor-fold desc="Define Constants">
    app_tla = 'HSA'
    config_filename = 'config.ini'
    params_def_dict = config_params()  # Definition of all parameters expected in config file
    cwd = os.getcwd()  # Get current working directory
    # </editor-fold>

    # <editor-fold desc="Create Loggers">
    app_logger = create_logger(app_tla)
    # </editor-fold>

    # <editor-fold desc="Update Log">
    app_logger.info('Running test for HXY Dividend Transaction Processing')
    # </editor-fold>

    # <editor-fold desc="Read variables from config file - Main Application">
    config_section = app_tla + '-App'
    app_params_dict = read_config_file(app_tla, config_filename, config_section, params_def_dict[config_section])
    # </editor-fold>

    # <editor-fold desc="Main Code">
    save_variable = 'Test Value'
    save_var_to_pkl(app_tla, save_variable, 'test', 'Test')
    load_variable = load_var_from_pkl(app_tla, 'test')
    # </editor-fold>
