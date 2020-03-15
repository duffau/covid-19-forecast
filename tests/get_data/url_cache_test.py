import pytest
import pickle
import io
from get_data.url_cache import URLCache


@pytest.fixture
def url_set_member():
    return 'a'


@pytest.fixture
def url_set_non_member():
    return 'z'


@pytest.fixture
def url_set(url_set_member):
    return {url_set_member, 'b', 'c'}


@pytest.fixture
def url_cache(url_set):
    cache_file = io.BytesIO()
    pickle.dump(url_set, cache_file)
    cache_file.seek(0)  # Reset cursor to head of file
    return URLCache(cache_file)


def test_init():
    URLCache()


def test_init_with_empty_file():
    cache_file = io.BytesIO()
    with pytest.raises(EOFError):
        URLCache(cache_file)


def test_init_with_pickled_file(url_set):
    cache_file = io.BytesIO()
    pickle.dump(url_set, cache_file)
    cache_file.seek(0)  # Reset cursor to head of file
    print("size:", cache_file.tell())
    url_cache = URLCache(cache_file)
    assert url_cache.cache == url_set


def test_init_with_cache_file_cant_cast_to_set():
    cache_file = io.BytesIO()
    pickle.dump(42, cache_file)
    cache_file.seek(0)  # Reset cursor to head of file
    with pytest.raises(TypeError):
        URLCache(cache_file)


def test_repr(url_cache):
    assert url_cache.__repr__() == url_cache.cache.__repr__()


def test_is_member_in_url_cache(url_set_member, url_cache):
    assert url_set_member in url_cache


def test_is_not_member_in_url_cache(url_set_non_member, url_cache):
    assert url_set_non_member not in url_cache
