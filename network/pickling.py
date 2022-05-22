"""
Pickling process to serialize and de-serialize a dictionary inot different either JSON, XML, or binary format
"""

import json, pickle
from dicttoxml import dicttoxml

def to_json(dictionary: dict()) :
    """
    Converts "dictionary" to JSON and returns it

    Parameters:
        dictionary (dict): a dictionary list 
    """
    return json.dumps(dictionary).encode("utf-8")


def to_xml(dictionary: dict()):
    """
    Converts "dictionary" to XML and returns it
    
    Parameters:
        dictionary (dict): a dictionary list 
    """
    return dicttoxml(dictionary)


def to_bin(dictionary: dict()):
    """
    Converts "dictionary" to binary and returns it
    
    Parameters:
        dictionary (dict): a dictionary list """
    string = json.dumps(dictionary)
    # Return the binary "str" file
    return ' '.join(format(ord(letter), 'b') for letter in string).encode("utf-8")
