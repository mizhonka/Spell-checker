from tkinter import ttk, Text, filedialog

class MainView():
    def __init__(self, root, command):
        self._frame=ttk.Frame(root)
        input_field = Text(self._frame, height=10)
        input_field.insert("1.0", "Type text here or select a file...")
        self.input=input_field
        self._initialize(command)

    def pack(self):
        self._frame.pack()

    def destroy(self):
        self._frame.destroy()

    def _open_file(self):
        file=filedialog.askopenfile(filetypes=[("Text files", "*.txt")])
        content=""
        for row in file:
            content+=row
        self.input.delete("1.0", "end")
        self.input.insert("1.0", content)

    def _save_file(self):
        file=filedialog.asksaveasfile()
        file.write(self.input.get("1.0", "end"))

    def _initialize(self,command):
        input_submit = ttk.Button(self._frame, text="Submit", command=command)
        file_save=ttk.Button(self._frame, text="Save as...", command=self._save_file)
        file_submit = ttk.Button(
            self._frame, text="Open file", command=self._open_file)

        file_submit.grid(row=0, column=0)
        self.input.grid(row=2, column=0)
        file_save.grid(row=1, column=0)
        input_submit.grid(row=3, column=0)

