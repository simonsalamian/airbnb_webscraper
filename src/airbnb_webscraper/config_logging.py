# config_logging.py
import logging

def setup_logging(location=None, log_level='INFO'):
    """
    Configures and returns a logger for Airbnb scraping processes.

    Sets the logging level, output format, and attaches a console handler. The logger
    can optionally include a location prefix in each log message.

    Args:
        location (str | None): Optional location name to prepend to each log message.
        log_level (str): Minimum logging level as a string (e.g., 'INFO', 'DEBUG', 'WARNING').

    Returns:
        logging.Logger: Configured logger instance for use in the application.
    """

    ## Create a logger
    logger = logging.getLogger('airbnb_logger')
    numeric_level = getattr(logging, log_level.upper(), logging.INFO)
    logger.setLevel(numeric_level)

    ## Create a formatter
    formatter = logging.Formatter(f'{location} | %(message)s')

    ## Create a stream handler for optional console output
    console_handler = logging.StreamHandler()
    console_handler.setLevel(numeric_level)
    if location:
        console_handler.setFormatter(formatter)
    
    ## Remove all handlers associated with the logger
    logger.handlers = []

    ## Add the file and console handlers to the logger
    logger.addHandler(console_handler)

    return logger