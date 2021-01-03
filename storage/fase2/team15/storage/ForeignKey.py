# -------------------------------
# Released under MIT License
# Copyright (c) 2020 TytusDb Team


class ForeignKey:

    def __init__(self, name: str, database: str, table: str, tableRef: str, columns: list, columnsRef: list):
        
        self.name=name
        self.database=database

        self.table=table
        self.tableRef=tableRef

        self.columns=columns
        self.columnsref=columnsRef
        