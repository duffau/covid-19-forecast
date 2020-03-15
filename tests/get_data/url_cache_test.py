import pytest
import pickle
import io
from get_data.url_cache import URLCache


@pytest.fixture
def url_set():
    return {'a', 'b', 'c'}


def test_init():
    URLCache()


def test_init_with_empty_file():
    cache_file = io.BytesIO()
    URLCache(cache_file)


def test_init_with_pickled_file(url_set):
    cache_file = io.BytesIO()
    pickle.dump(url_set, cache_file)
    cache_file.seek(0)  # Reset cursor to head of file
    URLCache(cache_file)
