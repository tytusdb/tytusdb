import ply.lex as lex

tokens = []

reservadas = {
    'smallint': 'SMALLINT',
    'integer' 'INTEGER'
    'bigint': 'BIGINT',
    'decimal': 'DECIMAL',
    'numeric': 'NUMERIC',
    'real': 'REAL',
    'double': 'DOUBLE',
    'money': 'MONEY',
    'character': 'CHARACTER',
    'varying':  'VARYING',
    'varchar': 'VARCHAR',
    'char': 'CHAR',
    'text': 'TEXT',
    'timestamp': 'TIMESTAMP',
    'date': 'DATE',
    'time': 'TIME',
    'interval': 'INTERVAL',
    'year': 'YEAR',
    'month':  'MONTH',
    'day': 'DAY',
    'hour':    'HOUR',
    'minute': 'MINUTE',
    'second': 'SECOND',
    'year_to_month': 'YEAR_TO_MONTH',
    'day_to_hour': 'DAY_TO_HOUR',
    'dat_to_minute': 'DAY_TO_MINUTE',
    'day_to_second:': 'DAY_TO_SECOND',
    'hour_to_minute:': 'HOUR_TO_MINUTE',
    'hour_to_second': 'HOUR_TO_SECOND',
    'minute_to_second': 'MINUTE_TO_SECOND',
    'boolean': 'BOOLEAN',
    'table': 'TABLE',
    'create': 'CREATE',
    'or': 'OR',
    'replace': 'REPLACE',
    'except':'EXCEPT'

}


