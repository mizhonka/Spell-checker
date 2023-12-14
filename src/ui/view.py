from tkinter import ttk


class View:
    def __init__(self, root):
        self._frame = ttk.Frame(root)
        self._initialize()

    def pack(self):
        self._frame.pack()

    def destroy(self):
        self._frame.destroy()
