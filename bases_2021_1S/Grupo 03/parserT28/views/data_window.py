from tkinter import *
from tkinter import ttk
from tkinter import scrolledtext
from pandas.core.frame import DataFrame
from prettytable import PrettyTable

from parserT28.utils.decorators import singleton


@singleton
class DataWindow(object):
    def __init__(self):
        self._console = None

        self._data = ''
        self._headers = []
        self._rows = []

    @property
    def console(self):
        return self._console

    @property
    def data(self):
        return self._data

    @property
    def headers(self):
        return self._headers

    @property
    def rows(self):
        return self._rows

    def clearProperties(self):
        self._data = ''
        self._headers = []
        self._rows = []

    @console.setter
    def console(self, frame):
        Label(frame, text='Consola', borderwidth=0,
              font='Arial 15 bold', width=52, bg='#3c3f41', foreground='#fff').grid(row=3, column=1)
        x_scroll = Scrollbar(frame, orient='horizontal')
        y_scroll = Scrollbar(frame, orient='vertical')

        self._console = Text(frame, borderwidth=0, height=35,
                             width=70, bg='#1c1c1e', foreground='#9efb01', undo=True, wrap='none', xscrollcommand=x_scroll.set, yscrollcommand=y_scroll.set)

        y_scroll.config(command=self._console.yview)
        y_scroll.grid(column=1, row=4, sticky='NE', ipady=255, padx=12)
        x_scroll.config(command=self._console.xview)
        x_scroll.grid(column=1, row=5, sticky='NS', ipadx=255)

    def consoleText(self, data):
        if self._console is None:
            self._data = f"{data}\n\n"
            print(f"{data}\n\n")
        else:
            self._data = f"{data}\n\n"
            self._console.insert(INSERT, f"{data}\n\n")

    def consoleTable(self, headers: list, rows: list):
        table = PrettyTable()
        table.field_names = headers
        for row in rows:
            table.add_row(row)
        if self._console is None:
            self._headers = headers
            for row in rows:
                self._rows.append(row)
            self._data = f"{table}\n\n"

            print(INSERT, f"{table}\n\n")
        else:
            self._data = f"{table}\n\n"
            self._console.insert(INSERT, f"{table}\n\n")

    def format_df(self, df: DataFrame):
        table = PrettyTable([''] + list(df.columns))
        self._headers = list(df.columns)

        for row in df.itertuples():
            table.add_row(row)
            self._rows.append(row)

        self._data = f"{str(table)}\n\n"
        return str(table)

    def format_table_list(self, array: list):
        try:
            table_value = PrettyTable(array[0])
            table_value.add_row(array[1])

            self._headers = array[0]

            for row in array[1]:
                self._rows.append(row)

            self._data = f"{str(table_value)}\n\n"

            return str(table_value)
        except:
            desc = "FATAL ERROR, Funciones Select"
            # ErrorController().add(34, 'Execution', desc, 0, 0)

    def clearConsole(self):
        self._console.delete('1.0', END)
