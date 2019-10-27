# <editor-fold desc="File Header">
# Copyright   : Copyright information (if applicable)
# Author      : Author Name
# Date        : 18/10/2019
# Description : Python file contains all classes, functions and scripts related to the Python Development Template App
# </editor-fold>


# <editor-fold desc="Function containing all classes, functions and scripts related to main application">
def jta_main_app(logger_name, config):
    # Import control
    import logging
    import time

    # Define variables
    fcn_app_tla = 'PDT'

    # Start timer
    time_start = time.time()

    # Function logger (handlers typically picked up from parent)
    fcn_logger = logging.getLogger(logger_name + '.' + fcn_app_tla.lower() + '_main_app')
    fcn_logger.info('Executing main %s function' % app_tla)

    # Dummy function
    time.sleep(2)

    # Update log
    app_enable = config['App ' + fcn_app_tla]['app_enable']
    fcn_logger.info('Application Enable Value = %s' % app_enable)
    time_elapsed = time.time() - time_start
    fcn_logger.info('Completed main %s function in %.2f Seconds' % (fcn_app_tla, time_elapsed))
# </editor-fold>


# <editor-fold desc="Main script to run code or tests">
if __name__ == "__main__":
    # Import control
    import time
    import sys
    from common_logger_control import create_logger
    from common_logger_control import logger_config_update

    # Define variables
    app_tla = 'PDT'
    app_name = 'Python Development Template'
    app_version = '2019.10.26'
    ver_lgr_name = 'Version'
    config_filename = 'config.ini'
    loop_num = 0

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
        config_obj = logger_config_update(config_filename, app_tla, app_logger)  # Also reads config file
        # ToDo: Add config value checker for parameters & types

        # Check for application exit
        # ToDo: Update code below to split out app config section first, then process section keys
        if config_obj['App ' + app_tla].getboolean('app_exit'):
            app_logger.info('Exiting %s' % app_name)
            sys.exit()

        # Run application if enabled, otherwise wait for next loop
        if config_obj['App ' + app_tla].getboolean('app_enable'):
            loop_freq = config_obj['App ' + app_tla].getfloat('loop_freq')
            app_logger.info('Running %s - Loop Freq %.2f Seconds' % (app_name, loop_freq))
            jta_main_app(app_tla, config_obj)  # Run main application
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
