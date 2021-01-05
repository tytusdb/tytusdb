from parse.symbol_table import *
import os
import shutil
import pickle
from grammarReview import *


def save_st(symbol_table: SymbolTable):
    st_file = open('stored_st.bin', 'wb')
    pickle.dump(symbol_table, st_file)
    st_file.close()


def load_st():
    try:
        st_file = open('stored_st.bin', 'rb')
        return pickle.load(st_file)
    except FileNotFoundError:
        return SymbolTable([])


def exec_sql(input_string):
    symbol_table = load_st()
    execute_from_wrapper(symbol_table, input_string)
    save_st(symbol_table)


def report_stored_st():
    symbol_table = load_st()
    symbol_table.report_symbols()


def clear_all_execution():
    if os.path.exists('stored_st.bin'):
        os.remove('stored_st.bin')
    shutil.rmtree('data')
