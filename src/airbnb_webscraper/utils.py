# utils.py
""" Small functions used across python files """

from time import sleep
import random


def r_sleep(min_sleep):
    """
    A custom sleep with small randomness added to reduce tracing the webscraper 
    Args: min_sleep: The minimum time the script sleeps
    """
    return sleep(random.uniform(min_sleep, min_sleep+0.12))

def dict_subset(json_dict, *args):
    """
    For any dict, return a nested element of it as a new dict.
    Where *args is a series of key names, each a child element
    
    eg: json_dict['one'][2]['three'] == DictSubset(json_dict, 'one', 2, 'three')
    If the nested dict does not exist, returns None
    """
    
    result = json_dict
    for key in args:
        try:
            result = result[key]
        except (KeyError, IndexError, TypeError):
            return None
    return result