from tkinter import filedialog


class FileUploader:
    def __init__(self):
        # TODO unlock to allow any file formats
        filetypes = (
            ('Text files', '*.txt'),
            ('Images', '*.png*'),
            ('Videos', '*.avi*'),
        )

        self.file = filedialog.askopenfile(
            title='Open a file',
            initialdir='/',
            mode = 'r',
            filetypes=filetypes)

        if self.file:
            content = self.file.read()
            self.file.close()
            print("%d characters in this file" % len(content))
