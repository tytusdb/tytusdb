from enum import Enum
class DBType(Enum):
    smallint = 0
    integer = 1
    bigint = 2
    decimal = 3
    numeric = 4
    real = 5
    double_precision = 6
    money = 7
    ch_varying = 8
    varchar=9
    character = 10
    char = 11
    text = 12
    timestamp_wtz = 13
    timestamp_tz = 14
    date = 15
    time_wtz = 16
    time_tz = 17
    interval = 18
    boolean =  19