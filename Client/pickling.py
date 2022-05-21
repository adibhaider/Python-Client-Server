import json

from dicttoxml import dicttoxml


def to_json(dictionary):
    """Converts "dictionary" to JSON and returns it"""
    return json.dumps(dictionary).encode("utf-8")


def to_xml(dictionary):
    """Converts "dictionary" to XML and returns it"""
    return dicttoxml(dictionary)


def to_bin(dictionary):
    """Converts "dictionary" to binary and returns it"""
    string = json.dumps(dictionary)
    # Return the binary "str" file
    return ' '.join(format(ord(letter), 'b') for letter in string).encode("utf-8")
