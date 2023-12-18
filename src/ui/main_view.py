from tkinter import ttk, Text, filedialog, constants, font

class MainView():
    """
    This class controls what is shown in

    Attributes:
        _frame (Frame): Tkinter frame containing all the elements.
        command (method): Method from the UI class that initializes a SpellChecker.
        checker (SpellChecker): Instance of SpellChecker.
        suggestions (list): Contains tuples of correction suggestions given by SpellChecker.
        def_font (font): Default font.
        first_word (Label): Label showing an incorrectly spelled word.
        second_word (Label): Label showing a correction suggestion.
        correction_title (Label): Title showed when going through correction suggestions.
        input (Text): Text field for user input.
        submit (Button): Button used to submit the user input.
        accept (Button): Button used to accept a correction suggestion.
        skip (Button): Button used to skip a correction suggestion.
    """

    def __init__(self, root, command):
        """
        The constructor for MainView class.

        Parameters:
            root (Tk): Source window for _frame.
            command (method): Assigns self.command.

        """
        self._frame = ttk.Frame(root)
        self.command=command
        self.checker=None
        self.suggestions=None
        self.def_font=font.nametofont("TkDefaultFont")
        self._initialize()

    def _start(self):
        """
        Calls self.command and begins the correction process.

        """
        self.submit["state"]="disabled"
        self.submit["text"]="Processing..."
        self._frame.update_idletasks()
        self.command()

    def _stop(self):
        """
        Returns the submit button to its orginal state.

        """
        self.submit["state"]="normal"
        self.submit["text"]="Submit"

    def _show_next(self):
        """
        Shows the next correction suggestion.

        """
        if not self.suggestions:
            self.first_word.grid_remove()
            self.correction_title.grid_remove()
            self.second_word.grid_remove()
            self.accept.grid_remove()
            self.skip.grid_remove()
            self.input.delete("1.0", "end")
            self.input.insert("1.0", self.checker.get_text())
            self._stop()
            self.pack()
            return
        pair=self.suggestions[0]
        self.first_word["text"]=f"{self.checker.get_word_at(pair[0])}"
        self.second_word["text"]=f"{pair[1]}?"

    def _no_mistakes(self):
        """
        Shows the correction title when there are no misspellings.

        """
        self.correction_title["text"]="There are no spelling mistakes, yay!"
        self.correction_title.grid()
        self._stop()

    def _skip_correction(self):
        """
        Skips a correction suggestion.

        """
        self.suggestions.pop(0)
        self._show_next()

    def _accept_correction(self):
        """
        Accepts a correction suggestion.

        """
        pair=self.suggestions.pop(0)
        self.checker.correct(pair[0], pair[1])
        self._show_next()

    def show_corrections(self, checker):
        """
        Calls checker.get_suggestions() and shows necessary ui elements.

        """
        self.checker=checker
        self.suggestions=[(r,s) for r, s in checker.get_suggestions().items()]
        if not self.suggestions:
            self._no_mistakes()
            return
        self.first_word.grid()
        self.correction_title.grid()
        self.second_word.grid()
        self.accept.grid()
        self.skip.grid()
        self._show_next()

    def pack(self):
        """
        Packs all the elements inside _frame.

        """
        self._frame.pack()

    def destroy(self):
        """
        Destroys _frame.

        """
        self._frame.destroy()

    def _open_file(self):
        """
        Shows a file dialog for opening a file and writes it contents inside self.input.

        """
        file = filedialog.askopenfile(filetypes=[("Text files", "*.txt")])
        if not file:
            return
        content = ""
        for row in file:
            content += row
        self.input.delete("1.0", "end")
        self.input.insert("1.0", content)

    def _save_file(self):
        """
        Shows a file dialog for saving a file and overwrites a file with the contents of self.input.

        """
        file = filedialog.asksaveasfile()
        if not file:
            return
        file.write(self.input.get("1.0", "end"))

    def _initialize(self):
        """
        Creates all the ui elements.

        """
        input_field = Text(self._frame, height=10)
        input_field.insert("1.0", "Type text here or select a file...")

        input_submit = ttk.Button(self._frame, text="Submit", command=self._start)

        self.input = input_field
        self.submit=input_submit

        file_save = ttk.Button(
            self._frame, text="Save as...", command=self._save_file)
        file_submit = ttk.Button(
            self._frame, text="Open file", command=self._open_file)

        first_word=ttk.Label(self._frame, font=(self.def_font['family'], self.def_font['size'], 'bold'))
        second_word=ttk.Label(self._frame, font=(self.def_font['family'], self.def_font['size'], 'bold'))
        correction_title=ttk.Label(self._frame, text="did you mean")
        accept_button=ttk.Button(self._frame, text="Accept", command=self._accept_correction)
        skip_button=ttk.Button(self._frame, text="Skip", command=self._skip_correction)


        file_submit.grid(row=0, column=0)
        file_save.grid(row=0, column=1)
        input_field.grid(row=1, column=0, columnspan=2, sticky=(constants.E, constants.W))

        first_word.grid(row=2, column=0)
        first_word.grid_remove()
        self.first_word=first_word

        correction_title.grid(row=3, column=0)
        correction_title.grid_remove()
        self.correction_title=correction_title

        second_word.grid(row=4, column=0)
        second_word.grid_remove()
        self.second_word=second_word

        accept_button.grid(row=5, column=0)
        accept_button.grid_remove()
        self.accept=accept_button

        skip_button.grid(row=6, column=0)
        skip_button.grid_remove()
        self.skip=skip_button

        input_submit.grid(row=7, column=0)
