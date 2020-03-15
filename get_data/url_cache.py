import pickle


class URLCache:

    def __init__(self, cache_file=None):
        if cache_file:
            loaded_cache = self.read(cache_file)
            self.cache = set(loaded_cache)
        else:
            self.cache = set()

    def __repr__(self):
        return self.cache.__repr__()

    def __contains__(self, item):
        return item in self.cache

    def read(self, cache_file):
        return pickle.load(cache_file)

    def save(self, cache_file):
        pickle.dump(self.cache, cache_file)

    def add(self, url):
        self.cache.add(url)
