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
            self._data += '\n\t\t\t<tr>\n\t\t\t\t<td bgcolor="#324960" colspan=\'2\'>'
            self._data += f"\n\t\t\t\t\t<font color=\"white\">DATABASE: {db.name}</font>"
            self._data += '\n\t\t\t\t</td>\n\t\t\t</tr>'
            self.generateTables(db)
            self._data += '\n\t\t\t<tr>\n\t\t\t\t<td colspan=\'2\' SIDES="T"> </td>\n\t\t\t</tr>'

    def generateTables(self, database):
        for tb in database.tables:
            self._data += '\n\t\t\t<tr>\n\t\t\t\t<td bgcolor="#4fc3a1" colspan=\'2\' SIDES="LR">'
            self._data += f"\n\t\t\t\t\t<font color=\"white\">TABLE: {tb.name}</font>"
            self._data += '\n\t\t\t\t</td>\n\t\t\t</tr>'
            self.generateColumns(tb)

    def generateColumns(self, table):
        for col in table.columns:
            self.dataCol('Name', col.name)
            self.dataCol('Data Type', col.dataType)
            self.dataCol('Length', col.length)
            self.dataCol('Not Null', col.notNull)

            #self.dataCol('Primary Key', col.primaryKey)
            self._data += f"\n\t\t\t<tr>\n\t\t\t\t<td SIDES=\"LB\" ALIGN=\"RIGHT\"><b>Primary Key: </b></td>"
            self._data += f"\n\t\t\t\t<td SIDES=\"RB\" ALIGN=\"LEFT\">{col.primaryKey}</td>\n\t\t\t</tr>"

    def dataCol(self, name, data):
        self._data += f"\n\t\t\t<tr>\n\t\t\t\t<td SIDES=\"L\" ALIGN=\"RIGHT\"><b>{name}:</b></td>"
        self._data += f"\n\t\t\t\t<td SIDES=\"R\" ALIGN=\"LEFT\">{data}</td>\n\t\t\t</tr>"
