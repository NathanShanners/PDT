# <editor-fold desc="File Header">
# Copyright   : Copyright information (if applicable)
# Author      : Author Name
# Date        : 18/10/2019
# Description : Python file contains all classes, functions and scripts related to the Python Development Template App
# </editor-fold>


# <editor-fold desc="Function containing all classes, functions and scripts related to main application">
def pdt_main_app(logger_name, params_dict):
    # Import control
    import logging
    import time

    # Start timer
    time_start = time.time()

    # Function logger (handlers typically picked up from parent)
    fcn_logger = logging.getLogger(logger_name + '.' + logger_name.lower() + '_main_app')
    fcn_logger.info('Executing main %s function' % logger_name)

    # Dummy function
    time.sleep(2)

    # Update log
    app_enable = params_dict['app_enable']
    fcn_logger.info('Application Enable Value = %s' % app_enable)
    time_elapsed = time.time() - time_start
    fcn_logger.info('Completed main %s function in %.2f Seconds' % (logger_name, time_elapsed))
# </editor-fold>


# <editor-fold desc="Main script to run code or tests">
if __name__ == "__main__":
    # Import control
    import time
    import sys
    from common_logger_control import create_logger
    from config_params_dict import config_params
    from common_config_control import read_config_file

    # Define variables
    app_tla = 'PDT'
    app_name = 'Python Development Template'
    app_version = '2019.10.26'
    ver_lgr_name = 'Version'
    config_filename = 'config.ini'
    loop_num = 0
    params_def_dict = config_params()  # Definition of all parameters expected in config file

    # Create loggers
    app_logger = create_logger(app_tla)
    ver_logger = create_logger(ver_lgr_name)

    # Update version log
    ver_logger.info('Starting %s Version %s' % (app_tla, app_version))

    # Main app code goes here
    while True:  # Continuous loop
        # Start timer
        start_time = time.time()

        # Update variables
        loop_num = loop_num + 1

        # Update log
        app_logger.info('Starting %s Application (version %s) Loop Number %d' % (app_tla, app_version, loop_num))

        # Read config file and update logger
        config_section = 'App ' + app_tla
        app_params_dict = read_config_file(app_tla, config_filename, config_section, params_def_dict[config_section])

        # Check for application exit
        # ToDo: Update code below to split out app config section first, then process section keys
        if app_params_dict['app_exit']:
            app_logger.info('Exiting %s' % app_name)
            sys.exit()

        # Run application if enabled, otherwise wait for next loop
        if app_params_dict['app_enable']:
            loop_freq = app_params_dict['loop_freq']
            app_logger.info('Running %s - Loop Freq %.2f Seconds' % (app_name, loop_freq))
            pdt_main_app(app_tla, app_params_dict)  # Run main application
        else:
            loop_freq = 5
            app_logger.info('%s Disabled - Loop Freq %.2f Seconds' % (app_name, loop_freq))

        # Check for next application loop
        while True:
            elapsed_time = time.time() - start_time
            if elapsed_time > loop_freq:
                break

        # Update log
        app_logger.info('Completed %s Loop Number %d' % (app_name, loop_num))
# </editor-fold>
