from enum import Enum


Type = {
    "SMALLINT": "NUMERIC",
    "INTEGER": "NUMERIC",
    "BIGINT": "NUMERIC",
    "DECIMAL": "NUMERIC",
    "NUMERIC": "NUMERIC",
    "REAL": "NUMERIC",
    "DOUBLE": "NUMERIC",
    "MONEY": "NUMERIC",
    "CHARACTER": "CHARACTER",
    "VARYING": "CHARACTER",
    "VARCHAR": "CHARACTER",
    "CHAR": "CHARACTER",
    "TEXT": "CHARACTER",
    "DATE": "TIME",
    "TIME": "TIME",
    "BOOLEAN": "BOOLEAN",
    "TIMESTAMP": "TIME",
}