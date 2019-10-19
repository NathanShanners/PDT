# <editor-fold desc="File Header">
# Copyright   : Copyright information (if applicable)
# Author      : Author Name
# Date        : 18/10/2019
# Description : Python file contains all classes, functions and scripts related to the Python Development Template App
# </editor-fold>


# <editor-fold desc="Function containing all classes, functions and scripts related to main PDT application">
def pdt_main_app(logger_name, config):
    # Import control
    import logging
    import time

    # Start timer
    time_start = time.time()

    # Function logger (handlers typically picked up from parent)
    fcn_logger = logging.getLogger(logger_name + '.pdt_main_app')
    fcn_logger.info('Executing main PDT function')

    # Dummy function
    time.sleep(2)

    # Update log
    app_enable = config['App PDT']['app_enable']
    fcn_logger.info('Application Enable Value = %s' % app_enable)
    time_elapsed = time.time() - time_start
    fcn_logger.info('Completed main PDT function in %.2f Seconds' % time_elapsed)
# </editor-fold>


# <editor-fold desc="Main script to run code or tests">
if __name__ == "__main__":
    # Import control
    import time
    import sys
    from common_logger_ctrl import create_logger
    from common_logger_ctrl import logger_config_update

    # Define variables
    app_version = "2019.10.19"
    app_lgr_name = 'PDT'
    ver_lgr_name = 'Version'
    loop_num = 0

    # Create loggers
    pdt_logger = create_logger(app_lgr_name)
    ver_logger = create_logger(ver_lgr_name)

    # Update version log
    ver_logger.info('Starting PDT Version %s' % app_version)

    # Main app code goes here
    while True:  # Continuous loop
        # Start timer
        start_time = time.time()

        # Update variables
        loop_num = loop_num + 1

        # Update log
        pdt_logger.info('Starting PDT Application (version %s) Loop Number %d' % (app_version, loop_num))

        # Read config file and update logger
        config_obj = logger_config_update(app_lgr_name, pdt_logger)  # Also reads config file
        # ToDo: Add config value checker for parameters & types

        # Check for application exit
        if config_obj['App PDT'].getboolean('app_exit'):
            pdt_logger.info('Exiting Python Development Template Application')
            sys.exit()

        # Run application if enabled, otherwise wait for next loop
        if config_obj['App PDT'].getboolean('app_enable'):
            loop_freq = config_obj['App PDT'].getfloat('loop_freq')
            pdt_logger.info('Running Python Development Template Application - Loop Freq %.2f Seconds'
                            % loop_freq)
            pdt_main_app(app_lgr_name, config_obj)  # Run main application
        else:
            loop_freq = 5
            pdt_logger.info('Python Development Template Application Disabled - Loop Freq %.2f Seconds'
                            % loop_freq)

        # Check for next application loop
        while True:
            elapsed_time = time.time() - start_time
            if elapsed_time > loop_freq:
                break

        # Update log
        pdt_logger.info('Completed PDT Application Loop Number %d' % loop_num)
# </editor-fold>
