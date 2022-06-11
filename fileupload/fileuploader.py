from tkinter import filedialog


class FileUploader:
    def __init__(self):
        # TODO unlock to allow any file formats
        filetypes = (
            ('Text files', '*.txt'),
            ('Images', '*.png*'),
            ('Zip files', '*.zip'),
            ('Videos', '*.avi*'),
        )

        self.file = filedialog.askopenfile(
            title='Open a file',
            initialdir='/',
            mode='r',
            filetypes=filetypes)
