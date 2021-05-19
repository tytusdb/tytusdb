import os

from parserT28.controllers.symbol_table import SymbolTable


class SymbolTableReport(object):
    def __init__(self):
        self._symbolTable = SymbolTable()
        self._data = ''

    def generateReport(self):
        self._data = 'digraph {\n\ttbl [\n\tshape=plaintext\n\tlabel=<'
        self._data += '\n\t\t<table border=\'0\' cellborder=\'1\' color=\'#324960\' cellspacing=\'0\'>'
        self._data += '\n\t\t\t<tr>\n\t\t\t\t<td bgcolor="#324960" colspan=\'8\' SIDES=\"TB\">'
        self._data += f"\n\t\t\t\t\t<font color=\"white\">SYMBOL TABLE</font>"
        self._data += '\n\t\t\t\t</td>\n\t\t\t</tr>'

        self.generateHeaders()

        self._data += '\n\t\t</table>\n\t>];\n}'

        return self._data

    def generateHeaders(self):
        self._data += '\n\t\t\t<tr>'
        self.dataHeaderCol('ID')
        self.dataHeaderCol('Name')
        self.dataHeaderCol('Value')
        self.dataHeaderCol('Type')
        self.dataHeaderCol('Environment')
        self.dataHeaderCol('References')
        self.dataHeaderCol('Line')
        self.dataHeaderCol('Column')
        self._data += '\n\t\t\t</tr>'

        for col in self._symbolTable.getList():
            self._data += '\n\t\t\t<tr>'
            self.dataCol(col.idSymbol)
            self.dataCol(col.name)
            self.dataCol(col.value)
            self.dataCol(col.dataType)
            self.dataCol(col.environment)
            self.dataCol(col.references)
            self.dataCol(col.row)
            self.dataCol(col.column)
            self._data += '\n\t\t\t</tr>'

    def dataHeaderCol(self, name):
        self._data += f"\n\t\t\t\t<td bgcolor=\"#4fc3a1\" SIDES=\"B\"><b><font color=\"white\"> {name} </font></b></td>"

    def dataCol(self, data):
        self._data += f"\n\t\t\t\t<td SIDES=\"B\"> {data} </td>"
