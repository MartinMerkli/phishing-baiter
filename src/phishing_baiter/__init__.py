from .data import E_MAIL_PROVIDERS as _E_MAIL_PROVIDERS, E_MAIL_PROVIDERS_W as _E_MAIL_PROVIDERS_W
from names import get_last_name as _names_last, get_first_name as _names_first
from random import choices as _rand_choices, randint as _rand_int


class FakeIdentity:

    def __init__(self):
        self._first_name = None
        self._last_name = None
        self._e_mail = None

    def _generate_first_name(self):
        self._first_name = _names_first()

    def _generate_last_name(self):
        self._last_name = _names_last()

    def _generate_e_mail(self):
        if self._first_name is None:
            self._generate_first_name()
        if self._last_name is None:
            self._generate_last_name()
        provider = '@' + _rand_choices(_E_MAIL_PROVIDERS, _E_MAIL_PROVIDERS_W)[0]
        rand = _rand_choices(['first_last', 'first.last', 'last.first', 'firstlast', 'firstlast123', 'last',
                              'first@last'], [1, 1, 1, 1, 0.5, 0.2, 0.1])[0]
        e_mail = ''
        match rand:
            case 'first_last':
                e_mail = self._first_name + '_' + self._last_name + provider
            case 'first.last':
                e_mail = self._first_name + '.' + self._last_name + provider
            case 'last.first':
                e_mail = self._last_name + '_' + self._first_name + provider
            case 'firstlast':
                e_mail = self._first_name + self._last_name + provider
            case 'firstlast123':
                e_mail = self._first_name + self._last_name + str(_rand_int(0, 999)) + provider
            case 'last':
                e_mail = self._last_name + provider
            case 'first@last':
                domain = _rand_choices(['com', 'me', 'de', 'us', 'io', 'co.uk'], [1, 2, 0.2, 0.4, 0.4, 0.2])[0]
                e_mail = self._first_name + '@' + self._last_name + '.' + domain
        self._e_mail = e_mail

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

    def e_mail(self):
        if self._e_mail is None:
            self._generate_e_mail()
        return self._e_mail
