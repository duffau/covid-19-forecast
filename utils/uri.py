import re


def clean(s):
    re_replace_dash = r'\s|\,'
    re_remove = r'[^a-zA-Z0-9_\-]'
    s = s.lower()
    s = re.sub(re_replace_dash, '-', s)
    s = re.sub(re_remove, '', s)
    return s
