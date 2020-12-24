import tkinter as tk


class TextLineNumbers(tk.Canvas):
    def __init__(self, *args, **kwargs):
        tk.Canvas.__init__(self, *args, **kwargs)
        self.text = None

    def attach(self, text):
        self.text = text

    def redraw(self, *args):
        self.delete("all")

        i = self.text.index("@0,0")
        while True:
            dline = self.text.dlineinfo(i)
            if dline is None:
                break
            y = dline[1]
            linenum = str(i).split(".")[0]
            self.create_text(2, y, anchor="nw", font=(
                "Consolas", "10"), text=linenum)
            i = self.text.index("%s+1line" % i)
