from tkinter import ttk


class LoadingView():
    def __init__(self, root):
        self._frame = ttk.Frame(root)
        self._initialize()

    def pack(self):
        self._frame.pack()

    def destroy(self):
        self._frame.destroy()

    def _initialize(self):
        load = ttk.Label(self._frame, text="Processing...")
        load.grid(row=0, column=0)
