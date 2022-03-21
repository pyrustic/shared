import os
import os.path
import json
import math


def json_dump(json_filename, data, pretty=False):
    with open(json_filename, "w") as file:
        indent = None
        if pretty:
            indent = 4
        json.dump(data, file, indent=indent)


def json_load(json_filename):
    with open(json_filename, "r") as file:
        data = json.load(file)
    return data


def valid_dossier(name, directory):
    dossier_path = os.path.join(directory, name)
    meta_filename = os.path.join(dossier_path, "DOSSIER")
    data_dir = os.path.join(dossier_path, "data")
    if not os.path.isfile(meta_filename):
        return False
    if not os.path.isdir(data_dir):
        return False
    return True


def convert_size(size):
    """ Size should be in bytes.
    Return a tuple (float_or_int_val, str_unit) """
    if size == 0:
        return (0, "B")
    KILOBYTE = 1024
    size_name = ("B", "KB", "MB", "GB", "TB", "PB", "EB", "ZB", "YB")
    i = int(math.floor(math.log(size, KILOBYTE)))
    p = math.pow(KILOBYTE, i)
    result = round(size/p, 2)
    return result, size_name[i]
