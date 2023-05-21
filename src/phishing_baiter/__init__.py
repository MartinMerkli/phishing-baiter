from names import get_last_name as _names_last, get_first_name as _names_first


class FakeIdentity:

    def __init__(self):
        self._first_name = None
        self._last_name = None

    def _generate_first_name(self):
        self._first_name = _names_first()

    def _generate_last_name(self):
        self._last_name = _names_last()

    def first_name(self):
        if self._first_name is None:
            self._generate_first_name()
        return self._first_name

    def last_name(self):
        if self._last_name is None:
            self._generate_last_name()
        return self._last_name

    def name(self):
        if self._first_name is None:
            self._generate_first_name()
        if self._last_name is None:
            self._generate_last_name()
        return self._first_name + ' ' + self._last_name
