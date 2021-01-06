import enum

# Tipos de errores posibles para postgrestsql que considero que tendriamos
# Puden seguir agregando mas si es que los consideran necesarios o quitar
# Use esta pagina https://sqliteonline.com/ para ver que errores recibo
# por eso para el lexico y sintactico uso el 33 y para cuando el sintactico
# no se puede recuperar uso el 1


class ErrorType(enum.Enum):
    warning = 1
    no_data = 2
    sql_statement_not_yet_complete = 3
    connection_does_not_exist = 4
    case_not_found = 5
    data_exception = 6
    character_not_in_repertoire = 7
    division_by_zero = 8
    error_in_assignment = 9
    escape_character_conflict = 10
    invalid_argument_for_logarithm = 11
    invalid_argument_for_ntile_function = 12
    invalid_argument_for_nth_value_function = 13
    invalid_argument_for_power_function = 14
    invalid_argument_for_width_bucket_function = 15
    invalid_character_value_for_cast = 16
    invalid_datetime_format = 17
    invalid_row_count_in_limit_clause = 18
    invalid_row_count_in_result_offset_clause = 19
    invalid_use_of_escape_character = 20
    substring_error = 21
    foreign_key_violation = 22
    unique_violation = 23
    invalid_foreign_key = 24
    invalid_name = 25
    undefined_column = 26
    undefined_table = 27
    undefined_parameter = 28
    duplicate_column = 29
    duplicate_database = 30
    duplicate_table = 31
    duplicate_alias = 32
    syntax_error = 33
    internal_error = 34
    invalid_catalog_name = 35
    invalid_table_definition = 36
    invalid_data_type = 37
    duplicate_function = 38
    invalid_sql_statement_name = 39
# Este metodo rebice el numero de error, es decir de clase enum que esta arriba
# asi como warning es el 1, entonces para retornar su descripcion y id del error
# el metodo debe recibir como parametro el 1
# Observa la clase lex.py y syntactic.py como uso este metodo para que me hagarres
# la onda


def get_type_error(option):
    description = ''
    id_error = ''
    if ErrorType.warning.value == option:
        description = 'warning'
        id_error = '01000'
        return id_error, description
    elif ErrorType.syntax_error.value == option:
        description = 'syntax_error'
        id_error = '42601'
        return id_error, description
    elif ErrorType.no_data.value == option:
        description = 'no_data'
        id_error = '02000'
        return id_error, description
    elif ErrorType.sql_statement_not_yet_complete.value == option:
        description = 'sql_statement_not_yet_complete'
        id_error = '03000'
        return id_error, description
    elif ErrorType.connection_does_not_exist.value == option:
        description = 'connection_does_not_exist'
        id_error = '08003'
        return id_error, description
    elif ErrorType.case_not_found.value == option:
        description = 'case_not_found'
        id_error = '20000'
        return id_error, description
    elif ErrorType.data_exception.value == option:
        description = 'data_exception'
        id_error = '22000'
        return id_error, description
    elif ErrorType.character_not_in_repertoire.value == option:
        description = 'character_not_in_repertoire'
        id_error = '22021'
        return id_error, description
    elif ErrorType.division_by_zero.value == option:
        description = 'division_by_zero'
        id_error = '22012'
        return id_error, description
    elif ErrorType.error_in_assignment.value == option:
        description = 'error_in_assignment'
        id_error = '22005'
        return id_error, description
    elif ErrorType.escape_character_conflict.value == option:
        description = 'escape_character_conflict'
        id_error = '2200B'
        return id_error, description
    elif ErrorType.invalid_argument_for_logarithm.value == option:
        description = 'invalid_argument_for_logarithm'
        id_error = '2201E'
        return id_error, description
    elif ErrorType.invalid_argument_for_ntile_function.value == option:
        description = 'invalid_argument_for_ntile_function'
        id_error = '22014'
        return id_error, description
    elif ErrorType.invalid_argument_for_nth_value_function.value == option:
        description = 'invalid_argument_for_nth_value_function'
        id_error = '22016'
        return id_error, description
    elif ErrorType.invalid_argument_for_power_function.value == option:
        description = 'invalid_argument_for_power_function'
        id_error = '2201F'
        return id_error, description
    elif ErrorType.invalid_argument_for_width_bucket_function.value == option:
        description = 'invalid_argument_for_width_bucket_function'
        id_error = '2201G'
        return id_error, description
    elif ErrorType.invalid_character_value_for_cast.value == option:
        description = 'invalid_character_value_for_cast'
        id_error = '22018'
        return id_error, description
    elif ErrorType.invalid_datetime_format.value == option:
        description = 'invalid_datetime_format'
        id_error = '22007'
        return id_error, description
    elif ErrorType.invalid_row_count_in_limit_clause.value == option:
        description = 'invalid_row_count_in_limit_clause'
        id_error = '2201W'
        return id_error, description
    elif ErrorType.invalid_row_count_in_result_offset_clause.value == option:
        description = 'invalid_row_count_in_result_offset_clause'
        id_error = '2201X'
        return id_error, description
    elif ErrorType.invalid_use_of_escape_character.value == option:
        description = 'invalid_use_of_escape_character'
        id_error = '2200C'
        return id_error, description
    elif ErrorType.substring_error.value == option:
        description = 'substring_error'
        id_error = '22011'
        return id_error, description
    elif ErrorType.foreign_key_violation.value == option:
        description = 'foreign_key_violation'
        id_error = '23503'
        return id_error, description
    elif ErrorType.unique_violation.value == option:
        description = 'unique_violation'
        id_error = '23505'
        return id_error, description
    elif ErrorType.invalid_foreign_key.value == option:
        description = 'invalid_foreign_key'
        id_error = '42830'
        return id_error, description
    elif ErrorType.invalid_name.value == option:
        description = 'invalid_name'
        id_error = '42602'
        return id_error, description
    elif ErrorType.undefined_column.value == option:
        description = 'undefined_column'
        id_error = '42703'
        return id_error, description
    elif ErrorType.undefined_table.value == option:
        description = 'undefined_table'
        id_error = '42P01'
        return id_error, description
    elif ErrorType.undefined_parameter.value == option:
        description = 'undefined_parameter'
        id_error = '42P02'
        return id_error, description
    elif ErrorType.duplicate_column.value == option:
        description = 'duplicate_column'
        id_error = '42701'
        return id_error, description
    elif ErrorType.duplicate_database.value == option:
        description = 'duplicate_database'
        id_error = '42P04'
        return id_error, description
    elif ErrorType.duplicate_table.value == option:
        description = 'duplicate_table'
        id_error = '42P07'
        return id_error, description
    elif ErrorType.duplicate_alias.value == option:
        description = 'duplicate_alias'
        id_error = '42712'
        return id_error, description
    elif ErrorType.internal_error.value == option:
        description = 'internal_error'
        id_error = 'XX000'
        return id_error, description
    elif ErrorType.invalid_catalog_name.value == option:
        description = 'invalid_catalog_name'
        id_error = '3D000'
        return id_error, description
    elif ErrorType.invalid_table_definition.value == option:
        description = 'invalid_table_definition'
        id_error = '42P16'
        return id_error, description
    elif ErrorType.invalid_data_type.value == option:
        description = 'invalid_data_type'
        id_error = '22000'
        return id_error, description
    elif ErrorType.duplicate_function.value == option:
        description = 'duplicate_function'
        id_error = '42723'
        return id_error, description
    elif ErrorType.invalid_sql_statement_name.value == option:
        description = 'invalid_sql_statement_name'
        id_error = '26000'
        return id_error, description
