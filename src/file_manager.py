class FileManager:
    """
    This class reads input from a given file and writes corrected text to it.

    Attributes:
        _path (string): File path where the file is located.

    """

    def __init__(self, path):
        """
        The constructor for FileManager class.

        Parameters:
            path (string): File path where the file is located.

        """
        self._path = path

    def read_file(self):
        """
        Reads file at self._path.

        Returns:
            text (string): File content as string.
        """
        text = ""
        try:
            with open(self._path, encoding="utf-8") as file:
                for row in file:
                    row = row.replace("\n", " ")
                    text += row
            return text
        except FileNotFoundError:
            print("File not found\n")
            return None

    def write_file(self, text):
        """
        Writes corrected text to file.

        Parameters:
            text (string): Corrected text.
        """
        with open(self._path, "w", encoding="utf-8") as file:
            file.write(text)
