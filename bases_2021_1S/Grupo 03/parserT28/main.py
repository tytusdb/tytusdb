import tkinter as tk
from parserT28.views.main_window import MainWindow

if __name__ == '__main__':
    root = tk.Tk()
    app = MainWindow(root)
    root.mainloop()
