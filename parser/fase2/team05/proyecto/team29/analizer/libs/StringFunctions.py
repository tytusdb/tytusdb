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


def trim_(opt, chars, string):
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
        r = hashlib.md5(s.encode())
        col.append(r.hexdigest())
    return col


def sha256(string1):
    string1 = str_to_list(string1)
    col = []
    for s in string1:
        r = hashlib.sha256(s.encode())
        col.append(r.hexdigest())
    return col


def substr(string1, start, end):
    string1 = str_to_list(string1)
    return [s[start:end] for s in string1]


def get_byte(string, num):
    strings = str_to_list(string)
    col = []
    for s in strings:
        if num > len(s):
            # Aqui deberia estar un error de lenght
            col.append(None)
        else:
            byte_ = ord(s[num])
            col.append(byte_)
    return col


def convert_date(string):
    string = str_to_list(string)
    print(string)
    return [datetime.strptime(s, "%d/%m/%Y") for s in string]


def convert_int(string):
    string = str_to_list(string)
    return [int(s) for s in string]


def set_byte(string, index, byte_):
    strings = str_to_list(string)
    col = []
    for s in strings:
        if index > len(s):
            # TODO: Aqui deberia estar un error de lenght
            col.append(None)
        else:
            s = s[:index] + chr(byte_) + s[index + 1 :]
            col.append(s)
    return col


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
