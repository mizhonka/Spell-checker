from tkinter import ttk


class CorrectionView():
    def __init__(self, root, suggestions):
        self._frame = ttk.Frame(root)
        self.input = None
        self._initialize(suggestions)

    def pack(self):
        self._frame.pack()

    def destroy(self):
        self._frame.destroy()

    def _initialize(self, suggestions):
        content = ""
        for index, suggestion in suggestions.items():
            content += suggestion+"\n"
        info = ttk.Label(self._frame, text=content)
        info.grid(row=0, column=0)
