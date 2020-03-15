class BaseKnownError:

    def __init__(self, filename: str, replacement: str, *args, **kwargs):
        self.filename = filename
        self.replacement = replacement

    def replace(self, file_content):
        raise NotImplementedError


class KnownCSVError(BaseKnownError):

    def __init__(self, filename: str, replacement: str,  linenr: int):
        super().__init__(filename, replacement)
        self.linenr = linenr

    def replace(self, csv_content: str):
        new_content = csv_content.split('\n')
        line_index = self.linenr - 1  # zero indexing
        new_content[line_index] = self.replacement
        return '\n'.join(new_content)


class KnownErrors:

    def __init__(self):
        self.known_errors = {}

    def add(self, known_error):
        if known_error.filename in self.known_errors:
            self.known_errors[known_error.filename].append(known_error)
        else:
            self.known_errors[known_error.filename] = [known_error]

    def replace(self, filename, file_content):
        known_errors = self.known_errors.get(filename, [])
        for i, known_error in enumerate(known_errors):
            print("Replacing error {} in {}".format(i+1, filename))
            file_content = known_error.replace(file_content)
        return file_content
