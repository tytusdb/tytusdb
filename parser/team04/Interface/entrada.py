import tkinter as tk
from tkinter import font
import re
from .customtext import CustomText
from .textlinenumbers import TextLineNumbers

class EntradaEditor(tk.Frame):
    def __init__(self, *args, **kwargs):
        tk.Frame.__init__(self, *args, **kwargs)
        self.text = CustomText(self)
        self.text.bind("<<Change>>", self._on_change)
        self.text.bind("<<TextModified>>", self.__textchanged__)

        self.text.configure(font=("Consolas", "10"))
        self.text.tag_config("red", foreground="red")
        self.text.tag_config("blue", foreground="#2874A6")
        self.text.tag_config("blue_bold", foreground="blue",
                             font=("Consolas", "10", "bold"))
        self.text.tag_config("yellow", foreground="#F4D03F")
        self.text.tag_config("pink", foreground="#FB54C6")

        self.linenumbers = TextLineNumbers(self, width=30)
        self.linenumbers.attach(self.text)
        self.linenumbers.pack(side="left", fill="y")
        self.text.pack(side="right", fill="both", expand=True)

        self.pack(side="top", fill="both", expand=True)

        self.nums = r'(\d+\.\d+)|(\d+)'
        self.strings = r'(\".*?\")'
        self.char = r'(\'.*?\')'
        self.reserved = r'smallint|integer|insert|bigint|decimal|numeric|real|double|precition|money|float|true|false|yes|no|off|character|varying|varchar|char|text|timestamp|data|time|interval|year|month|day|hour|minute|second|extract|data_part|now|current_date|current_time|between|symmetric|in|like|ilike|similar|is|isnull|notnull|not|and|or|if|else|sum|min|max|avg|count|abs|cbrt|ceil|ceiling|degrees|div|exp|factorial|floor|gcd|lcm|ln|log|log10|min_scale|mod|pi|power|radians|round|scale|sing|sqrt|trim_scale|truc|width_bucket|ramdom|setseed|acos|acosd|asin|asind|atan|atand|atan2|atand2d|cos|cosd|cot|cotd|sin|sind|tan|tand|sinh|consh|tanh|length|substring|trim|get_byte|md5|set_byte|sha256|substr|encode|decode|database|databases|create|insert|into|alter|table|show|drop|delete|primary|foreign|key|add|column|set|type|constraint|unique|check|references|exists|replace|owner|new_owner|current_user|session_user|mode|rename|inherits|values|update|where|fron|select|distinct|group|order|by|as|having|unknown|escape|any|all|some|left|right|full|outer|inner|join|on|using|natural|asc|desc|first|last|case|when|then|end|greatest|least|limit|offset|union|intersect|except|null|to'
        self.id = r'[a-zA-Z_][a-zA-Z_0-9]*'
        self.signs = r'(\+|-|\*|/|%|!|&&|\|\||\~|&|\||\^|<<|>>|==|!=|<|<=|>|>=|\(|\)|\[|\]|\{|\}|:|;|=|,)'
        self.comment = r'[#].*'

    def _on_change(self, event):
        self.linenumbers.redraw()

    def __textchanged__(self, event):
        for tag in self.text.tag_names():
            self.text.tag_remove(tag, '1.0', 'end')
        lines = self.text.get('1.0', 'end-1c').split('\n')

        for i, line in enumerate(lines):
            self.__applytag__(i, line, 'pink', self.nums, self.text)
            self.__applytag__(i, line, 'black', self.id, self.text)
            self.__applytag__(i, line, 'blue', self.reserved, self.text)
            self.__applytag__(i, line, 'blue_bold', self.strings, self.text)
            self.__applytag__(i, line, 'yellow', self.char, self.text)
            self.__applytag__(i, line, 'red', self.signs, self.text)
            self.__applytag__(i, line, 'green', self.comment, self.text)

    @ staticmethod
    def __applytag__(line, text, tag, regex, widget):
        indexes = [(m.start(), m.end()) for m in re.finditer(regex, text)]
        for x in indexes:
            widget.tag_remove(
                "blue_bold", f'{line+1}.{x[0]}', f'{line+1}.{x[1]}')
            widget.tag_remove("pink", f'{line+1}.{x[0]}', f'{line+1}.{x[1]}')
            widget.tag_remove("black", f'{line+1}.{x[0]}', f'{line+1}.{x[1]}')
            widget.tag_add(tag, f'{line+1}.{x[0]}', f'{line+1}.{x[1]}')
