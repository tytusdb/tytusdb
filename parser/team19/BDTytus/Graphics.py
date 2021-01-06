import platform
version = platform.python_version_tuple()[0]

if version=='2':
    import Tkinter as Tkinter
    import tkFileDialog
    import tkFont
    import ttk
    import tkMessageBox as tkMessageBox

elif version=='3':
    from tkinter import ttk
    from tkinter import font as tkFont
    import tkinter as Tkinter
    from tkinter import filedialog as tkFileDialog
    import tkinter.messagebox as tkMessageBox

else:
    raise Exception("Unable To Import Tkinter Module")
    exit()
