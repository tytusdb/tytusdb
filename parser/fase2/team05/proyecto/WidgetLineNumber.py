# GRUPO 5
# 201213062 - Mónica Raquel Calderon Muñoz
# 201213223 - Astrid Edith Hernandez Gonzalez
# 201213255 - Leonel Eduardo Avila Calvillo
# 201220159 - Diego Ahtohil Noj Armira
# 201220165 - Oscar Rolando Bernard Peralta

# IMPORT SECTION
import tkinter as tk
import tkinter.scrolledtext as st


# CREATING A CUSTOM SCROLLEDTEXT WIDGET
class TextAreaWidget(st.ScrolledText):
    def __init__(self, *args, **kwargs):
        st.ScrolledText.__init__(self, *args, **kwargs)

        # Create a proxy for the underlying widget
        self._orig = self._w + "_orig"
        self.tk.call("rename", self._w, self._orig)
        self.tk.createcommand(self._w, self._proxy)

    def _proxy(self, *args):
        try:
            # Let the actual widget perform the requested action
            cmd = (self._orig,) + args
            result = self.tk.call(cmd)

            if (args[0] in ("insert", "replace", "delete") or
                    args[0:3] == ("mark", "set", "insert") or
                    args[0:2] == ("xview", "moveto") or
                    args[0:2] == ("xview", "scroll") or
                    args[0:2] == ("yview", "moveto") or
                    args[0:2] == ("yview", "scroll")
            ):
                self.event_generate("<<Change>>", when="tail")

            # Return what the actual widget returned
            return result
        except:
            pass


# CREATING LINE NUMBERS
class LineNumber(tk.Canvas):
    def __init__(self, *args, **kwargs):
        tk.Canvas.__init__(self, *args, **kwargs)
        self.text_widget = None

    def attach(self, text_widget):
        self.text_widget = text_widget

    def redraw(self, *args):
        """ redraw line numbers """
        self.delete("all")

        i = self.text_widget.index("@0,0")
        while True:
            dline = self.text_widget.dlineinfo(i)
            if dline is None: break
            y = dline[1]
            linenum = str(i).split(".")[0]
            self.create_text(2, y, anchor="nw", text=linenum)
            i = self.text_widget.index("%s+1line" % i)
