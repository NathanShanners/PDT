# <editor-fold desc="File Header">
# Copyright   :
# Description : This python file contains all classes, functions and scripts related to logger and logging control
# </editor-fold>


# <editor-fold desc="Python file variables">
filename = 'common_logger_control'  # Name of python filename (useful for logger traceability)
# </editor-fold>


# <editor-fold desc="Function to create logger">
def create_logger(parent_logger):
    # Standard setup has the handler
    # Import control
    import logging

    # Create logger
    # Note : Only log levels >= this level will be executed for all handlers
    logger = logging.getLogger(parent_logger)
    logger.setLevel(logging.DEBUG)

    # File handler
    fh = logging.FileHandler(parent_logger + '.log')
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

    logger.info('Started main logger for %s' % parent_logger)

    return logger
# </editor-fold>


# <editor-fold desc="Function to update logger handlers from config file">
def logger_config_update(config_filename, logger_name):
    # <editor-fold desc="Import Control">
    from common_config_control import config_open_file
    import logging
    import sys
    # </editor-fold>

    # <editor-fold desc="Define Constants">
    fcn_name = 'logger_config_update'
    # </editor-fold>

    # <editor-fold desc="Function logger (handlers typically picked up from parent)">
    logger_name = logger_name + '.' + fcn_name
    fcn_logger = logging.getLogger(logger_name)
    fcn_logger.debug('Updating logger configuration')
    # </editor-fold>

    # <editor-fold desc="Extract Parent Logger Name (required for reading config file)">
    parent_logger_name = logger_name.split('.')[0]
    # </editor-fold>

    # <editor-fold desc="Read config file">
    config = config_open_file(parent_logger_name, config_filename)
    if config == 'Error':  # Error when reading config file, likely file is missing
        fcn_logger.error('Reading config file error, application will now exit')
        sys.exit()  # Exit application
    fh_level = 'INFO'
    sh_level = 'INFO'
    config_read_flag = False
    try:
        fh_level = config[parent_logger_name + '-Logger']['file_handler_level']  # String : Reporting level file handlers
        sh_level = config[parent_logger_name + '-Logger']['stream_handler_level']  # String : Reporting level stream handlers
        config_read_flag = True  # Indicate config file section parsed successfully
    except KeyError as error:
        fcn_logger.debug('Could not find config section %s to update Logger', error)
    # </editor-fold>

    # <editor-fold desc="Update Logger Handlers With Settings From Config File">
    if config_read_flag:
        try:
            parent_logger = logging.getLogger(parent_logger_name)
            for handler in parent_logger.handlers:
                handler_type = handler.__class__.__name__
                if handler_type == "FileHandler":
                    handler.setLevel(fh_level)
                elif handler_type == "StreamHandler":
                    handler.setLevel(sh_level)
            fcn_logger.debug('Logger configuration updated successfully')
        except KeyError as error:
            fcn_logger.error(error)
    # </editor-fold>

    # <editor-fold desc="Return config object as it's been read">
    return config
    # </editor-fold>
# </editor-fold>


# <editor-fold desc="Function to list all currently active loggers">
def logger_list_active(parent_logger):
    # Import control
    import logging

    # Constants
    fcn_name = 'logger_list_active'

    # Function logger (handlers typically picked up from parent)
    logger_name = parent_logger + '.' + filename + '.' + fcn_name
    fcn_logger = logging.getLogger(logger_name)
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
    lgr_name = 'TesterApp'
    cfg_filename = 'config.ini'

    # Create logger
    app_logger = create_logger(lgr_name)

    # Test messages
    app_logger.debug('Debug message')
    app_logger.info('Info message')
    app_logger.warning('Warning message')
    app_logger.error('Error message')

    # Update logger from config file
    logger_config_update(cfg_filename, lgr_name)

    # Test messages
    app_logger.debug('Debug message')
    app_logger.info('Info message')
    app_logger.warning('Warning message')
    app_logger.error('Error message')

    logger_list_active(lgr_name)
# </editor-fold>
