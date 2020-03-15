
class URLCache:
    SEP_STR = "\n"

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
        return set(cache_file.read().split(self.SEP_STR))

    def save(self, cache_file):
        return cache_file.write(self.SEP_STR.join(self.cache))

    def add(self, url):
        self.cache.add(url)
