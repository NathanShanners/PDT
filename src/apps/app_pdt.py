# <editor-fold desc="File Header">
# Copyright   :
# Description : Python file contains all classes, functions and scripts related to the Python Development Template
# </editor-fold>


# <editor-fold desc="Main application function for Python Development Template">
def pdt_main_app(logger_name):
    # <editor-fold desc="Import Control">
    import logging
    import time
    from time import sleep
    # </editor-fold>

    # <editor-fold desc="Define Constants">
    fcn_name = 'pdt_main_app'
    fcn_purpose = 'Python Development Template main function'
    # </editor-fold>

    # <editor-fold desc="Declare Variables">
    time_start = time.time()  # Start timer
    # </editor-fold>

    # <editor-fold desc="Function logger (handlers typically picked up from parent)">
    logger_name = logger_name + '.' + fcn_name
    fcn_logger = logging.getLogger(logger_name)
    fcn_logger.info(fcn_purpose)
    # </editor-fold>

    # <editor-fold desc="Main Code">
    fcn_logger.debug('Sleeping for 2 seconds')
    sleep(2)
    # </editor-fold>

    # Update log
    time_elapsed = time.time() - time_start
    fcn_logger.info('Completed %s in %.2f Seconds' % (fcn_purpose, time_elapsed))
# </editor-fold>


# <editor-fold desc="Script : Main script to run code or tests">
if __name__ == "__main__":
    # <editor-fold desc="Import Control">
    import os
    import sys
    import time
    from time import sleep
    from common_logger_control import create_logger
    from config_params_dict import config_params
    from common_config_control import read_config_file
    from alive_progress import alive_bar
    # </editor-fold>

    # <editor-fold desc="Define Constants">
    app_tla = 'PDT'
    app_name = 'Python Development Template'
    app_version = '2021.01.05d'
    ver_lgr_name = 'Version'
    config_filename = 'config.ini'
    loop_num = 0
    params_def_dict = config_params()  # Definition of all parameters expected in config file
    # </editor-fold>

    # <editor-fold desc="Create Loggers">
    app_logger = create_logger(app_tla)
    ver_logger = create_logger(ver_lgr_name)
    # </editor-fold>

    # <editor-fold desc="Update version log">
    ver_logger.info('Starting %s Version %s' % (app_tla, app_version))
    # </editor-fold>

    # <editor-fold desc="Main App Code">
    while True:  # Continuous loop
        # <editor-fold desc="Update variables">
        start_time = time.time()  # Start Timer
        loop_num = loop_num + 1  # Increment App Loop Counter
        # </editor-fold>

        # <editor-fold desc="Update Log">
        app_logger.info('Starting %s Application (version %s) Loop Number %d' % (app_tla, app_version, loop_num))
        # </editor-fold>

        # <editor-fold desc="Read config file and update logger">
        config_section = app_tla + '-App'
        app_params_dict = read_config_file(app_tla, config_filename, config_section, params_def_dict[config_section])
        # </editor-fold>

        # <editor-fold desc="Check for application exit">
        if app_params_dict['app_exit']:
            app_logger.info('Exiting %s' % app_name)
            sys.exit()
        # </editor-fold>

        # <editor-fold desc="Run application if enabled, otherwise wait for next loop">
        if app_params_dict['app_enable']:
            loop_freq = app_params_dict['loop_freq']
            app_logger.info('Running %s - Loop Freq %.2f Seconds' % (app_name, loop_freq))
            pdt_main_app(app_tla)  # Run main application
        else:
            loop_freq = 5
            app_logger.info('%s Disabled - Loop Freq %.2f Seconds' % (app_name, loop_freq))
        # </editor-fold>

        # <editor-fold desc="Check for next application loop">
        app_logger.info('Waiting for next loop...')
        elapsed_time = int(time.time() - start_time)
        with alive_bar(loop_freq) as bar:  # default setting
            for bar_count in range(loop_freq):
                if bar_count < elapsed_time:
                    sleep(0.01)
                else:
                    sleep(1)
                bar()
        # </editor-fold>

        # <editor-fold desc="Update Log">
        app_logger.info('Completed %s Loop Number %d' % (app_name, loop_num))
        app_logger.info(' ')
        app_logger.info(' ')
        os.system('cls' if os.name == 'nt' else 'clear')
        # </editor-fold>
    # </editor-fold>
# </editor-fold>
