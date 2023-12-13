from tkinter import Tk, ttk, Text, filedialog
from spell_checker import SpellChecker


class UI:
    def __init__(self):
        self._root = Tk()
        self._root.title("Spell Checker")
        self._root.geometry("800x600")
        self._root.grid_columnconfigure(0, weight=1)

    def _menu(self):
        input_title = ttk.Label(self._root, text="Input text:")
        input_field = Text(self._root, height=10)
        input_submit = ttk.Button(self._root, text="Submit")
        option = ttk.Label(self._root, text="or")
        file_submit = ttk.Button(
            self._root, text="Select file", command=filedialog.askopenfilename)

        input_title.grid(row=0, column=0)
        input_field.grid(row=1, column=0)
        input_submit.grid(row=2, column=0)
        option.grid(row=3, column=0)
        file_submit.grid(row=4, column=0)

    def run(self):
        self._menu()
        self._root.mainloop()
