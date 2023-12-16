from tkinter import Tk
from spell_checker import SpellChecker
from ui.main_view import MainView
from ui.loading_view import LoadingView
from ui.correction_view import CorrectionView


class UI:
    def __init__(self):
        self._root = Tk()
        self._root.title("Spell Checker")
        self._root.geometry("800x400")
        self._root.grid_columnconfigure(0, weight=1, minsize=40)
        self._current_view = None

    def _hide_current_view(self):
        if self._current_view:
            self._current_view.destroy()
        self._current_view = None

    def _show_menu(self):
        self._hide_current_view()
        self._current_view = MainView(self._root, self._handle_corrections)
        self._current_view.pack()

    def _handle_corrections(self):
        data = self._current_view.input.get("1.0", "end")
        checker = SpellChecker(data)
        self._current_view.show_corrections(checker)

    def run(self):
        self._show_menu()
        self._root.mainloop()
