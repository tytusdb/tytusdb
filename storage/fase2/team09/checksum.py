import hashlib

def checksum(mode , data):
    lis = []
    for p in data:
        if ( mode == "sha"):
            lis.append(sha(p))
        else:
            lis.append(md(p))
    return lis

def sha(pieza):
    r = hashlib.sha256(str(pieza).encode())
    return r.hexdigest()

def md(pieza):
    r = hashlib.md5(str(pieza).encode())
    return r.hexdigest()

