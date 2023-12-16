from tkinter import ttk, Text, filedialog, constants

class MainView():
    def __init__(self, root, command):
        self._frame = ttk.Frame(root)
        self.command=command
        self.checker=None
        self.suggestions=None
        self._initialize()

    def _start(self):
        self.submit["state"]="disabled"
        self.submit["text"]="Processing..."
        self.command()

    def _stop(self):
        self.submit["state"]="normal"
        self.submit["text"]="Submit"

    def _show_next(self):
        if not self.suggestions:
            self.correction_title.grid_remove()
            self.accept.grid_remove()
            self.skip.grid_remove()
            self.input.delete("1.0", "end")
            self.input.insert("1.0", self.checker.get_text())
            self._stop()
            self.pack()
            return
        pair=self.suggestions[0]
        self.correction_title["text"]=f"'{self.checker.get_word_at(pair[0])}', did you mean '{pair[1]}'?"
        self.pack()

    def _no_mistakes(self):
        self.correction_title["text"]="There are no spelling mistakes, yay!"
        self.correction_title.grid()
        self._stop()

    def _skip_correction(self):
        self.suggestions.pop(0)
        self._show_next()

    def _accept_correction(self):
        pair=self.suggestions.pop(0)
        self.checker.correct(pair[0], pair[1])
        self._show_next()

    def show_corrections(self, checker):
        self.checker=checker
        self.suggestions=[(i,s) for i, s in checker.get_suggestions().items()]
        if not self.suggestions:
            self._no_mistakes()
            return
        self.correction_title.grid()
        self.accept.grid()
        self.skip.grid()
        self._show_next()

    def pack(self):
        self._frame.pack()

    def destroy(self):
        self._frame.destroy()

    def _open_file(self):
        file = filedialog.askopenfile(filetypes=[("Text files", "*.txt")])
        content = ""
        for row in file:
            content += row
        self.input.delete("1.0", "end")
        self.input.insert("1.0", content)

    def _save_file(self):
        file = filedialog.asksaveasfile()
        file.write(self.input.get("1.0", "end"))

    def _initialize(self):
        input_field = Text(self._frame, height=10)
        input_field.insert("1.0", "Type text here or select a file...")

        input_submit = ttk.Button(self._frame, text="Submit", command=self._start)

        self.input = input_field
        self.submit=input_submit

        file_save = ttk.Button(
            self._frame, text="Save as...", command=self._save_file)
        file_submit = ttk.Button(
            self._frame, text="Open file", command=self._open_file)

        correction_title=ttk.Label(self._frame, text="Did you mean...")
        accept_button=ttk.Button(self._frame, text="Accept", command=self._accept_correction)
        skip_button=ttk.Button(self._frame, text="Skip", command=self._skip_correction)
        file_submit.grid(row=0, column=0)
        file_save.grid(row=0, column=1)
        input_field.grid(row=1, column=0, columnspan=2, sticky=(constants.E, constants.W))

        correction_title.grid(row=2, column=0)
        correction_title.grid_remove()
        self.correction_title=correction_title

        accept_button.grid(row=3, column=0)
        accept_button.grid_remove()
        self.accept=accept_button

        skip_button.grid(row=3, column=1)
        skip_button.grid_remove()
        self.skip=skip_button

        input_submit.grid(row=4, column=0)
