from .data import E_MAIL_PROVIDERS as _E_MAIL_PROVIDERS, E_MAIL_PROVIDERS_W as _E_MAIL_PROVIDERS_W
from names import get_last_name as _names_last, get_first_name as _names_first
from random import choices as _rand_choices, randint as _rand_int
from string import digits as _str_digits, ascii_lowercase as _str_lower, ascii_uppercase as _str_upper, \
    punctuation as _str_punctuation


class FakeIdentity:

    def __init__(self) -> None:
        """
        Create a new fake identity. Details are only generated if needed.
        """
        self._first_name = None
        self._last_name = None
        self._e_mail = None
        self._password = None

    def _generate_first_name(self) -> None:
        """
        Generate the first name using the 'names' package.
        :return: None
        """
        self._first_name = _names_first()

    def _generate_last_name(self) -> None:
        """
        Generate the last name using the 'names' package.
        :return: None
        """
        self._last_name = _names_last()

    def _generate_e_mail(self) -> None:
        """
        Generate a random e-mail address based on the name.
        :return: None
        """
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

    def _generate_password(self) -> None:
        """
        Generate a random password.
        :return: None
        """
        rand = _rand_choices(['random'], [1])[0]
        password = ''  # noqa
        match rand:
            case 'random':
                length = _rand_choices([8, 9, 10, 11, 12, 15, 16, 20, 24, 32, 36, 44, 48, 50, 64],
                                       [1.5, 0.1, 0.5, 0.1, 0.7, 0.1, 1.5, 0.5, 0.7, 1,
                                        0.8, 0.1, 0.4, 0.8, 0.1, 0.5])[0]
                character_set = _rand_choices(['digits', 'lower', 'lower+upper', 'lower+digits',
                                               'lower+digits+punctuation', 'lower+upper+digits',
                                               'lower+upper+digits+punctuation'],
                                              [1, 1, 2, 2, 1, 4, 4])[0]
                character_sets = {'digits': _str_digits, 'lower': _str_lower, 'upper': _str_upper,
                                  'punctuation': _str_punctuation}
                characters = ''
                character_set_list = character_set.split('+')
                for k, v in character_sets.items():
                    if k in character_set_list:
                        characters += v
                for _ in range(length):
                    password += _rand_choices(characters)
        self._password = password

    def first_name(self) -> str:
        """
        Get the first name, which is randomly selected by the 'names' package.
        :return: The first name
        """
        if self._first_name is None:
            self._generate_first_name()
        return self._first_name

    def last_name(self) -> str:
        """
        Get the last name, which is randomly selected by the 'names' package.
        :return: The last name
        """
        if self._last_name is None:
            self._generate_last_name()
        return self._last_name

    def name(self) -> str:
        """
        Get the full name, which is randomly selected by the 'names' package.
        :return: The full name
        """
        if self._first_name is None:
            self._generate_first_name()
        if self._last_name is None:
            self._generate_last_name()
        return self._first_name + ' ' + self._last_name

    def e_mail(self) -> str:
        """
        Get a generated E-Mail address based on the full name.
        :return: An (hopefully non-existant) E-Mail address
        """
        if self._e_mail is None:
            self._generate_e_mail()
        return self._e_mail

    def password(self) -> str:
        """
        Get a random password.
        :return: A random password.
        """
        if self._password is None:
            self._generate_password()
        return self._password
