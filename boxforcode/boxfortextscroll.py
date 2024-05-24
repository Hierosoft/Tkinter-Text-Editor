__author__ = "Aryan Khandelwal, Jake Gustafson"
import tkinter as tk
from tkinter import ttk


class BoxForTextScroll(tk.Text):
    """
    Class used to Make a TextWidget
    having horizontal and vertical
    scrollbars
    """

    def __init__(self, master=None, **kw):
        self.frame = ttk.Frame(master)
        self.vbar = ttk.Scrollbar(self.frame, command=self.yview)
        self.vbar.pack(side=tk.RIGHT, fill=tk.Y)
        self.hbar = ttk.Scrollbar(
            self.frame, orient="horizontal", command=self.xview)
        self.hbar.pack(side=tk.BOTTOM, fill=tk.X)
        kw.update({'yscrollcommand': self.vbar.set})
        kw.update({'xscrollcommand': self.hbar.set})
        tk.Text.__init__(self, self.frame, **kw)
        self.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
        text_meths = vars(tk.Text).keys()
        methods = (vars(tk.Pack).keys()
                   | vars(tk.Grid).keys()
                   | vars(tk.Place).keys())
        methods = methods.difference(text_meths)

        for m in methods:
            if m[0] != '_' and m != 'config' and m != 'configure':
                setattr(self, m, getattr(self.frame, m))

    def __str__(self):
        return str(self.frame)
