import pickle


class URLCache:

    def __init__(self, cache_file=None):
        if cache_file:
            self.cache = self.read(cache_file)
        else:
            self.cache = set()

    def read(self, cache_file):
        if cache_file.tell() > 0:
            return pickle.load(cache_file)
        else:
            return set()

    def save(self, cache_file):
        pickle.dump(self.cache, cache_file)
