import hashlib
import os.path as path


def checksum_database(type: int, database: str, mode_db, data):
    # sha256 -> 1
    if type == 1:
        return __generate_checksum_db_mode(1, database, mode_db, data)
    # md5 -> 2
    elif type == 2:
        return __generate_checksum_db_mode(2, database, mode_db, data)
    else:
        return None


def checksum_table(type: int, database: str, mode_db, data):
    # sha256 -> 1
    if type == 1:
        return __generate_checksum_table(1, database, mode_db, data)
    # md5 -> 2
    elif type == 2:
        return __generate_checksum_table(2, database, mode_db, data)
    else:
        return None


def generate_md5(data):
    return hashlib.md5(data).hexdigest()


def generate_sha256(data):
    return hashlib.sha256(data).hexdigest()


def read_file(filename: str, tipo):
    if path.exists(filename):
        file = open(filename, "rb")
        data = file.read()
        final_hash = generate_md5(data) if tipo == 1 else generate_sha256(data)
        return final_hash
    return "File doesn't exist"


def __generate_checksum_db_mode(mode: int, db: str, mode_db: str, data):
    hash = hashlib.sha256() if mode == 1 else hashlib.md5()
    if mode_db == "b":
        if isinstance(data, list):
            for table in data:
                hash.update(table)
        return hash.hexdigest()
    if isinstance(data, list):
        for table in data:
            if mode_db == "avl":
                hash.update(open(f"./data/avlMode/{db}_{table}.tbl", "rb").read())

            elif mode_db == "bPlus".lower():
                hash.update(open(f"./data/BPlusMode/{db}/{table}/{table}.bin", "rb").read())
            elif mode_db == "dict":
                hash.update(open(f"./data/{db}/{table}.bin", "rb").read())
            elif mode_db == "hash":
                hash.update(open(f"./data/hash/{db}/{table}.bin", "rb").read())
            elif mode_db == "isam":
                hash.update(open(f"./data/ISAMMODE/tables/{db}{table}.bin", "rb").read())
            elif mode_db == "json":
                hash.update(open(f"./data/json/{db}-{table}", "rb").read())
        return hash.hexdigest()
    else:
        return None


def __generate_checksum_table(mode: int, db: str, mode_db: str, data):
    hash = hashlib.sha256() if mode == 1 else hashlib.md5()
    if mode_db.lower().strip() == "avl":
        hash.update(open(f"./data/avlMode/{db}_{data}.tbl", "rb").read())
    elif mode_db.lower().strip() == "b":
        if isinstance(data, list):
            for tuple in data:
                hash.update(tuple)
    elif mode_db.lower().strip() == "bPlus".lower():
        hash.update(open(f"./data/BPlusMode/{db}/{data}/{data}.bin", "rb").read())
    elif mode_db.lower().strip() == "dict":
        hash.update(open(f"./data/{db}/{data}.bin", "rb").read())
    elif mode_db.lower().strip() == "hash":
        hash.update(open(f"./data/hash/{db}/{data}.bin", "rb").read())
    elif mode_db.lower().strip() == "isam":
        hash.update(open(f"./data/ISAMMode/tables/{db}{data}.bin", "rb").read())
    elif mode_db.lower().strip() == "json":
        hash.update(open(f"./data/json/{db}-{data}", "rb").read())

    return hash.hexdigest()
