import hashlib

def checksum(data, mode):
    f = list(map(_toString, data))
    b = _toByte(f)
    if mode == "SHA256":
        return sha(b)
    elif mode == "MD5":
        return md(b)
    else:
        return None


def sha(pieza):
    try:
        r = hashlib.sha256(pieza)
        return str(r.hexdigest())
    except:
        return None


def md(pieza):
    try:
        r = hashlib.md5(pieza)
        return str(r.hexdigest())
    except:
        return None

def _toString(data):
    if type(data) is str:
        return data
    l = ""
    for x in data:
        l = l + str(x)
    return l


def _toByte(data):
    d = ""
    for x in data:
        if type(x) is str:
            d += x
    return d.encode()


