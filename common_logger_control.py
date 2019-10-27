# <editor-fold desc="File Header">
# Copyright   : Copyright information (if applicable)
# Author      : Author Name
# Date        : 18/10/2019
# Description : This python file contains all classes, functions and scripts related to logger and logging control
# </editor-fold>


# <editor-fold desc="Function to create logger">
def create_logger(logger_name):
    # Standard setup has the handler
    # Import control
    import logging

    # Create logger
    # Note : Only log levels >= this level will be executed for all handlers
    logger = logging.getLogger(logger_name)
    logger.setLevel(logging.DEBUG)

    # File handler
    fh = logging.FileHandler(logger_name + '.log')
    fh.setLevel(logging.INFO)

    # Console handler
    ch = logging.StreamHandler()
    ch.setLevel(logging.INFO)

    # Create formatter
    formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')

    # Assign formatter to handlers
    fh.setFormatter(formatter)
    ch.setFormatter(formatter)

    # Add handlers to the logger
    logger.addHandler(fh)
    logger.addHandler(ch)

    logger.info('Started main logger for %s' % logger_name)

    return logger
# </editor-fold>


# <editor-fold desc="Function to update logger handlers from config file">
def logger_config_update(config_filename, logger_name, logger):
    # Import control
    from common_config_control import config_open_file
    import logging

    # Function logger (handlers typically picked up from parent)
    fcn_logger = logging.getLogger(logger_name + '.common_logger_control.logger_config_update')
    fcn_logger.info('Updating logger configuration')

    # Read config file
    config = config_open_file(logger_name, config_filename)

    # Parse parameters
    try:
        fh_level = config['Logger ' + logger_name]['file_handler_level']  # String : Reporting level file handlers
        sh_level = config['Logger ' + logger_name]['stream_handler_level']  # String : Reporting level stream handlers
        for handler in logger.handlers:
            handler_type = handler.__class__.__name__
            if handler_type == "FileHandler":
                handler.setLevel(fh_level)
            elif handler_type == "StreamHandler":
                handler.setLevel(sh_level)
        fcn_logger.info('Logger configuration updated successfully')
    except KeyError as error:
        fcn_logger.error(error)

    # Return config object as it's been read
    return config
# </editor-fold>


# <editor-fold desc="Function to list all currently active loggers">
def logger_list_active(logger_name):
    # Import control
    import logging

    # Function logger
    fcn_logger = logging.getLogger(logger_name + '.common_logger_control.logger_list_active')
    fcn_logger.info('Getting dictionary of all active loggers')

    # Get a dictionary of all loggers
    loggers_dict = [logging.getLogger(name) for name in logging.root.manager.loggerDict]

    # Update log
    fcn_logger.info('Currently there are %d loggers active' % (len(loggers_dict)-3))

    # Return dictionary
    return loggers_dict
# </editor-fold>


# <editor-fold desc="Main script to run code or tests">
if __name__ == "__main__":

    # Define variables
    lgr_name = 'PDT'
    cfg_filename = 'config.ini'

    # Create logger
    app_logger = create_logger(lgr_name)

    # Test messages
    app_logger.debug('Debug message')
    app_logger.info('Info message')
    app_logger.warning('Warning message')
    app_logger.error('Error message')

    # Update logger from config file
    logger_config_update(cfg_filename, lgr_name, app_logger)

    # Test messages
    app_logger.debug('Debug message')
    app_logger.info('Info message')
    app_logger.warning('Warning message')
    app_logger.error('Error message')

    logger_list_active(lgr_name)
# </editor-fold>
