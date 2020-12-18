import hashlib
import datetime
import base64


def str_to_list(str):
    return str if isinstance(str, list) else [str]


def lenght(string1):
    string1 = str_to_list(string1)
    return [len(s) for s in string1]


def substring(string1, start, end):
    string1 = str_to_list(string1)
    return [s[start:end] for s in string1]


def trim_(opt, string, chars):
    opt = opt.lower()
    if opt == "trailing":
        return trim_trailing(string, chars)
    if opt == "leading":
        return trim_leading(string, chars)
    if opt == "both":
        return trim_both(string, chars)
    else:
        return []


def trim_leading(string1, characters):
    string1 = str_to_list(string1)
    return [s.lstrip(characters) for s in string1]


def trim_trailing(string1, characters):
    string1 = str_to_list(string1)
    return [s.rstrip(characters) for s in string1]


def trim_both(string1, characters):
    string1 = str_to_list(string1)
    return [s.strip(characters) for s in string1]


def md5(string1):
    string1 = str_to_list(string1)
    col = []
    for s in string1:
        col.append(hashlib.md5(s.encode()))
        col.append(s.hexdigest())
    return col


def sha256(string1):
    string1 = str_to_list(string1)
    col = []
    for s in string1:
        col.append(hashlib.sha256(s.encode()))
        col.append(s.hexdigest())
    return col


def substr(string1, start, end):
    string1 = str_to_list(string1)
    return [s[start:end] for s in string1]


def get_byte(string, num):
    string = str_to_list(string)
    col = []
    for s in string:
        byte_array = bytes(s, "utf-8")
        if len(byte_array) > num:
            col.append(byte_array[num])
    return col


def convert_date(string):
    string = str_to_list(string)
    return [datetime.strptime(s, "%Y-%m-%d %H:%M:%S") for s in string]


def convert_int(string):
    string = str_to_list(string)
    return [int(s) for s in string]


# LAS FUNCIONES DE ABAJO NO FUNCIONAN CON COLUMNAS:
def set_byte(string, num, num2):
    byte_array = bytes(string, "utf-8")
    array = list()
    i = 0
    for value in byte_array:
        array.insert(i + 1, int(str(value)))
        i += 1
    if len(array) > num:
        array[num] = num2
    byte_array = bytes(array)
    return byte_array


def encode_string(string, format):
    if format == "escape":
        return string
    elif format == "base64":
        string = bytes(string, "utf-8")
        string_base64 = base64.b64encode(string)
        return string_base64
    elif format == "hex":
        return string.encode("utf-8").hex()


def decode_string(string, format):
    if format == "escape":
        return string
    elif format == "base64":
        print("escape")
    elif format == "hex":
        print("escape")
