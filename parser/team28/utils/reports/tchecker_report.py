import os

from controllers.type_checker import TypeChecker


class TypeCheckerReport(object):
    def __init__(self):
        self._typeChecker = TypeChecker()
        self._data = ''
        self.generateReport()

        report = open('typeChecker.dot', 'w')
        report.write(self._data)
        report.close()
        os.system('dot -Tpng typeChecker.dot -o typeChecker.png')

    def generateReport(self):
        self._data = 'digraph {\n\ttbl [\n\tshape=plaintext\n\tlabel=<'
        self._data += '\n\t\t<table border=\'0\' cellborder=\'1\' color=\'#324960\' cellspacing=\'0\'>'
        self.generateDatabases()
        self._data += '\n\t\t</table>\n\t>];\n}'

    def generateDatabases(self):
        databases = self._typeChecker.getList()

        for db in databases:
            self._data += '\n\t\t\t<tr>\n\t\t\t\t<td bgcolor="#324960" colspan=\'5\'>'
            self._data += f"\n\t\t\t\t\t<font color=\"white\">DATABASE: {db.name}</font>"
            self._data += '\n\t\t\t\t</td>\n\t\t\t</tr>'
            self.generateTables(db)
            self._data += '\n\t\t\t<tr>\n\t\t\t\t<td colspan=\'5\' SIDES="T"> </td>\n\t\t\t</tr>'

    def generateTables(self, database):
        for tb in database.tables:
            self._data += '\n\t\t\t<tr>\n\t\t\t\t<td bgcolor="#4fc3a1" colspan=\'5\' SIDES="LR">'
            self._data += f"\n\t\t\t\t\t<font color=\"white\">TABLE: {tb.name}</font>"
            self._data += '\n\t\t\t\t</td>\n\t\t\t</tr>'
            self.generateColumns(tb)

    def generateColumns(self, table):

        self._data += '\n\t\t\t<tr>'
        self.dataHeaderCol('Name')
        self.dataHeaderCol('Data Type')
        self.dataHeaderCol('Length')
        self.dataHeaderCol('Not Null')
        self.dataHeaderCol('Primary Key')
        self._data += '\n\t\t\t</tr>'

        for col in table.columns:
            self._data += '\n\t\t\t<tr>'
            self.dataCol(col.name)
            self.dataCol(col.dataType)
            self.dataCol(col.length)
            self.dataCol(col.notNull)
            self.dataCol(col.primaryKey)
            self._data += '\n\t\t\t</tr>'

    def dataHeaderCol(self, name):
        self._data += f"\n\t\t\t\t<td SIDES=\"B\"><b> {name} </b></td>"

    def dataCol(self, data):
        self._data += f"\n\t\t\t\t<td SIDES=\"B\">{data}</td>"
