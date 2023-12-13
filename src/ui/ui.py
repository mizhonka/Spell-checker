from tkinter import Tk
from spell_checker import SpellChecker
from ui.main_view import MainView
from ui.loading_view import LoadingView
from ui.correction_view import CorrectionView


class UI:
    def __init__(self):
        self._root = Tk()
        self._root.title("Spell Checker")
        self._root.geometry("800x600")
        self._root.grid_columnconfigure(0, weight=1)
        self._current_view=None

    def _hide_current_view(self):
        if self._current_view:
            self._current_view.destroy()
        self._current_view=None

    def _show_menu(self):
        self._hide_current_view()
        self._current_view=MainView(self._root, self._handle_corrections)
        self._current_view.pack()

    def _show_correction_screen(self, suggestions):
        self._hide_current_view()
        self._current_view=CorrectionView(self._root, suggestions)
        self._current_view.pack()

    def _handle_corrections(self):
        data=self._current_view.input.get("1.0", "end")
        self._show_loading_screen()
        checker=SpellChecker(data)
        suggestions=checker.get_suggestions()
        self._show_correction_screen(suggestions)


    def _show_loading_screen(self):
        self._hide_current_view()
        self._current_view=LoadingView(self._root)
        self._current_view.pack()

    def run(self):
        self._show_menu()
        self._root.mainloop()
