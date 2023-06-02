from .email import EMAIL as _EMAIL
from ..utils import combine as _combine


LOCALES = []
DATA = {
    'email': email
}


def get_data(name, locale):
    resp = None
    if locale in DATA[name]:
        resp = _combine(resp, DATA[name][locale])
    if 'int' in DATA[name]:
        resp = _combine(resp, DATA['name']['int'])
    return resp
